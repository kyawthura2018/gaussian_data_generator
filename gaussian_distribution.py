# Re-import necessary libraries after reset
import pandas as pd
import numpy as np

# Create a dataframe for Excel setup
data = {
    "x": [round(i, 1) for i in np.arange(0, 25.1, 0.1)],  # Retention time (x values)
}

# Define parameters for Point1, Point2, and Point3
parameters = {
    "Point1": {"a": 426149, "mu": 5.857, "sigma": 1.5},
    "Point2": {"a": 446130, "mu": 13.987, "sigma": 1.5},
    "Point3": {"a": 649939, "mu": 18.405, "sigma": 1.5},
}

# Calculate Gaussian values for each compound
for compound, params in parameters.items():
    data[compound] = [
        params["a"] * np.exp(-((x - params["mu"])**2) / (2 * params["sigma"]**2))
        for x in data["x"]
    ]

# Create a dataframe
df = pd.DataFrame(data)

# Add parameter metadata for the first few rows (for user reference)
param_info = {
    "Parameter": ["Amplitude (a)", "Mean (μ)", "Std Dev (σ)"],
    "Point1": [parameters["Point1"]["a"], parameters["Point1"]["mu"], parameters["Point1"]["sigma"]],
    "Point2": [parameters["Point2"]["a"], parameters["Point2"]["mu"], parameters["Point2"]["sigma"]],
    "Point3": [parameters["Point3"]["a"], parameters["Point3"]["mu"], parameters["Point3"]["sigma"]],
}

# Save to Excel
output_path = "./Gaussian_Distribution_Flavonoids.xlsx"
with pd.ExcelWriter(output_path, engine="xlsxwriter") as writer:
    pd.DataFrame(param_info).to_excel(writer, sheet_name="Parameters", index=False)
    df.to_excel(writer, sheet_name="Gaussian Data", index=False)

output_path
