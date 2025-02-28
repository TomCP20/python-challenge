"""bin"""
from base64 import b64decode
import io
import wave

with open("hex.txt", encoding="utf-8") as f:
    data = b64decode("".join(f.readlines()))

w = wave.Wave_read(io.BytesIO(data))

with wave.open("result.wav", "wb") as h:
    h: wave.Wave_write
    h.setnchannels(w.getnchannels())
    h.setsampwidth(w.getsampwidth()//2)
    h.setframerate(w.getframerate()*2)
    frames = w.readframes(w.getnframes())
    h.writeframes(frames)
