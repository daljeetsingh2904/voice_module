def detect_intent(text):

    text = text.lower()

    if any(word in text for word in
           [
               "internet",
               "wifi",
               "network",
               "connection"
           ]):
        return "INTERNET_ISSUE"

    elif any(word in text for word in
             [
                 "restart",
                 "restarted"
             ]):
        return "ROUTER_RESTARTED"

    elif any(word in text for word in
             [
                 "supervisor",
                 "manager",
                 "escalate"
             ]):
        return "ESCALATION"

    elif any(word in text for word in
             [
                 "thank",
                 "thanks"
             ]):
        return "THANKS"

    return "UNKNOWN"