# Напиши функцию calc(a, b, op), где:
# a и b — числа
# op — строка: "+", "-", "*", "/"
# Функция должна возвращать результат операции.

def calc(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '/':
        return a / b
    elif op == '*':
        return a * b

num1 = int(input("Enter a number#1: "))
num2 = int(input("Enter a number#2: "))
z = input('Enter a symbol: ')

print(calc(num1, num2, z))