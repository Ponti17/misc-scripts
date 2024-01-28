import itertools
import numpy as np

# Initialize a list to store the resistance values
resistances = []

# Loop through the number of resistors and ask the user for the resistance values
for i in range(0, 1000):
    resistance = input(f"Enter the resistance value for resistor {i+1}: ")
    if resistance.isdigit():
        resistances.append(float(resistance))
    else:
        break

# Calculate the equivalent resistance
if len(resistances) == 0:
    equivalent_resistance = 0
else:
    total_resistance = sum([1/r for r in resistances])
    equivalent_resistance = 1/total_resistance

# Print the equivalent resistance
print(f"The equivalent resistance is {equivalent_resistance:.2f} ohms.")

parallel_combinations = []
for i in range(1, len(resistances)+1):
    for combination in itertools.combinations(resistances, i):
        parallel_combinations.append(combination)

# Print all possible parallel combinations of entered resistances
parallel_resistances = []
print("All possible parallel combinations of entered resistances:")
for combination in parallel_combinations:
    parallel_resistances.append(1/sum([1/r for r in combination]))
arg_sorted_resistances = np.argsort(parallel_resistances)
for i in arg_sorted_resistances:
    print(np.round(parallel_resistances[i], 1), parallel_combinations[i], sep=": ")
