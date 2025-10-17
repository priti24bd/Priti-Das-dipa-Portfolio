# File: mangrove_tracker.py
# Project: Mangrove Innovators
# Author: Preeti Dasdeepa

"""
Track mangrove planting progress and CO2 absorption data.
This could later connect to a simple web dashboard.
"""

import csv
from datetime import datetime

# Sample data (you can update manually)
data = [
    ["2025-02-15", "Gopalganj", 100, 30.5],
    ["2025-03-01", "Bagerhat", 150, 48.2],
    ["2025-04-10", "Khulna", 200, 66.1]
]

# Save to CSV
with open("mangrove_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Date", "Location", "Trees_Planted", "CO2_Absorbed_kg"])
    writer.writerows(data)

print("🌿 Mangrove planting data saved to mangrove_data.csv")

# Example analysis
total_trees = sum(row[2] for row in data)
total_co2 = sum(row[3] for row in data)
print(f"Total trees planted: {total_trees}")
print(f"Total CO2 absorbed: {total_co2} kg")
