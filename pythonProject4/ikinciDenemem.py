
while True:
    number = float(input("Please enter a number: "))
    if number.is_integer():
        if number % 2 == 0:
            print("Number is even")
        else:
            print("Number is odd")
        break
    else:
        print("Please try again\n")