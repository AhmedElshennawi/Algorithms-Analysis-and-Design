import math

# Initialize variables
sd = ava = a = b = 0
x = []

# Get the number of elements from the user
n = int(input("N = "))

# Input values and calculate the sum
for i in range(n):
    if i < n:  # Loop to get n values
        x.append(int(input(f"X [{i}] = ")))  # Input and add value to the list
        ava += x[i]  # Calculate the sum
        i += 1

# Calculate the mean (average) of the entered values
ava = ava / n

# Calculate the variance (a) and standard deviation (sd)
for i in range(n):
    if i < n:  # Loop to process n values
        a += math.pow(x[i] - ava, 2)  # Calculate variance 'a'

# Calculate the standard deviation 'sd'
b = a / n
sd = math.sqrt(b)

# Print the calculated standard deviation
print("Standard Deviation:", sd)
