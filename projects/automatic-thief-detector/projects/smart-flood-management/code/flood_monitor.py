# File: flood_monitor.py
# Project: Smart Flood Management System
# Author: Preeti Dasdeepa

"""
Simulates water level monitoring using IoT sensors.
If the water level exceeds threshold, the system sends an alert.
"""

import random
import time

THRESHOLD = 75  # cm
print("Starting flood monitoring simulation...")

while True:
    # Random sensor data (simulate)
    water_level = random.randint(40, 100)
    print(f"Current water level: {water_level} cm")

    if water_level > THRESHOLD:
        print("🚨 ALERT: Flood risk detected! Sending drone signal...")
        # In real implementation: send signal to drone via IoT module

    time.sleep(2)
