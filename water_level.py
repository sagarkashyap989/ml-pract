import time
import random

CRITICAL_LOW = 20
TANK_FULL = 95

water_level = random.randint(30, 70)
motor_running = False

def check_water_level():
    global water_level, motor_running

    print(f"\nCurrent Water Level: {water_level}%")

    if water_level <= CRITICAL_LOW and not motor_running:
        print("Water level is LOW! Starting motor...")
        motor_running = True
    elif water_level >= TANK_FULL and motor_running:
        print("Tank is FULL! Stopping motor...")
        motor_running = False

    if motor_running:
        water_level += random.randint(5, 10)
    else:
        water_level -= random.randint(1, 3)

    water_level = max(0, min(100, water_level))

    print("Motor Status:", "ON" if motor_running else "OFF")

print("IoT Water Tank Monitoring System Started\n")

try:
    while True:
        check_water_level()
        time.sleep(2)
except KeyboardInterrupt:
    print("\nSystem Stopped.")
