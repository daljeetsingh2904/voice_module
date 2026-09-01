from faster_whisper import WhisperModel

print("Loading Whisper Model...")

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

print("Whisper Model Ready.\n")


def speech_to_text(audio_path):
    """
    Converts speech into text.
    """

    segments, info = model.transcribe(audio_path)

    transcript = ""

    for segment in segments:
        transcript += segment.text + " "

    return transcript.strip()


if __name__ == "__main__":

    audio_file = "sample.mp3"

    text = speech_to_text(audio_file)

    print("Transcript:")
    print(text)