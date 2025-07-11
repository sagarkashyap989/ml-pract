import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
TOPIC = "iotgame/guess"
RESP_TOPIC = "iotgame/response"
SECRET_NUMBER = 42  # Player 1's number

def on_connect(client, userdata, flags, rc):
    print("Connected to broker.")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    guess = int(msg.payload.decode())
    print(f"Player 2 guessed: {guess}")
    if guess < SECRET_NUMBER:
        client.publish(RESP_TOPIC, "Too low")
    elif guess > SECRET_NUMBER:
        client.publish(RESP_TOPIC, "Too high")
    else:
        client.publish(RESP_TOPIC, "Correct! You won")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, 1883, 60)
client.loop_forever()
