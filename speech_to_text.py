from faster_whisper import WhisperModel

print("Loading Whisper model...")

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

print("Model loaded successfully.\n")

segments, info = model.transcribe("sample.mp3")

print("Detected Language:", info.language)
print("\nTranscript:\n")

for segment in segments:
    print(segment.text)