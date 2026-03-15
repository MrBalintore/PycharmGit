import numpy as np
import matplotlib.pyplot as plt

# Months and approximate day lengths (hours) for the 15th of each month
months = ["Dec", "Jan", "Feb", "Mar", "Apr", "May", "Jun"]
day_lengths = [6.9, 7.5, 9.5, 12.0, 14.4, 16.5, 17.7]

# Approximate solar noon (Kirriemuir ~12:15 local time)
solar_noon = 12.25

# Time axis across the day
t = np.linspace(0, 24, 1000)

plt.figure(figsize=(10,6))

for month, dl in zip(months, day_lengths):
    sunrise = solar_noon - dl/2
    sunset = solar_noon + dl/2

    intensity = np.zeros_like(t)
    mask = (t >= sunrise) & (t <= sunset)

    # Smooth daylight curve
    intensity[mask] = np.sin(np.pi * (t[mask] - sunrise) / dl)

    plt.plot(t, intensity, label=month)

plt.xlabel("Time of day (hours)")
plt.ylabel("Relative daylight intensity")
plt.title("Daylight Intensity Curves – Kirriemuir (15th of month, Dec–Jun)")
plt.xlim(0, 24)
plt.ylim(0, 1.05)

plt.legend()
plt.grid(True)

plt.show()