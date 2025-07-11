import requests
import time

def check_rain(city="Palghar"):
    print(f"Checking weather for: {city}")
    try:
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url)
        data = response.json()
        
        condition = data["current_condition"][0]["weatherDesc"][0]["value"]
        print("Current condition:", condition)
        
        if "rain" in condition.lower():
            print("Rain expected! Triggering alarm")
            try:
                import winsound
                winsound.Beep(1000, 800)
            except:
                print("Beep triggered (manual fallback)")
        else:
            print("No rain expected.")
    except Exception as e:
        print("Error:", e)

print("Rain Alert System Started")
check_rain("Palghar")
