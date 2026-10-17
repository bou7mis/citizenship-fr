#!/usr/bin/env python3
"""
Batch Neural AI Audio Generator for all 18 Chapters.
Uses edge-tts with fr-FR-VivienneMultilingualNeural.
Skips existing audio files for efficiency.
"""

import os
import json
import asyncio
import edge_tts

VOICE = "fr-FR-VivienneMultilingualNeural"
RATE = "+0%"

async def generate_scene_audio(sem, text, out_file, scene_label):
    if os.path.exists(out_file) and os.path.getsize(out_file) > 1000:
        print(f"  [Skipping existing] {scene_label}")
        return True

    async with sem:
        for attempt in range(3):
            try:
                print(f"  [Generating] {scene_label} -> {out_file}")
                comm = edge_tts.Communicate(text, VOICE, rate=RATE)
                await comm.save(out_file)
                print(f"  ✓ Saved ({os.path.getsize(out_file)} bytes) {scene_label}")
                await asyncio.sleep(0.4)
                return True
            except Exception as e:
                print(f"  ✗ Error on {scene_label} (attempt {attempt+1}): {e}")
                await asyncio.sleep(2.0)
    return False

async def main():
    with open("data/video_lessons.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    lessons = data["lessons"]
    print(f"Total lessons to process: {len(lessons)}")

    sem = asyncio.Semaphore(2)  # 2 concurrent requests
    tasks = []

    for chap_id, lesson in lessons.items():
        out_dir = f"audio/video_lessons/{chap_id}"
        os.makedirs(out_dir, exist_ok=True)

        for idx, scene in enumerate(lesson["scenes"]):
            out_file = f"{out_dir}/scene_{idx + 1}.mp3"
            scene["audioSrc"] = out_file
            text = scene["narrationText"]
            label = f"{chap_id} s{idx + 1}"
            tasks.append(generate_scene_audio(sem, text, out_file, label))

    print(f"Queued {len(tasks)} scene audio generation tasks...")
    results = await asyncio.gather(*tasks)
    success_count = sum(1 for r in results if r)
    print(f"\nCompleted! {success_count} / {len(tasks)} scene audios ready.")

    # Save final video_lessons.json with all audioSrc populated
    with open("data/video_lessons.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    asyncio.run(main())
