number1 = int(input( "User please enter number 1:"))
number2 = int(input( "User please enter number 2:"))
operation = input("Choose among the following +,-,*,/:")
if operation == "+":
    sum = number1 + number2 
    print("The sum is {}".format(sum))
elif operation == "-":
    subtraction  = number1 - number2 
    print("The subtraction is {}".format(subtraction))
elif operation == "*" :
    multiplication = number1 * number2 
    print("The multiplication is {}".format(multiplication))
elif operation == "/" :
    if number2 != 0 :
        division = number1/number2
        print("The division is {}".format(division))
    else:
        print("Divison is invalid")

else:
    print("Please choose a valid operator from +,-,*,/ and try again ")
