def generate_reply(
        result,
        conversation_history=None
):

    emotion = result["emotion"]

    if conversation_history:

        last_customer_message = (
            conversation_history[-1]["customer"]
            .lower()
        )

        if (
            "supervisor" in last_customer_message
            or "manager" in last_customer_message
        ):
            return (
                "I understand. "
                "Please wait while I connect "
                "you to a supervisor."
            )

    if emotion == "ANGRY":

        return (
            "I am sorry for the inconvenience. "
            "Since when are you facing this issue?"
        )

    elif emotion == "FRUSTRATED":

        return (
            "I understand your frustration. "
            "Have you already contacted support?"
        )

    elif emotion == "NEGATIVE":

        return (
            "I am sorry for the inconvenience. "
            "Could you please explain your issue further?"
        )

    elif emotion == "POSITIVE":

        return (
            "Thank you for your feedback. "
            "We are glad that you are satisfied."
        )

    return (
        "Thank you for contacting customer support."
    )