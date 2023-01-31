from tkinter import *
import requests
import json

root = Tk()
root.title("Learn to Code!")
root.geometry('600x50')

# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=00F3BB3A-6636-4A32-8C76-C5E2D1F506F6 


#try:
api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=00F3BB3A-6636-4A32-8C76-C5E2D1F506F6")
api = json.loads(api_request.content)
city = api[0]['ReportingArea']
quality = api[0]['AQI']
category = api[0]['Category']['Name']

if category == "Good":
    weather_colour = "#0C0"
elif category == "Moderate":
    weather_colour = "FFFF00"
elif category == "Unhealthy for Sensitive Groups":
    weather_colour = "ff9900"
elif category == "Unhealthy":
    weather_colour = "FF0000"
elif category == "Very Unhealthy":
    weather_colour = "#990066"
elif category == "Hazardous":
    weather_colour = "#660000"

root.configure(background=weather_colour)

my_label = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 20), background=weather_colour)
my_label.pack()

#except Exception as e:
#    api = "Error ..."


root.mainloop()