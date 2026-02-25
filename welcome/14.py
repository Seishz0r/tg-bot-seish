# def safe_devide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return 'На 0 делить нельзя!'
#     except ValueError:
#         return 'Вводите числа!'
#
# a = int(input())
# b = int(input())
# print(safe_devide(a,b))

def get_int():
    while True:
        try:
            num = int(input("Enter a number: "))
            return num
        except ValueError:
            print('Введите число!')


print(get_int())


