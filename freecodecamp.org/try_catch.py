try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
except ValueError:
    print("That's not a valid number. Please try again.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:    print("This block will always execute, regardless of whether an exception occurred or not.")

# Example of handling multiple exceptions
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("You cannot divide by zero.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    
# Example of using else with try-except
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number. Please try again.")
else:
    print(f"You entered: {number}")
