import random

# Запит умов лотереї
print("Умови лотереї: ")    
min_value = int(input("Введіть мінімальне число (min >=1): "))
max_value = int(input("Введіть максимальне число (max <=1000): "))
quantity_value = int(input("Введіть кількість чисел, які потрібно вибрати (quantity від 1 та між min і max) : "))

def get_numbers_ticket(min_value, max_value, quantity_value):

    try:

        if not (1 <= min_value <= max_value <= 1000):
            print(f"Помилка при введенні діапазону чисел в лотереї (від 1 до 1000)")
            return []
        
        if not (1 <= quantity_value <= (max_value-min_value+1)):
            print(f"Помилка в веденні кількості чисел, які потрібно вибрати (від 1 та між min і max)")   
            return []

        # Генерація та сортування унікальних випадкових чисел

        lottery_numbers = random.sample(range(min_value, max_value+1), quantity_value)
        return sorted(lottery_numbers)

    except ValueError:
        print(f"Помилка при введенні умов лотереї: введено не числові значення")
        return []

# Вивід Лотерейних чисел або помилки
result = get_numbers_ticket(min_value, max_value, quantity_value)

if result:  # Якщо немає помилки
    print(f"Лотерейні числа: {result}")

else:  # Якщо Помилка при введенні умов лотереї
    print(f"Помилка при введенні умов лотереї")
