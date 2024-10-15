import requests
import smtplib
import time
from datetime import datetime


MY_LAT = 20.717542
MY_LNG = 77.022079

MY_EMAIL = "youremail@gmail.com"  # Your Gmail address
MY_PASSWORD = "app-specific-password"  # Your app-specific Gmail password


def is_iss_overhead():
    reponse = requests.get('http://api.open-notify.org/iss-now.json')
    reponse.raise_for_status()

    # ISS latitude and longitue
    iss_latitude = float(reponse.json()['iss_position']['latitude'])
    iss_longitude = float(reponse.json()['iss_position']['longitude'])
    # print(iss_latitude)
    # print(iss_longitude)

    # Chech weather the iss is near me 
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG - 5 <= iss_longitude <= MY_LNG +5:
        return True



def is_night():
    # created a parameter for my location 
    parameters ={
        'lat':MY_LAT,
        'lng':MY_LNG,
        'formatted': 0
    }

    # API call request to server sunrise and sunset which requiered parameter 
    sunset_reponse = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    sunset_reponse.raise_for_status()
    sunrise = int(sunset_reponse.json()['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(sunset_reponse.json()['results']['sunset'].split("T")[1].split(":")[0])
 
    # print(sunrise)
    # print(sunset)

    # getting the current time hour
    current_time = datetime.now().hour
    if current_time >= sunset or current_time <= sunrise:
        return True
    

# Run the code in a loop sleep time 60 sec
while True:
    time.sleep(60)
    # If ISS is close to my current position and it is currently dark 
    if is_iss_overhead() and is_night():
        try:
            # Then send and email to myself saying ISS is above you 
            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(MY_EMAIL,MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=MY_EMAIL,
                    msg="Subject:Look Up\n\nThe ISS is above you in the sky"
                )
        except Exception as e:
            print(f"Error sending email: {e}")
