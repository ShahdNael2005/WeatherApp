from microbit import *
import speech
# Define the weather icons
sun = Image("90909:"
            "09990:"
            "99099:"
            "09990:"
            "90909:")
few = Image('04040:'
            '44444:'
            '04040:'
            '00000:'
            '00000:')
cloud = Image('06060:'
              '66666:'
              '06060:'
              '00000:'
              '00000:')
broken = Image('09090:'
               '99999:'
               '09090:'
               '00000:'
               '00000:')
shower = Image('09090:'
               '99999:'
               '09090:'
               '30303:'
               '03030:')
rain = Image('07070:'
             '77777:'
             '07070:'
             '20202:'
             '02020:')
thunder = Image('90090:'
                '09009:'
                '00900:'
                '09009:'
                '90090:')
snow = Image('70707:'
             '07070:'
             '70707:'
             '07070:'
             '70707:')
mist = Image('33333:44444:33333:44444:33333:')

# Mapping of weather descriptions to icons
weather_icons = {
    b'clear sky': sun,
    b'few clouds': few,
    b'scattered clouds': cloud,
    b'broken clouds': broken,
    b'shower rain': shower,
    b'rain': rain,
    b'thunderstorm': thunder,
    b'snow': snow,
    b'mist': mist
}
weather_sounds = {
    b'clear sky': 'Hello, the weather is clear.',
    b'few clouds': 'There are a few clouds.',
    b'scattered clouds': 'The sky is scattered with clouds.',
    b'broken clouds': 'There are broken clouds.',
    b'shower rain': 'It is showering rain.',
    b'rain': 'It is raining.',
    b'thunderstorm': 'There is a thunderstorm.',
    b'snow': 'It is snowing.',
    b'mist': 'It is misty.'
}
while True:
    if True:
        display.show(mist)
        #uart.write(b"teststring")
        if uart.any():
            bytestring = uart.readline()
            #uart.write("1")
            bytestring = bytestring[9:]
            bytestring = bytestring[0:bytestring.find(b',')]
            uart.write(bytestring)
            
            display.show(weather_icons.get(bytestring, mist))

            sound = weather_sounds.get(bytestring, 'The weather condition is unknown.')
            speech.say(sound)
        #if bytestring:
        sleep(1000)
       
        
        #weather_data = str(bytestring)
        #print(weather_data)  # For debugging purposes
        
        # Extract weather description from the message
        #weather_description = weather_data.split(',')[0].split(':')[1].strip()
        
        # Get the corresponding weather icon
        #icon = weather_icons.get(weather_description, mist)  # Default to mist if not found
        #display.show(icon)
    
    sleep(1000)