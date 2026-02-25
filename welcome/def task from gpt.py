# Напиши функцию greet, которая:
# Принимает один параметр — имя (строку)
# Возвращает строку вида:
# Привет, <имя>!

def greet(name):
    if name:
        return 'hello ' + name + '!'
    else:
        return 'hello! guest'


ans = input('what is your name? ')
fnl = greet(ans)

print(fnl)