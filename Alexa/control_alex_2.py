import os
import asyncio
from alexapy import AlexaLogin, AlexaAPI

# Store your credentials in environment variables instead of hardcoding
EMAIL = os.getenv("ALEXA_EMAIL")
EMAIL = "davidjohnjohnston@gmial.com"
PASSWORD = os.getenv("ALEXA_PASSWORD")
PASSWORD="toklas"
URL = "amazon.com"  # change if your account is on amazon.co.uk, amazon.de, etc.
URL = "amazon.co.uk"
DEVICE_NAME = "Dr's Echo Studio"


def of(input:str):
    output = r"""C:\Users\david\PycharmProjects\PycharmGit\Alexa"""
    return output

async def main():
    # Login to Alexa
    login = AlexaLogin(EMAIL, PASSWORD, URL, of)
    await login.login()

    # Get all devices
    devices = await AlexaAPI.get_devices(login)

    # Find your target Echo
    target = next(
        (device for device in devices if device['accountName'] == DEVICE_NAME),
        None
    )

    if target:
        # Send TTS message
        await AlexaAPI.send_tts(login, target, "Hello World")
        print(f"✅ Sent 'Hello World' to {DEVICE_NAME}")
    else:
        print(f"❌ Device '{DEVICE_NAME}' not found")

asyncio.run(main())