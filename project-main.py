# Imports go at the top
import microbit
import speech
cloud = Image("00000:"
                    "09990:"
                    "99999:"
                    "09990:"
                    "00000:")
snow = Image("90909:"
            "09990:"
            "99999:"
            "09990:"
            "90909:")
sun= Image("90909:"
            "09990:"
            "99099:"
            "09990:"
            "90909:")
sun= Image("90909:"
            "09990:"
            "99099:"
            "09990:"
            "90909:")
thunder = Image("90090:"
                "09009:"
                "00900:"
                "09009:"
                "90090:")
rain = Image("07070:"
            "77777:"
            "07070:"
            "20202"
            "02020:")
mist = Image('33333:44444:33333:44444:33333:')
weather_icons = {
    'cloudy': cloud,
    'snow': snow,
    'sun': sun,
    'thunderstorm': thunder,
    'rain': rain,
    'mist': mist,
    'sprinkling': mist  # Assuming mist for sprinkling
}
# Code in a 'while True:' loop repeats forever
while True:
    display.show(weather_icons[weather_condition])
    sleep(1000)
    speech.say(f"The weather today is {weather_condition}")
    display.scroll(weather_condition.capitalize())
    sleep(5000)  # Wait before checking the next condition
    
   
