def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

try:
    user_input = int(input("Enter a number: "))
    result = check_even_odd(user_input)
    print(f"{user_input} is {result}.")
except ValueError:
    print("Please enter a valid integer.")
