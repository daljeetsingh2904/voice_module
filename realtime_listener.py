import time
from audio_service import speech_to_text
from sentiment_service import analyze_text
from response_service import generate_reply
from text_to_speech import speak


audio_file = "sample.mp3"

while True:

    print("\nListening...")

    transcript = speech_to_text(
        audio_file
    )

    print("\nCustomer:")
    print(transcript)

    result = analyze_text(
        transcript
    )

    reply = generate_reply(
        result
    )

    print("\nAI:")
    print(reply)

    speak(reply)

    time.sleep(5)