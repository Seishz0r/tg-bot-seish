file = open('text','r')

def count_lines(f):
    count = 0
    for line in f:
        if line.strip() != '':
            count += 1

    return count


print(count_lines(file))


file.close()