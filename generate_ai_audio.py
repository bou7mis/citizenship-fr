#!/usr/bin/env python3
"""
Generate ultra-high-fidelity AI voice audio files for citizenship video lessons
using Azure / Edge Neural Speech (fr-FR-VivienneMultilingualNeural or fr-FR-DeniseNeural).
"""

import os
import json
import asyncio
import edge_tts

VOICE = "fr-FR-VivienneMultilingualNeural"  # Highly natural, clear, warm French studio voice
RATE = "+0%"  # Natural pacing

async def generate_lesson_audio(chapter_id="m1-c1"):
    with open("data/video_lessons.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    lesson = data["lessons"].get(chapter_id)
    if not lesson:
        print(f"Lesson {chapter_id} not found")
        return

    out_dir = f"audio/video_lessons/{chapter_id}"
    os.makedirs(out_dir, exist_ok=True)

    print(f"Generating AI audio for lesson: {lesson['title']} ({len(lesson['scenes'])} scenes)")

    for idx, scene in enumerate(lesson["scenes"]):
        out_file = f"{out_dir}/scene_{idx + 1}.mp3"
        text = scene["narrationText"]
        print(f"  [Scene {idx + 1}] Generating audio: {out_file}")
        
        communicate = edge_tts.Communicate(text, VOICE, rate=RATE)
        await communicate.save(out_file)

        # Update scene metadata in json with local audio path
        scene["audioSrc"] = out_file
        print(f"  ✓ Saved ({os.path.getsize(out_file)} bytes)")

    # Save updated video_lessons.json with audioSrc
    with open("data/video_lessons.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("\nAll AI voice audio files generated successfully!")

if __name__ == "__main__":
    asyncio.run(generate_lesson_audio("m1-c1"))
