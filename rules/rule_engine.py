import conversation_state
from ticket_service import create_ticket


def get_rule_reply(
        intent,
        transcript,
        history
):

    text = transcript.lower()


    if intent == "INTERNET_ISSUE":

        conversation_state.current_state = "ASK_DURATION"

        return (
            "Since when are you facing this issue?"
        )


    if conversation_state.current_state == "ASK_DURATION":

        conversation_state.current_state = "ASK_RESTART"

        return (
            "Have you restarted your router?"
        )


    if conversation_state.current_state == "ASK_RESTART":

        if "yes" in text:

            ticket = create_ticket()

            conversation_state.current_state = (
                "TICKET_CREATED"
            )

            return (
                f"Your issue has been escalated.\n"
                f"Your Ticket ID is {ticket}.\n"
                f"Our technical team will contact you shortly."
            )

        elif "no" in text:

            return (
                "Please restart your router once and let me know if the issue persists."
            )


    if intent == "ESCALATION":

        conversation_state.current_state = None

        return (
            "Connecting you to our supervisor."
        )


    if intent == "THANKS":

        conversation_state.current_state = None

        return (
            "Thank you for contacting customer support."
        )


    return None