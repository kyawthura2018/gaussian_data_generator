# Import numpy
import numpy as np

# Given values
CONTROL = 6.33
IE = 37.24

# Calculate WL using the IE equation
WL = round(CONTROL * (1 - (IE / 100)), 2)

# Define range for initialWeight and finalWeight
lower_bound = 14883.76
upper_bound = 16794.21

# Generate example combinations where initialWeight - finalWeight = WL
combinations = []
for initialWeight in np.linspace(lower_bound, upper_bound, 10):  # Generate 10 evenly spaced values for initialWeight
    finalWeight = round(initialWeight,2) - WL
    if lower_bound <= finalWeight <= upper_bound:
        combinations.append((round(initialWeight,2), finalWeight))

# Print WL and combinations
print("WL:", round(WL, 2))
print("Combinations of initialWeight and finalWeight:")
for initialWeight, finalWeight in combinations:
    print(f"initialWeight: {initialWeight}, finalWeight: {finalWeight}")
