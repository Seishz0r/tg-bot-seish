nums = {
    'a':1,
    'b':2,
    'c':3, }

def invert_dict(dict):
    new_dict = {}
    for k, v in dict.items():
        new_dict[v] = k

    return new_dict

print(nums)
print(invert_dict(nums))
