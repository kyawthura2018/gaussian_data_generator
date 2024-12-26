import pandas as pd
import numpy as np

# Generate x values
x = np.arange(0, 45.1, 0.1)

# Parameters for peaks
params = {
    "Peak1": {"a": 0.556, "mu": 6.050, "sigma": 0.2},
    "Peak2": {"a": 19.767, "mu": 14.305, "sigma": 0.2},
    "Peak3": {"a": 3.913, "mu": 18.197, "sigma": 0.2},
    "Peak4": {"a": 12.272, "mu": 18.602, "sigma": 0.2},
    "Peak5": {"a": 2.418, "mu": 18.948, "sigma": 0.2},


}

# Calculate peaks
data = {'Time': x}
for name, p in params.items():
    data[name] = p["a"] * np.exp(-(x - p["mu"])**2 / (2 * p["sigma"]**2))

# Create total intensity column
data['Total'] = sum(data[peak] for peak in params.keys())

# Create DataFrame and export
df = pd.DataFrame(data)
df.to_excel('Flavonoid.KU50-2.xlsx', index=False)