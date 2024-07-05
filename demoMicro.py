from microbit import *

# Define the weather icons
sun = Image('00000:'
            '00900:'
            '09990:'
            '00900:'
            '00000:')
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
mist = Image('22222:'
             '33333:'
             '22222:'
             '33333:'
             '22222:')

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