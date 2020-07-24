def twosum(nums, target):
    print("confirm start")

    info = input("List at least 2 numbers (ex. 1,2,3,4):  ")
    info = info.split(",")

    num1 = info[0]
    num2 = info[1]

    print(num1 + " + " + num2 + " = " + str(int(num1) + int(num2)))

    # does same thing
    print("{} + {} = {}".format(num1, num2, int(num1)+int(num2)))

    return 

def main():
    print(twosum([2, 7, 11, 15], 9)) # [0, 1]
    print(twosum([2, 7, 11, 15], 9) == [0, 1]) # True
    print(twosum([2, 7, 11, 15], 18) == [1, 2]) 

if __name__ == '__main__': 
    main()