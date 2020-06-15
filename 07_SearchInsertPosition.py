print("confirm start")

nums = input("List multiple numbers (ex. 1,3,5,6):    ")
search = input("List a number to search (ex. 5):   ")

listnums = list(nums)


i = 0
while i < len(listnums):
    if listnums[i] == ',':
        listnums.pop(i)
    else:
        pass
    
    i += 1

i = 0
while i < len(listnums):
    if search == listnums[i]:
        print("{} is item number {} in the list entered".format(search, i))
        break
    else:
        print("{} is not item number {} in the list entered".format(search, i))

    
    i += 1



# def Search(string, int):
#     print(len(string))

#     i = 0
#     char = []

#     while i <= len(string):
#         char.append(string[0]) 
#         i += 1
    
#     print(string)
#     print(type(string))
#     # for i in char:
#     #     print(i)
#     #     char.append()


# Search(nums, search)