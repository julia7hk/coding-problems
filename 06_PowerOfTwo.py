print("confirm start")

num = input("List an integer:   ")
newnum = int(num)

while newnum > 0:
    if newnum == 1:
        print(num + ' is a power of 2')
        break
    elif newnum % 2 == 0:
        newnum = newnum / 2
    else:
        print(num + ' is not a power of 2')
        break