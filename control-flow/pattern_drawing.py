size = int(input("Enter the size of the pattern: "))
count = 0
while count < size:
    count += 1
    for i in range(size):
        print("*",end = "")
    print()
