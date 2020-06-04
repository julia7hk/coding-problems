print("confirm start")

word = input("Type a word:  ")

def ToArray(string):
    i = len(string)-1
    output = []
    while i>=0:
        output.append(string[i])
        i -= 1
    print(output)

ToArray(word)