def extract_latest_user_message(messages):
    for message in reversed(messages):
        role = getattr(message, "role", None)
        if role == "user":
            return getattr(message, "content", "")
    return ""

def format_recommendations(items):
    return [
        {
            "name": item["name"],
            "url": item["url"],
            "test_type": item["test_type"],
        }
        for item in items[:10]
    ]
