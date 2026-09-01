from audio_service import convert_audio_to_text

audio_file = "sample.wav"

text = convert_audio_to_text(audio_file)

print("\nTranscript:\n")
print(text)