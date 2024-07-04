import pyowm
from bluezero import microbit

# OpenWeatherMap API key
KEY = '7fe781e473b58cb1f0f08e4e10f48183'

# Location for weather data
location = 'Hamilton,NZ'

# Initialize the OpenWeatherMap object
owm = pyowm.OWM(KEY)
mgr = owm.weather_manager()

# Get the current weather
observation = mgr.weather_at_place(location)
weather = observation.weather

# Format the weather message
weather_message = f'Weather: {weather.detailed_status}, Temp: {weather.temperature("celsius")["temp"]:.1f}C'

# Replace with the Bluetooth address of your micro:bit
microbit_address = 'XX:XX:XX:XX:XX:XX'

# Create a micro:bit object
ubit = microbit.Microbit(microbit_address)

# Connect to the micro:bit
ubit.connect()

# Send weather data to the micro:bit
ubit.uart.write(weather_message)

# Disconnect from the micro:bit
ubit.disconnect()
