'''
# print("line 1 this line is printed")
# print("line 2 this line is printed")
# print("line 3 this line is printed")
# print('line 4 this line is printed')
# a=10
# print("Tom is ",a,".")

# integer_example = 10.
# float_example = 10.5
# print(type(integer_example), type(float_example))
# list=["aa","ab","ac","ad","ae","af"]
# print(f"My favourite actor is: {list[2]}")


#iterative approach of factorial of given number.
def factorial_iterative(n):
    # Initialize result as 1 (since factorial of 0 is 1)
    result = 1
    for i in range(1, n + 1):
        result *= i  # Multiply result by the current number
    return result
num = 5
print(factorial_iterative(num))  # Output: 120


#recursive approach for factorial:
def factorial_recursive(n):
    if n == 0 or n == 1:  # Base case: factorial of 0 or 1 is 1
        return 1
    else:
        return n * factorial_recursive(n - 1)  # Recursive call

num = 5
print(factorial_recursive(num))  # Output: 120


#recursive approach with user input:
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Ask the user for input
num = int(input("Enter a number to calculate its factorial: "))

# Calculate the factorial and print the result
result = factorial_recursive(num)
print(f"The factorial of {num} is {result}")
'''

'''Reverse string function'''
'''
def reverse_string(s):
    reversed_str = ""  # Initialize an empty string to store the reversed string
    for char in s:
        reversed_str = char + reversed_str  # Prepend each character to the reversed string
    return reversed_str
# Ask for user input
input_string = input("Enter a string to reverse: ")

# Call the reverse function
reversed_string = reverse_string(input_string)

# Print the result
print(f"Reversed string: {reversed_string}")

'''

'''Palindrome check'''
'''
def is_palindrome(s):
    # Remove any spaces and convert to lowercase for case-insensitive comparison
    s = s.replace(" ", "").lower()
    
    # Compare the string with its reverse
    return s == reverse_string(input_string) #s[::-1]

# Ask for user input
#input_string = input("Enter a string to check if it is a palindrome: ")

# Check if the string is a palindrome
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

'''
'''Prime number check'''

def is_prime(n):
    # Numbers less than 2 are not prime
    if n < 2:
        return False
    # Check for factors from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:  # If n is divisible by any number other than 1 and itself, it's not prime
            return False
    return True

def find_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Ask for user input
start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

# Find primes in the given range
prime_numbers = find_primes_in_range(start, end)

# Print the result
print(f"Prime numbers between {start} and {end} are: {prime_numbers}")
