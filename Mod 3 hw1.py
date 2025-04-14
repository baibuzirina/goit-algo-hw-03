from datetime import datetime

def get_days_from_today(date):
    
    try:

        # Перетворення рядка у datetime
        given_date = datetime.strptime(date, "%Y-%m-%d").date()

        # Поточна дата
        today = datetime.today().date()

        # Різниця між датами
        delta = today - given_date
        return delta.days

    except ValueError:
        print("Помилка. Введіть дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').")
        return None


# Введення дати
date_input = input("Введіть дату у форматі 'РРРР-ММ-ДД' (наприклад, 2020-10-09): ") 

result = get_days_from_today(date_input)

if result is not None:  # Якщо немає помилки
    print(f"Різниця між поточною датою та заданою датою: {result}")