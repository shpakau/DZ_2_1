# 1.	Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = float(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number
def sumNums(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum

num = InputNumbers("Введите вещественное число: ")
print(f"Сумма цифр введенного числа= {sumNums(num)}")