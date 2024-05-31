
import re

phones = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    '00004546575     !!!'
]


def normalize_phone(phone_number: str) -> str:
    formatted = re.sub(r'[^0-9]', '', phone_number)
    if len(formatted) == 10:
        formatted = '+38' + formatted

    elif len(formatted) == 12:
        formatted = '+' + formatted
    else:
        return f'{formatted} : некоректний номер'

    return formatted


if __name__ == "__main__":
    valid_phones = [normalize_phone(phone) for phone in phones]
    print(valid_phones)

