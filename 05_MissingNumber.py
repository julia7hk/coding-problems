print("confirm start")

numbers = input("List multiple numbers with a number missing (ex. 3,0,1 - missing 2):   ")

listnums = list(numbers)
print(listnums)

i = 0
while i < len(listnums):
    if listnums[i] == ',':
        listnums.pop(i)
    else:
        pass
    
    i += 1


integers = []
for x in range(len(listnums)):
    integers.append(int(listnums[x]))


nums = []
for y in range(len(integers)):
    nums.append(min(integers))
    integers.pop(integers.index(min(integers)))


for a in range(len(nums)):
    if a == nums[a]:
        pass
    else:
        print(a, "is the missing number")
        break