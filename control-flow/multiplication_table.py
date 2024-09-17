number = int(input("Enter a number to see its multiplication table:"))

for i in range(10):
    print(number, "x", i+1, "=", number*(i+1))