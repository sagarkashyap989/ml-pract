import time
import random
from datetime import datetime

def read_light_sensor():
    return round(random.uniform(100, 1000), 2)

def send_to_console(event_id, data):
    print(f"Event #{event_id}")
    print(f"Timestamp          : {data['timestamp']}")
    print(f"Light Intensity    : {data['light_intensity_lux']} lux")
    print("-" * 40)

def main():
    print("=== IoT Light Sensor Module Started ===\n")
    event_count = 1

    try:
        while True:
            lux = read_light_sensor()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data = {
                "timestamp": timestamp,
                "light_intensity_lux": lux
            }
            send_to_console(event_count, data)
            event_count += 1
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nModule stopped by user.")

if __name__ == "__main__":
    main()
import time
import random
from datetime import datetime

def read_light_sensor():
    return round(random.uniform(100, 1000), 2)

def send_to_console(event_id, data):
    print(f"Event #{event_id}")
    print(f"Timestamp          : {data['timestamp']}")
    print(f"Light Intensity    : {data['light_intensity_lux']} lux")
    print("-" * 40)

def main():
    print("=== IoT Light Sensor Module Started ===\n")
    event_count = 1

    try:
        while True:
            lux = read_light_sensor()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data = {
                "timestamp": timestamp,
                "light_intensity_lux": lux
            }
            send_to_console(event_count, data)
            event_count += 1
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nModule stopped by user.")

if __name__ == "__main__":
    main()
