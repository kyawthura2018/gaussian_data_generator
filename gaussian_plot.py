import numpy as np
import matplotlib.pyplot as plt

# Data parameters with adjusted peaks
x = np.arange(0, 30.1, 0.1)
params = {
    "Point1": {"a": 40, "mu": 5.857, "sigma": 0.2},
    "Point2": {"a": 45, "mu": 13.967, "sigma": 0.2},
    "Point3": {"a": 65, "mu": 18.405, "sigma": 0.2}
}

# Calculate individual peaks
peaks = {}
combined = np.zeros_like(x)
for name, p in params.items():
    gaussian = p["a"] * np.exp(-(x - p["mu"])**2 / (2 * p["sigma"]**2))
    peaks[name] = gaussian
    combined += gaussian

# Plot settings
plt.figure(figsize=(12, 4))
plt.plot(x, combined, 'k-', linewidth=1)

# Add peak labels
for p in params.items():
    plt.text(p[1]['mu'], p[1]['a']+2, f"{p[1]['mu']}", ha='center', color='cyan')

# Axis settings
plt.ylim(-25, 110)
plt.xlim(0, 30)
plt.grid(True, alpha=0.3)
plt.ylabel('')
plt.xlabel('')

plt.show()