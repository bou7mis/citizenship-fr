#!/usr/bin/env python3
"""
Generate Studio Neural AI Audio Lessons for all 18 Chapters.
Uses Azure / Edge Neural TTS: fr-FR-VivienneMultilingualNeural.
Saves audio to audio/chapters/{chapter_id}.mp3 and updates data/course.json.
"""

import os
import re
import json
import asyncio
import edge_tts

VOICE = "fr-FR-VivienneMultilingualNeural"
RATE = "+0%"

def clean_text(text):
    if not text:
        return ""
    # Strip emojis
    emoji_pattern = re.compile(r"[\U00010000-\U0010ffff]", flags=re.UNICODE)
    cleaned = emoji_pattern.sub("", text)
    # Strip symbols
    misc_pattern = re.compile(r"[\u2600-\u26ff\u2700-\u27bf\ufe0f]")
    cleaned = misc_pattern.sub("", cleaned)
    # Strip markdown emphasis
    cleaned = re.sub(r"\*{1,3}([^*]+)\*{1,3}", r"\1", cleaned)
    # Remove HTML tags if any
    cleaned = re.sub(r"<[^>]+>", "", cleaned)
    # Normalize whitespace
    cleaned = re.sub(r"[ \t]+", " ", cleaned).strip()
    return cleaned

def build_chapter_narration(c):
    lines = []
    lines.append(f"Chapitre : {clean_text(c['title'])}.\n")

    if "highlights" in c and c["highlights"]:
        lines.append("Points clés à retenir pour votre entretien civique :")
        for h in c["highlights"]:
            cleaned = clean_text(h)
            if cleaned:
                lines.append(f"- {cleaned}")
        lines.append("")

    if "content" in c:
        for b in c["content"]:
            b_type = b.get("type")
            if b_type in ("intro", "paragraph"):
                t = clean_text(b.get("text", ""))
                if t:
                    lines.append(f"{t}\n")
            elif b_type == "section":
                title = clean_text(b.get("title", ""))
                if title:
                    lines.append(f"{title} :")
                text = clean_text(b.get("text", ""))
                if text:
                    lines.append(text)
                if b.get("points"):
                    for pt in b["points"]:
                        pt_clean = clean_text(pt)
                        if pt_clean:
                            lines.append(f"- {pt_clean}")
                lines.append("")
            elif b_type == "callout":
                title = clean_text(b.get("title", "Remarque importante"))
                text = clean_text(b.get("text", ""))
                if text:
                    lines.append(f"{title} : {text}\n")
            elif b_type == "grid":
                for it in b.get("items", []):
                    title = clean_text(it.get("title", ""))
                    desc = clean_text(it.get("text", ""))
                    if title or desc:
                        lines.append(f"{title} : {desc}")
                lines.append("")
            elif b_type == "timeline":
                lines.append("Repères chronologiques majeurs :")
                for ev in b.get("events", []):
                    d = clean_text(ev.get("date", ""))
                    t = clean_text(ev.get("title", ""))
                    desc = clean_text(ev.get("desc", ""))
                    lines.append(f"En {d}, {t}. {desc}")
                lines.append("")
            elif b_type == "table":
                for row in b.get("rows", []):
                    row_clean = [clean_text(cell) for cell in row if clean_text(cell)]
                    if row_clean:
                        lines.append(" - ".join(row_clean))
                lines.append("")

    if "interviewQuestions" in c and c["interviewQuestions"]:
        lines.append("Questions types de l'entretien préfectoral :")
        for q in c["interviewQuestions"]:
            q_text = clean_text(q.get("question", ""))
            a_text = clean_text(q.get("answer", ""))
            tip = clean_text(q.get("tip", ""))
            if q_text and a_text:
                lines.append(f"Question : {q_text}")
                lines.append(f"Réponse : {a_text}")
                if tip:
                    lines.append(f"Conseil : {tip}")
                lines.append("")

    return "\n".join(lines).strip()

async def generate_audio_file(sem, text, out_file, label):
    if os.path.exists(out_file) and os.path.getsize(out_file) > 10000:
        print(f"  [Skipping existing] {label} ({os.path.getsize(out_file)} bytes)", flush=True)
        return True

    async with sem:
        for attempt in range(3):
            try:
                print(f"  [Generating] {label} ({len(text)} chars)...", flush=True)
                comm = edge_tts.Communicate(text, VOICE, rate=RATE)
                await comm.save(out_file)
                size = os.path.getsize(out_file)
                print(f"  ✓ Saved ({size} bytes) -> {out_file}", flush=True)
                await asyncio.sleep(0.3)
                return True
            except Exception as e:
                print(f"  ✗ Error on {label} (attempt {attempt+1}): {e}", flush=True)
                await asyncio.sleep(1.5)
    return False

async def main():
    os.makedirs("audio/chapters", exist_ok=True)

    with open("data/course.json", "r", encoding="utf-8") as f:
        course_data = json.load(f)

    tasks = []
    sem = asyncio.Semaphore(4) # 4 concurrent generations for faster download

    total_chapters = 0
    for mod in course_data["modules"]:
        for chap in mod["chapters"]:
            total_chapters += 1
            chap_id = chap["id"]
            out_file = f"audio/chapters/{chap_id}.mp3"
            chap["audioSrc"] = out_file
            narration = build_chapter_narration(chap)
            tasks.append(generate_audio_file(sem, narration, out_file, f"{chap_id}: {chap['title'][:30]}"))

    print(f"Starting neural AI audio generation for {total_chapters} chapters...")
    results = await asyncio.gather(*tasks)

    success_count = sum(1 for r in results if r)
    print(f"\nFinished: {success_count}/{total_chapters} audio files generated.")

    # Save updated course.json with audioSrc
    with open("data/course.json", "w", encoding="utf-8") as f:
        json.dump(course_data, f, ensure_ascii=False, indent=2)
    print("Updated data/course.json with audioSrc paths.")

if __name__ == "__main__":
    asyncio.run(main())
