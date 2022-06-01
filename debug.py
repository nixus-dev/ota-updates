import time, machine, network, senko, credentials

GITHUB_URL = "https://github.com/nixus-dev/ota-updates/blob/main/"
OTA = senko.Senko(url=GITHUB_URL, files=["boot.py", "main.py"])

WIFI_SSID = credentials.WIFI_SSID
WIFI_PASSWORD = credentials.WIFI_PASSWORD

def connectToNetwork(ssid, password):
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

def myFunction():
    counter = 0
    led = Pin(1, Pin.OUT)
    while counter <= 5:
        led.value(not led.value())
        sleep(3)

def OTAupdate():
    if OTA.update():
        print("Updated to the latest version! Rebooting...")
        machine.reset()

connectToNetwork(WIFI_SSID, WIFI_PASSWORD)
myFunction()
OTAupdate()
