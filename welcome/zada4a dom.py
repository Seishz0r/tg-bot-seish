#в доме 100 квартир 5 подьездов 4 кв на этаж
#вход - кв, выход номер подьезда и этажа
kv = input('what is your number of kvartira?')
kv = int(kv)
if kv < 20:
    pod = (kv - 1) // 20 + 1
    flr = (kv - 1) // 4 + 1
else:
    pod = (kv - 1) // 20 + 1
    flr = ((kv - 1) % 20) // 4 + 1
print('your podezd is', pod,)
print('your floar is', flr)
