import re

def normalize_phone(phone_number):
    pattern = r"[^\d]"
    normalized_number = re.sub(pattern, "", phone_number)
    if normalized_number.startswith("380"):
        normalized_number = "+" + normalized_number
    elif normalized_number.startswith("0"):
        normalized_number = "+38" + normalized_number
    elif normalized_number.startswith("80"):
        normalized_number = "+3" + normalized_number
    return normalized_number