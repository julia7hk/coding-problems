s = input("Enter a lowercase string:    ")

slist = list(s)
print(slist)
print(len(slist))
print(slist[0])

sdict = {}
for x in range(len(slist)):
    if slist[x] in sdict:
        sdict[slist[x]] = sdict[slist[x]] + 1
    else:
        sdict[slist[x]] = 1

print(sdict)

for x, y in sdict.items():
    if y == 1:
        char = x
        break
    else:
        pass

print("Character:", char, "    Index:", slist.index(char))