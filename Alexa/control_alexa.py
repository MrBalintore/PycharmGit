import asyncio
from alexapy import AlexaLogin, AlexaAPI

EMAIL = "your-amazon-email@example.com"
EMAIL = "davidjohnjohnston@gmail.com"
PASSWORD = "your-amazon-password"
PASSWORD = "toklas"
URL = "amazon.com"  # or "amazon.co.uk", "amazon.de", etc.
DEVICE_NAME = "Living Room Echo"  # The friendly name of your Alexa device
DEVICE_NAME = "DR's Echo Studio"
async def send_tts():
    login = AlexaLogin(EMAIL, PASSWORD, URL, "your-device-serial")
    await login.login()
    devices = await AlexaAPI.get_devices(login)

    # Find your device
    for device in devices:
        if device['accountName'] == DEVICE_NAME:
            device_serial = device['serialNumber']
            break

    # Send text-to-speech (Alexa will say this)
    await AlexaAPI.send_tts(login, "Hello! This is a test message.", device_serial)

loop = asyncio.get_event_loop()
loop.run_until_complete(send_tts())