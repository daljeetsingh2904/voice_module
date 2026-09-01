import sys

sys.path.append(
    r"C:\Users\Welcome\Desktop\sentiment-module"
)

# PostgreSQL Repositories
from postgres.call_repository import CallRepository
from postgres.transcript_repository import TranscriptRepository
from postgres.sentiment_repository import SentimentRepository
from postgres.emotion_repository import EmotionRepository
from postgres.analytics_repository import AnalyticsRepository
from postgres.escalation_repository import EscalationRepository
from postgres.ai_response_repository import AIResponseRepository

# Models
from models.sentiment import Sentiment
from models.emotion import Emotion
from models.analytics import Analytics
from models.escalation import Escalation
from models.ai_response import AIResponse

# Voice Module Files
from audio_service import speech_to_text
from sentiment_service import analyze_text
from response_service import generate_reply
from text_to_speech import speak


# -----------------------
# Create Call
# -----------------------

call_repository = CallRepository()

CALL_ID = call_repository.create_call(1)

print("Call ID:", CALL_ID)


# -----------------------
# Speech To Text
# -----------------------

audio_file = "sample.mp3"

transcript = speech_to_text(
    audio_file
)

print("\nTranscript:")
print(transcript)


# -----------------------
# Save Transcript
# -----------------------

TranscriptRepository().save_transcript(
    CALL_ID,
    transcript
)


# -----------------------
# Sentiment Analysis
# -----------------------

result = analyze_text(
    transcript
)

print("\n===== RESULT =====")

for key, value in result.items():
    print(f"{key} : {value}")


# -----------------------
# Save Sentiment
# -----------------------

sentiment = Sentiment(
    CALL_ID,
    result["sentiment"],
    result["confidence"]
)

SentimentRepository().save_sentiment(
    sentiment
)


# -----------------------
# Save Emotion
# -----------------------

emotion = Emotion(
    CALL_ID,
    result["emotion"],
    result["confidence"]
)

EmotionRepository().save_emotion(
    emotion
)


# -----------------------
# Save Analytics
# -----------------------

analytics = Analytics(
    CALL_ID,
    120,
    "RESOLVED",
    result["confidence"]
)

AnalyticsRepository().save_analytics(
    analytics
)


# -----------------------
# Escalation
# -----------------------

if result["risk"] == "HIGH":

    escalation = Escalation(
        CALL_ID,
        result["emotion"],
        result["alert"]
    )

    EscalationRepository().save_escalation(
        escalation
    )


# -----------------------
# Generate AI Reply
# -----------------------

reply = generate_reply(result)

print("\nAI Reply:")
print(reply)

speak(reply)

# -----------------------
# Save AI Reply
# -----------------------

response = AIResponse(
    CALL_ID,
    reply
)

AIResponseRepository().save_response(
    response
)

print("\nEverything saved successfully.")