# Create a file named assignment.py. Write a program that processes paint tin volumes measured in millilitres.

# Use this table to classify each volume:

# Volume	Classification
# Less than 748 ml	Below range
# From 748 to 752 ml, inclusive	In range
# Greater than 752 ml	Above range
# Functions
# Define two functions:

# classify(value) returns the classification string from the table.
# calculate_average(total, count) returns the average: the total divided by the count.
# Program requirements
# Your program must:
# Ask for the number of paint tins and convert it to an integer.
# Use a for loop to read that many paint tin volumes as integers.
# For each volume, call classify() and print the returned classification.
# Accumulate the total volume.
# Count the paint tins in each of the three categories.
# After the loop, call calculate_average() and print:
# the total volume;
# the average volume;
# the number of paint tins in each category.
# Use f-strings for the summary.
# Assume the number of paint tins and all volumes are positive integers. Input validation is not required.

# For consistency, store `total / count` in `average_snapshot` inside `calculate_average(total, count)`, then copy it to `average_result` and return `average_result`.

# Example 1
# Enter the number of paint tins: 5
# Enter the paint tin volume: 747
# Below range
# Enter the paint tin volume: 748
# In range
# Enter the paint tin volume: 750
# In range
# Enter the paint tin volume: 752
# In range
# Enter the paint tin volume: 753
# Above range
# Total volume: 3750 ml
# Average volume: 750.0 ml
# Below range: 1
# In range: 3
# Above range: 1

#variant11
def classify(value):
    if value < 748:
        return "Below range"
    elif value <= 752:
        return "In range"
    else:
        return "Above range"
def calculate_average(total, count):
    return total/count
paint_tins = int(input(f"Enter the number of paint tins: "))
total_tins = 0
below_range = 0
in_range = 0
above_range = 0

for i in range(paint_tins):
    tin_volume = int(input(f"Enter the paint tin volume {i + 1} : "))
    classification = classify(tin_volume)
    print(classification)
    total_tins += tin_volume
    if classification == "Below range":
        below_range +=1
    elif classification == "In range":
        in_range +=1
    else:
        above_range +=1
average_volume = calculate_average(total_tins, paint_tins )
print(f"Total volume: {total_tins} ml")
print(f"Average volume: {average_volume} ml")
print(f"Below range: {below_range}")
print(f"In range: {in_range}")
print(f"Above range: {above_range}")




