# I am using simple functions, if, elif and else statements for this very basic calculator :)
  
def addition():
    first_value = int(input("Enter your first value: "))
    second_value = int(input("Enter your second value: "))
    return(first_value + second_value)

def subtraction():
    first_value = int(input("Enter your first value: "))
    second_value = int(input("Enter your second value: "))
    return(first_value - second_value)

def multiplication():
    first_value = int(input("Enter your first value: "))
    second_value = int(input("Enter your second value: "))
    return(first_value * second_value)

def division():
    first_value = int(input("Enter your first value: "))
    second_value = int(input("Enter your second value: "))
    return(first_value // second_value)

print("Hello Welcome the simple calculator")
calculator = input("Please enter which operation do you want to perform (+, -, * or / ): ").lower()
if calculator == "+":
    print(f"Your final value is : {addition()}")

elif calculator == "-":
    print(f"Your final value is : {subtraction()}")

elif calculator == "*":
    print(f"Your final value is : {multiplication()}")

elif calculator == "/":
    print(f"Your final value is : {division()}")

else:
    print("Please enter a correct operation which you want to perform.")

print("Thank you for using our calculator")

# Just run it. Peace :)