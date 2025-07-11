import time
import random
from datetime import datetime

registered_users = {
    "user_123": {
        "name": "Ayushi Upadhyay",
        "email": "ayushi@gmail.com",
        "mobile": "9876543210"
    }
}

def is_user_near_bus(user_id):
    return random.choice([True, True, True, True, False])

def generate_ticket(user_id):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ticket_id = f"TICKET-{random.randint(1000, 9999)}"
    ticket = {
        "ticket_id": ticket_id,
        "issued_to": registered_users[user_id]["name"],
        "issued_time": now,
        "bus_route": "Route A - City Center",
        "valid_for": "Single Ride"
    }
    return ticket

def send_ticket(ticket, user_id):
    user = registered_users[user_id]
    print(f"\nTicket sent to {user['name']} at {user['email']} / {user['mobile']}")
    print("Ticket Details:")
    for k, v in ticket.items():
        print(f"  {k}: {v}")

def iot_ticketing_system(user_id):
    print(f"Checking for user {user_id} near bus stop...")
    if is_user_near_bus(user_id):
        print("User detected near the bus.")
        ticket = generate_ticket(user_id)
        send_ticket(ticket, user_id)
    else:
        print("User not detected near the bus. Try again later.")

if __name__ == "__main__":
    user_id = "user_123"
    while True:
        iot_ticketing_system(user_id)
        time.sleep(5)
