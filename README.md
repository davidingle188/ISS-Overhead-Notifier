


# ISS Overhead Notifier

This Python script sends an email notification whenever the International Space Station (ISS) is overhead and it's nighttime at your location. It uses the ISS location API and the Sunrise-Sunset API to track the ISS position and determine whether it's dark outside. If both conditions are met, the script sends an email alert.

## Features

- Tracks the position of the ISS in real-time using the Open Notify API.
- Uses the Sunrise-Sunset API to determine if it’s nighttime at your location.
- Sends an email notification when the ISS is overhead during the night.
- Runs continuously, checking every 60 seconds.

## Requirements

- Python 3.x
- Libraries: `requests`, `smtplib`
- A Gmail account (you will need to use an **app-specific password** for Gmail if two-factor authentication is enabled).

## Setup

### 1. Install the necessary libraries

This project requires the `requests` library to make API calls. Install it using pip:

```bash
pip install requests
```

### 2. Configure your details

In the Python script, replace the following placeholders with your actual details:

```python
MY_LAT = 20.717542  # Your latitude
MY_LNG = 77.022079  # Your longitude

MY_EMAIL = "youremail@gmail.com"  # Your Gmail address
MY_PASSWORD = "app-specific-password"  # Your app-specific Gmail password
```

- **Latitude and Longitude:** Enter your location's latitude and longitude. You can find your coordinates using Google Maps.
- **Email:** Your Gmail address for sending the notification.
- **App-Specific Password:** If you have two-factor authentication enabled, you’ll need to create an app-specific password in your Google Account Security settings.

### 3. Running the Script

Once you have everything configured, run the script:

```bash
python iss_notifier.py
```

The script will continuously check every 60 seconds to see if the ISS is overhead and if it's nighttime. If both conditions are met, it will send you an email notifying you to look up and spot the ISS.

## How It Works

1. **Tracking the ISS:** The script fetches the current location of the ISS from the Open Notify API.
   - API Endpoint: [http://api.open-notify.org/iss-now.json](http://api.open-notify.org/iss-now.json)
   - It compares the ISS's latitude and longitude with your location to determine if the ISS is nearby (within 5 degrees).

2. **Checking Day/Night Status:** The script uses the Sunrise-Sunset API to determine whether it's currently nighttime at your location.
   - API Endpoint: [https://api.sunrise-sunset.org/json](https://api.sunrise-sunset.org/json)
   - It calculates whether the current time is before sunrise or after sunset at your location.

3. **Sending an Email:** If both conditions (ISS overhead and nighttime) are met, the script sends an email to the specified Gmail account using SMTP.

## API Documentation

- **Open Notify API (ISS Location):** This API provides real-time data on the location of the ISS.
  - API URL: [http://api.open-notify.org/iss-now.json](http://api.open-notify.org/iss-now.json)
  
- **Sunrise-Sunset API:** This API returns the sunrise and sunset times for a given location.
  - API URL: [https://api.sunrise-sunset.org/json](https://api.sunrise-sunset.org/json)

## Potential Improvements

- Add support for other email providers (currently supports Gmail only).
- Add a GUI to make the configuration more user-friendly.
- Customize the notification frequency or add more detailed email notifications.

## License

This project is licensed under the MIT License. You are free to use and modify the code as you see fit. Feel free to contribute and make improvements!

### How to Use the `README.md`

1. Copy the text above into a file named `README.md`.
2. Place the `README.md` file in the same directory as your Python script.
3. When you upload the project to GitHub or share it, others will have clear instructions on how to set it up and use it.

Let me know if you need further modifications!
```

You can copy and use this entire Markdown text as needed!
