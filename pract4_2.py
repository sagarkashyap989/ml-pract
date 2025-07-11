import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
TOPIC = "iotgame/guess"
RESP_TOPIC = "iotgame/response"

def on_connect(client, userdata, flags, rc):
    print("Connected to broker.")
    client.subscribe(RESP_TOPIC)

def on_message(client, userdata, msg):
    response = msg.payload.decode()
    print(f"Feedback: {response}")
    if "Correct" in response:
        exit()

def send_guess(client):
    while True:
        try:
            guess = int(input("Enter your guess (0-100): "))
            client.publish(TOPIC, str(guess))
        except ValueError:
            print("Invalid input.")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, 1883, 60)
client.loop_start()

send_guess(client)
