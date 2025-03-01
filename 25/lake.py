"""lake"""
import wave

from PIL import Image

output = Image.new("RGB", (300,300))
for i in range(25):
    wav: wave.Wave_read = wave.open(f"lake{i+1}.wav")
    byte = wav.readframes(wav.getnframes())
    img = Image.frombytes("RGB", (60, 60), byte)
    output.paste(img, (60 * (i % 5), 60 * (i // 5)))
output.show()
