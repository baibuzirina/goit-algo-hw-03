import re

def normalize_phone(phone_number):


  # Видалення всіх символів, крім цифр та символу '+'
    pattern = r"[^+\d]"
    replacement = ""
    phone_number = re.sub (pattern, replacement, phone_number)

  # Якщо номер починається з '380', заміна на  '+380'
    pattern = r"^380"
    replacement = "+380"
    phone_number = re.sub(pattern, replacement, phone_number)

  # Якщо номер починається з '8', додаємо '+38'
    pattern = r"^8"
    replacement = "+38"
    phone_number = re.sub(pattern, replacement, phone_number) 

  # Якщо номер починається з '0', заміна на '+380'
    pattern = r"^0"
    replacement = "+380"
    phone_number = re.sub(pattern, replacement, phone_number) 

    return phone_number


#  Тестування
phone_numbers = [
"+38(050)123-32-34",
"     0503451234",
"(050)8889900",
"38050-111-22-22",
"38050 111 22 11   "
]

for phone_number in phone_numbers:
    print(normalize_phone(phone_number))