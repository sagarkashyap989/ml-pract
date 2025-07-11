import time
import threading
from queue import Queue

# Simulated UART line as a queue (FIFO)
uart_buffer = Queue()

def device_a_transmitter():
    messages = ["Hello", "Temperature:25C", "Motion Detected", "End"]
    for msg in messages:
        print(f"Device A: Sending → {msg}")
        uart_buffer.put(msg)
        time.sleep(2)

def device_b_receiver():
    while True:
        if not uart_buffer.empty():
            msg = uart_buffer.get()
            print(f"Device B: Received ← {msg}")
            if msg == "End":
                print("Device B: Communication complete.")
                break
        time.sleep(1)

def main():
    print("UART Communication Simulation\n")
    tx_thread = threading.Thread(target=device_a_transmitter)
    rx_thread = threading.Thread(target=device_b_receiver)

    tx_thread.start()
    rx_thread.start()

    tx_thread.join()
    rx_thread.join()

    print("\nSimulation Ended.")

if __name__ == "__main__":
    main()
