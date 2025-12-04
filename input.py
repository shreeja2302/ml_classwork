# input.py
# Creates:
#   data/my_data.csv
#   data/notes.txt
#   data/audio.wav   (fake 1-second sine wave)
#   data/data.json
#   logs/app.log

from pathlib import Path
import json
import math
import wave
import struct

import pandas as pd

BASE_DATA = Path("data")
BASE_LOGS = Path("logs")


def ensure_dirs():
    BASE_DATA.mkdir(parents=True, exist_ok=True)
    BASE_LOGS.mkdir(parents=True, exist_ok=True)


def make_csv(path=BASE_DATA / "my_data.csv"):
    df = pd.DataFrame(
        {
            "id": [1, 2, 3],
            "name": ["Alice", "Bob", "Charlie"],
            "score": [85, 90, 78],
        }
    )
    df.to_csv(path, index=False)
    print(f"created {path}")


def make_text(path=BASE_DATA / "notes.txt"):
    lines = [
        "This is a demo notes file.\n",
        "Line 2: some more text.\n",
        "Line 3: project B-321.\n",
    ]
    path.write_text("".join(lines), encoding="utf-8")
    print(f"created {path}")


def make_json(path=BASE_DATA / "data.json"):
    data = [
        {"user": "alice", "age": 21, "city": "Delhi"},
        {"user": "bob", "age": 22, "city": "Mumbai"},
    ]
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(f"created {path}")


def make_log(path=BASE_LOGS / "app.log"):
    lines = [
        "2025-12-04T07:00:00Z INFO Application started\n",
        "2025-12-04T07:00:05Z WARN Low disk space\n",
        "2025-12-04T07:00:10Z ERROR Failed to connect to DB\n",
    ]
    path.write_text("".join(lines), encoding="utf-8")
    print(f"created {path}")


def make_wav(path=BASE_DATA / "audio.wav", duration_sec=1.0, sr=16000):
    """Create a simple 440Hz sine wave WAV file."""
    n_samples = int(duration_sec * sr)
    amp = 16000
    freq = 440.0

    with wave.open(str(path), "w") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # 16-bit
        wf.setframerate(sr)

        for n in range(n_samples):
            t = n / sr
            sample = int(amp * math.sin(2 * math.pi * freq * t))
            wf.writeframes(struct.pack("<h", sample))

    print(f"created {path}")


if __name__ == "__main__":
    ensure_dirs()
    make_csv()
    make_text()
    make_json()
    make_log()
    make_wav()
