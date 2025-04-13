from datetime import datetime

def get_days_from_today():

    try:

    # Введення дати
        date_input = input("Введіть дату у форматі 'РРРР-ММ-ДД' (наприклад, 2020-10-09): ") 

    # Перетворення рядка у datetime
        given_date = datetime.strptime(date_input, "%Y-%m-%d").date()

    # Поточна дата
        today = datetime.today().date()

    # Різниця між датами
        delta = today - given_date
        return delta.days

    except ValueError:
        print("Помилка. Введіть дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').")
        return None

result = get_days_from_today()
if result is not None:  # Якщо немає помилки
    print(f"Різниця між поточною датою та заданою датою: {result}")