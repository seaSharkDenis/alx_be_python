size = int(input("Enter the size of the pattern: "))
count = size

while count > 0:
    for i in range(size):
        print("*", end="")
    count-=1
    print()
