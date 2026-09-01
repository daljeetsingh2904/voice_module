from sentiment_service import analyze_text
from llm_response_service import generate_reply
from text_to_speech import speak
from ticket_service import create_ticket
from conversation_logger import save_conversation
from call_service import create_call, end_call

conversation_history = []

current_call_id = create_call()

print("\n===== AI Voice Agent Started =====")

while True:

    transcript = input("\nCustomer: ").strip()

    # -----------------------------------
    # Customer Ends Call
    # -----------------------------------

    if transcript.lower() in ["bye", "exit", "quit"]:

        print("\nConversation Ended.")

        speak("Thank you for contacting Technical Support. Goodbye.")

        end_call(current_call_id)

        break

    # -----------------------------------
    # Sentiment Analysis
    # -----------------------------------

    result = analyze_text(transcript)

    print("\nSentiment Result:")

    for key, value in result.items():
        print(f"{key} : {value}")

    # -----------------------------------
    # AI Reply
    # -----------------------------------

    reply = generate_reply(
        transcript,
        conversation_history[-4:]
    )

    # -----------------------------------
    # Conversation Resolved
    # -----------------------------------

    resolved_words = [
        "thank you",
        "thank u",
        "thanks",
        "thx",
        "resolved",
        "fixed",
        "working now",
        "works now",
        "it works",
        "it worked",
        "did work",
        "did worked",
        "problem solved",
        "issue solved",
        "issue resolved",
        "that helped",
        "that worked"
    ]

    if any(word in transcript.lower() for word in resolved_words):

        reply = (
            "I'm glad your issue has been resolved. "
            "Thank you for contacting Technical Support. "
            "Have a great day!"
        )

        print("\nAI:")
        print(reply)

        speak(reply)

        conversation_history.append(
            {
                "customer": transcript,
                "ai": reply
            }
        )

        save_conversation(
            current_call_id,
            transcript,
            reply,
            result["sentiment"],
            result["emotion"]
        )

        end_call(current_call_id)

        print("\nConversation Ended.")

        break

    # -----------------------------------
    # Save Conversation
    # -----------------------------------

    conversation_history.append(
        {
            "customer": transcript,
            "ai": reply
        }
    )

    # -----------------------------------
    # Escalation Conditions
    # -----------------------------------

    escalate = False
    reason = ""

    if result["risk"] == "HIGH":

        escalate = True
        reason = "High Risk Customer"

    elif any(word in transcript.lower() for word in [
        "supervisor",
        "manager",
        "human",
        "agent",
        "complaint"
    ]):

        escalate = True
        reason = "Customer Requested Supervisor"

    elif len(conversation_history) >= 5:

        escalate = True
        reason = "Troubleshooting Unsuccessful"

    elif any(word in reply.lower() for word in [
        "escalate",
        "further investigation",
        "requires escalation"
    ]):

        escalate = True
        reason = "AI Recommended Escalation"

    # -----------------------------------
    # Escalation Reply
    # -----------------------------------

    if escalate:

        ticket = create_ticket(
            transcript,
            result["sentiment"],
            result["emotion"],
            reason
        )

        reply = (
            "Based on the information you've shared, your issue requires further investigation.\n\n"
            f"Ticket ID: {ticket}\n\n"
            "Please keep this Ticket ID for future reference.\n"
            "Our technical support team will review your issue.\n"
            "Thank you for contacting Technical Support."
        )

        print("\nAI:")
        print(reply)

        speak(reply)

        save_conversation(
            current_call_id,
            transcript,
            reply,
            result["sentiment"],
            result["emotion"]
        )

        end_call(current_call_id)

        print("\nConversation Ended.")

        break

    # -----------------------------------
    # Normal Reply
    # -----------------------------------

    print("\nAI:")
    print(reply)

    speak(reply)

    save_conversation(
        current_call_id,
        transcript,
        reply,
        result["sentiment"],
        result["emotion"]
    )