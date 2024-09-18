size = int(input("Enter the size of the pattern:"))
i=0
while i in range(size):
    for j in range(size):
        print("*", end="")
    i+=1
    print()