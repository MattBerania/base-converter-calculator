
# Name: Matthew Berania
# Base Converter Calculator
#   The problem is that while doing discrete math and computer organization homework,
# it takes too long to convert from base to base, thus the creation of a Base Converter
# Calculator which takes in the initial base, the number and changes it into the new base
# that the user chooses.

def Converter(base, num, change):
    # creates a function called Converter and takes in 3 inputs
    printNum = num
    # printNum is just a holder for the original input, since the original num is altered throughout the code-
    if base == '10' or base == 'decimal':
        # if base is equal to 10 or equal to decimal(this if statement is using OR)
        try:
            num = int(num)
            # int(num) turns the number that is input(which is a string) into a integer, which
            # represents base 10
        except ValueError:
            # ^ the try, except ValueError will print invalid if the code above produces an error
            # in this case if the num entered digits aren't numbers(0-9/decimal)
            print("invalid num")
            return None
            # return None returns None to wherever Converter() is being called from, which in this
            # case is from a while loop. This resets the while loop and starts from the beginning
    elif base == '2' or base == 'binary':
        # if the 'base' is equal to  '2' or 'binary', it will run the try code below
        # this elif statement also is using OR
        try:
            num = int(num, 2)
            # the int() fxn turns whatever num is into an int, the 2 represents the base it's is converting
            # from, which is base 2 aka Binary
        except ValueError:
            # the ValueError just prevents the code from stopping and producing an error code when there is an error
            # in this case it is used when the num entered digits aren't in 0 or 1(binary)
            print("invalid num")
            return None
    elif base in ('8', 'octal'):
        # if the 'base' is in '8' or 'octal', it will run the try code below
        # this elif statemend is using a simpler(shortcut) version of a or statement, it will 
        # check if the input given is in whatever is in the brackets
        try:
            num = int(num, 8)
            # the 8 in the int() fxn represents the base it's converting from which is base 8
            # aka Octal
        except ValueError:
            # for this ValueError, it is used when the num entered digits aren't in 0-7()
            print("invalid num")
            return None
    elif base in ('16', 'hexadecimal'):
        # if the 'base' is in '16' or 'hexadecimal', it will run the try code below
        # this elif is also using shortcut version of OR statement
        try:
            num = int(num, 16)
            # the 16 in the int() fxn represents the base it's converting from which is base 16
            # aka Hexadecimal
        except ValueError:
            # for this, it is used when the digits of the 'num' entered aren't in 0-9,abcdef(hexadecimal)
            print("invalid num")
            return None
    else:
        print("invalid")
        return None
        # else is used if the base inputted isn't valid

    if change in ('10', 'decimal'):
        return (printNum + " into base 10(Decimal form) is: " + str(num))
        # str(num) is used so that no error messages show up
    elif change in ('2', 'binary'):
        num = bin(num)
        # bin(num) converts the integer num into binary(base 2)
        return (printNum + " into base 2(Binary form) is: " + str(num[2:]))
        # str(num[2:]) just removes the 0b from the num(to look better)
        # and converts it into a string so no error msg appears
    elif change in ('8', 'octal'):
        num = oct(num)
        # oct(num) converts the integer num into octal(base 8)
        return (printNum + " into base 8(Octal form) is: " + str(num[2:]))
        # str(num[2:]) just removes the 0o from the num(to look better)
    elif change in ('16', 'hexadecimal'):
        num = hex(num)
        # hex(num) converts the integer num into hexadecimal(base 1)
        return (printNum + " into base 16(Hexadecimal form) is: " + str(num[2:]))
        # str(num[2:]) just removes the 0x from the num(to look better)
    else:
        print("invalid base change")
        return None
        # else meaning that if the base that they want to change into isn't one of the ones
        # listed, then tells the user it is invalid and will return None to reset the loop


print("_____________________________________")
print("Welcome to Base Converter Calculator")

while True:
    # while loop is True, this just runs the loop indefinetely. It will stop once break is used.
    base1 = input("Enter the base/number system(10, 2, 8, 16): ")
    # user input for the number system that is originally used
    num = input("Enter the number: ")
    # user input for the number being used in the number system previously specified
    base2 = input("Enter the base conversion(10, 2, 8, 16): ")
    # user input for the number system they want to convert to

    print(Converter(base1, num, base2))
    # prints out the fxn Converter() using the three inputs from the user
    # all of the inputs that are collected are strings

    on_off = input("Turn Calculator 'on' or 'off':\n")
    if on_off in 'off' or on_off in 'Off':
        # the Or statement is just used if the user puts a capital 'O'
        break
        # if the user inputs 'off' or 'Off' it will break the while loop
    else:
        (print(""))
        # code just for aesthetics, it will skip a line

print("Have a good day :)")
print("_____________________________________")
