hare = 5
tortois = 11
j = 0
count = 0
while j < 20:
    if hare < tortois:
        hare *=2
        print(hare)
    elif hare == tortois:
        break
    else:
        tortois += 1
        print(tortois)

print(hare + tortois)
