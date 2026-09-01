import sys

sys.path.append(
    r"C:\Users\Welcome\Desktop\sentiment-module"
)

from services.emotion_service import EmotionService


emotion_service = EmotionService()


def analyze_text(text):

    emotion, sentiment, confidence = (
        emotion_service.detect_emotion(text)
    )

    risk = (
        emotion_service.get_risk_level(
            emotion
        )
    )

    alert, precaution = (
        emotion_service.get_alert(
            emotion
        )
    )

    return {
        "emotion": emotion,
        "sentiment": sentiment,
        "confidence": confidence,
        "risk": risk,
        "alert": alert,
        "precaution": precaution
    }