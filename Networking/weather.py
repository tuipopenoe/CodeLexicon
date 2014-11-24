#!python2
# Tui Popenoe
# weather.py - weather fetcher

import urllib2
import json
import Tkinter as Tk
import datetime

class Weather(Tk.Frame):
    def __init__(self, parent):
        Tk.Frame.__init__(self, parent)
        self.parent = parent
        self.init_UI()
        self.search.focus()

    def init_UI(self):
        self.parent.title("Weather App 1.0")

        # Search Elements
        self.search = Tk.Entry(self.parent, justify=Tk.RIGHT)
        self.search_button = Tk.Button(self.parent, text="Search Weather",
                                       command=self. check_weather)

        # Display Elements
        self.coordinates = Tk.Label(self.parent, bg='light blue', width=25)
        self.country = Tk.Label(self.parent, bg='light blue', width=30)
        self.sunrise = Tk.Label(self.parent, bg='light blue', width=25)
        self.sunset = Tk.Label(self.parent, bg='light blue', width=25)
        # 5 day forecast
        # Day 1
        self.weather_one = Tk.Label(self.parent, bg='light blue', width=25)
        self.weather_one_desc = Tk.Label(self.parent, bg='light blue', width=25)
        # Day 2
        self.weather_two = Tk.Label(self.parent, bg='light blue', width=25)
        self.weather_two_desc = Tk.Label(self.parent, bg='light blue', width=25)
        # Day 3
        self.weather_three = Tk.Label(self.parent, bg='light blue', width=25)
        self.weather_three_desc = Tk.Label(self.parent, bg='light blue',
            width=25)
        # Day 4
        self.weather_four = Tk.Label(self.parent, bg='light blue', width=25)
        self.weather_four_desc = Tk.Label(self.parent, bg='light blue',
            width=25)
        # Day 5
        self.weather_five = Tk.Label(self.parent, bg='light blue', width=25)
        self.weather_five_desc = Tk.Label(self.parent, bg='light blue',
            width=25)

        # Temperature and Pressure and Humidity
        self.temperature = Tk.Label(self.parent, bg='light blue', width=25)
        self.pressure = Tk.Label(self.parent, bg='light blue', width=25)
        self.humidity = Tk.Label(self.parent, bg='light blue', width=25)
        self.temp_min = Tk.Label(self.parent, bg='light blue', width=25)
        self.temp_max = Tk.Label(self.parent, bg='light blue', width=25)
        # Wind
        self.wind_speed = Tk.Label(self.parent, bg='light blue', width=25)
        self.wind_angle = Tk.Label(self.parent, bg='light blue', width=25)
        # 
        self.cloud_percent = Tk.Label(self.parent, bg='light blue', width=25)

        # Assign Element Positions
        self.search.grid(row=0, column=3, columnspan=4)
        self.search_button.grid(row=1, column=3, columnspan=2)

        self.coordinates.grid(row=2, column =2, columnspan=1)
        self.country.grid(row=3, column=2, columnspan=1)
        self.sunrise.grid(row=4, column=2, columnspan=1)
        self.sunset.grid(row=5, column=2, columnspan=1)

        self.weather_one.grid(row=2, column=0, columnspan=1)
        self.weather_one_desc.grid(row=2, column=1, columnspan=1)

        self.weather_two.grid(row=3, column=0, columnspan=1)
        self.weather_two_desc.grid(row=3, column=1, columnspan=1)

        self.weather_three.grid(row=4, column=0, columnspan=1)
        self.weather_three_desc.grid(row=4, column=1, columnspan=1)

        self.weather_four.grid(row=5, column=0, columnspan=1)
        self.weather_four_desc.grid(row=5, column=1, columnspan=1)

        self.weather_five.grid(row=6, column=0, columnspan=1)
        self.weather_five_desc.grid(row=6, column=1, columnspan=1)

        self.wind_speed.grid(row=7, column=0, columnspan=1)
        self.wind_angle.grid(row=8, column=0, columnspan=1)

        self.cloud_percent.grid(row=9, column=0, columnspan=1)

        self.temperature.grid(row=6, column=2, columnspan=1)
        self.pressure.grid(row=7, column=2, columnspan=1)
        self.humidity.grid(row=8, column=2, columnspan=1)
        self.temp_min.grid(row=9, column=2, columnspan=1)
        self.temp_max.grid(row=10, column=2, columnspan=1)



    def check_weather(self):
        data = self.get_weather()
        self.coordinates['text'] ='Coordinates: (' +str(data['coord']['lat']) \
            + ', ' + str(data['coord']['lon']) + ')'
        self.country['text'] = 'Country: ' + data['sys']['country']
        self.sunrise['text'] = 'Sunrise: ' + self.get_formatted_time(
            data['sys']['sunrise'])
        self.sunset['text'] = 'Sunset: ' + self.get_formatted_time(
            data['sys']['sunset'])

        if(data['weather'][0]):
            self.weather_one['text'] = 'Today: ' + data['weather'][0]['main']
            self.weather_one_desc['text'] = data['weather'][0]['description']

        if(len(data['weather']) > 1):
            self.weather_two['text'] = 'Tomorrow: ' + data['weather'][1]['main']
            self.weather_two_desc['text'] = data['weather'][1]['description']

        if(len(data['weather']) > 2):
            self.weather_three['text'] = \
                self.get_day(2) + data['weather'][2]['main']
            self.weather_three['text'] = data['weather'][2]['description']

        if(len(data['weather']) > 3):
            self.weather_four['text'] = \
                self.get_day(3) + data['weather'][3]['main']
            self.weather_four['text'] = data['weather'][3]['description']

        if(len(data['weather']) > 4):
            self.weather_five['text'] = \
                self.get_day(4) + data['weather'][4]['main']
            self.weather_five['text'] = data['weather'][4]['description']

        self.temperature['text'] = 'Temperature: ' + str(data['main']['temp'])
        self.pressure['text'] = 'Pressure: ' + str(data['main']['pressure'])
        self.humidity['text'] = 'Humidity: ' + str(data['main']['humidity'])
        self.temp_min['text'] = 'Temperature Minimum: ' + \
            str(data['main']['temp_min'])
        self.temp_max['text'] = 'Temperature Maximum: ' + \
            str(data['main']['temp_max'])
        self.wind_speed['text'] = 'Wind Speed: ' + str(data['wind']['speed'])
        self.wind_angle['text'] = 'Wind Direction: ' + \
            self.calculate_wind_direction(data['wind']['deg'])
        self.cloud_percent['text'] = 'Clouds: ' + str(data['clouds']['all'])

    def calculate_wind_direction(self, angle):
        if angle >= 22.5 and angle < 67.5:
            return 'North East'
        elif angle >= 67.5 and  angle < 112.5:
            return 'East'
        elif angle >= 112.5 and angle < 157.5:
            return 'South East'
        elif angle >= 157.5 and angle < 202.5:
            return 'South'
        elif angle >= 202.5 and angle < 247.5:
            return 'South West'
        elif angle >= 247.5 and angle < 292.5:
            return 'West'
        elif angle >= 292.5 and angle < 337.5:
            return 'North West'
        else:
            return 'North'

    def get_day(self, adjust=0):
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
            'Saturday', 'Sunday']
        return days[(datetime.datetime.today().weekday() + adjust) % 7]

    def get_formatted_time(self, time):
        return datetime.datetime.fromtimestamp(time).strftime('%H:%M:%S')

    def get_weather(self):
        url = 'http://api.openweathermap.org/data/2.5/weather?q=' + \
            self.search.get() + '&mode=json&units=metric'
        print(url)
        u = urllib2.urlopen(url)
        data = u.read()
        print(data)
        return json.loads(data)

def main():
    root = Tk.Tk()
    weather = Weather(root)
    root.configure(background='light blue')
    root.mainloop()

if __name__ == '__main__':
    main()
