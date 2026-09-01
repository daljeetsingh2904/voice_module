from llm_response_service import generate_reply


reply = generate_reply(

    "My internet is not working.",

    []
)

print("\nAI Reply:\n")

print(reply)