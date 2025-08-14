from machine import Pin
import network
import urequests
import time

# --- WiFi config ---
SSID = "Redmi 12"
PASSWORD = ""

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)

while not wifi.isconnected():
    time.sleep(0.5)

print("Connected! IP:", wifi.ifconfig()[0])

# --- Button Setup ---
button = Pin(12, Pin.IN, Pin.PULL_UP)  # D2, pull-up resistor
api_url = "http://192.168.51.207:5000/add_point"

# Track last state for edge detection
last_state = button.value()

while True:
    current_state = button.value()
    
    # Detect falling edge: HIGH -> LOW
    if last_state == 1 and current_state == 0:
        try:
            response = urequests.post(api_url)
            print("Point added!", response.json())
        except Exception as e:
            print("Failed to connect to API:", e)
        time.sleep(0)  # simple debounce

    last_state = current_state
    time.sleep(0)
