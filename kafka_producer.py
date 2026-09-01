from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def send_transcript(call_id, transcript):

    message = {
        "call_id": call_id,
        "customer_text": transcript
    }

    producer.send(
        "voice-transcripts",
        value=message
    )

    producer.flush()

    print("Transcript sent to Kafka:")
    print(message)