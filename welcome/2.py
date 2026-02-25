nums = ['a', 'b', 'a', 'c', 'a', 'b']

def count_el(n):
    data = {}
    counter = 0
    for el in n:
        if el in data:
            data[el] += 1
        else:
            data[el] = 1

    return data

print(count_el(nums))
