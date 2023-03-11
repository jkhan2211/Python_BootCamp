def sum_of(*args):
    sum = 0 
    for x in args:
        sum += x
    return sum

print(sum_of(coffee=2.99, cake=4.55, juice=2.999))