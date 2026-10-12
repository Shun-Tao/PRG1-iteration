def countdown(start):
    for i in range(start,0, -1):
        print(i)
    print("Liftoff")

def first_over(limit, readings):

    checked = 0

    for reading in readings:
        checked += 1

        if reading > limit:
            return checked

    return None
    


countdown(3)
countdown(0)

print(first_over(100, [45, 92, 130, 88]))
print(first_over(100, [45, 92, 88]))
