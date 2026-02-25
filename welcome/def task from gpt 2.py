# Напиши функцию square_or_cube(number), которая:
# если число чётное → возвращает его квадрат
# если нечётное → возвращает его куб

def sqr_or_cube(x):
    if x % 2 == 0:
        return x ** 2
    else:
        return x ** 3


num = int(input("Enter a number: "))
print(sqr_or_cube(num))