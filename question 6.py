# Question 6:
    
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an
# integral number between 1 and n (both included). and then the program should print the dictionary.

# Suppose the following input is supplied to the program:
# 8

# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

# Then accept any integer in the range of 1 to n and disp

# Function to generate a dictionary with squares of numbers
def generate_square_dict(n):
    return {i: i*i for i in range(1, n+1)}

# Ask the user for the input number n
n = int(input("Enter an integer: "))

# Generate the dictionary
square_dict = generate_square_dict(n)

# Print the generated dictionary
print(square_dict)
