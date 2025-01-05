# Weather-app
Weather Voice Assistant
This project is a Python script that retrieves the current temperature of a city using the WeatherAPI and speaks the result aloud using text-to-speech functionality.

Features:
Retrieves the current temperature of a specified city from the WeatherAPI.
Converts the temperature information into speech using the SAPI.SpVoice engine.
Displays the temperature message both on the console and audibly.

Requirements:
Python 3.x
requests library (pip install requests)
win32com.client library for text-to-speech functionality (pip install pywin32)

How to Use:
Run the script and input the name of the city for which you want to know the temperature.
The script will retrieve the temperature and speak the result.
The temperature message will also be printed on the console.

Example:
Input: "London"
Output:
Console: "The current weather in London is 15 degrees Celsius."
Audio: "The current weather in London is 15 degrees Celsius."
This project is ideal for building interactive voice-based applications and experimenting with weather APIs and text-to-speech in Python.
