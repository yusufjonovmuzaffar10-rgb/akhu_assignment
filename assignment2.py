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




