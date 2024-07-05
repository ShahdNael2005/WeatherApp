import pyowm
#from bluezero import microbit # type: ignore
import serial

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
weather_message = f'Weather: {weather.detailed_status}, Temp: {weather.temperature("celsius")["temp"]:.1f}C\n'

# Replace with the Bluetooth address of your micro:bit
microbit_address = '40:00:02:48:8c:20'

# Create a micro:bit object
#ubit = microbit.Microbit(microbit_address)

# Connect to the micro:bit
#ubit.connect()

# Send weather data to the micro:bit
#ubit.uart.write(weather_message)

# Disconnect from the micro:bit
#ubit.disconnect()

with serial.Serial('COM6', 115200, timeout=10) as ser:
    ser.write(weather_message.encode('ascii'))
    print(ser.read(100))