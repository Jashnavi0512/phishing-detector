def check_phishing(message):
    message = message.lower()

    phishing_keywords = [
        "urgent", "click here", "verify", "password",
        "bank", "account locked", "login", "update",
        "suspend", "confirm", "free", "winner", "lottery"
    ]

    score = 0

    for word in phishing_keywords:
        if word in message:
            score += 1

    if "http://" in message or "https://" in message:
        score += 2

    if score >= 3:
        return "⚠️ High Risk Phishing"
    elif score == 2:
        return "⚠️ Suspicious Message"
    else:
        return "✅ Safe Message"



user_input = input("Enter the email/message: ")
result = check_phishing(user_input)
print("\nResult:", result)