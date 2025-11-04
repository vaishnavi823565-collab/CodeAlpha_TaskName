

def compound_interest(principal, rate, time):
    # Calculates compound interest
    Amount = principal * (pow((1 + rate / 100), time))
    CI = Amount - principal
    print("Compound interest is", CI)

# Driver code
# Taking input from the user
principal = int(input("Enter the principal amount: "))
rate = float(input("Enter rate of interest: "))
time = int(input("Enter time in years: "))

# Function call
compound_interest(principal, rate, time)


# Write a Python Function for reversing a string and call

def reverse_string_loop(s):
    """Reverses a string by iterating through it and prepending each character."""
    reversed_s = ""
    for char in s:
        # Prepend the current character to the new string
        reversed_s = char + reversed_s
    return reversed_s  # return outside the loop

# Call the function
original_string = "Python"
reversed_string = reverse_string_loop(original_string)

print("Original string:", original_string)
print("Reversed string:", reversed_string)

    
    