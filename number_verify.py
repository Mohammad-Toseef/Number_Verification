from typing import Dict

import phonenumbers
from phonenumbers import carrier
PHONE_NUMBER_STATUSES = {
    "VALID": 1,
    "INVALID": 2,
}


def phone_number_validation_helper(phone_number: str):
    number = phone_number
    try:
        entered_phone_number = phonenumbers.parse(number)
        number_valid = phonenumbers.is_valid_number(entered_phone_number)
        return {
            "phone_number_status": (PHONE_NUMBER_STATUSES["VALID"] if number_valid
                                    else PHONE_NUMBER_STATUSES["INVALID"])
        }

    except Exception:
        return {"phone_number_status": PHONE_NUMBER_STATUSES["INVALID"]}


