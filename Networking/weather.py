#!python2
# Tui Popenoe
# weather.py - weather fetcher

import urllib2
import json
import Tkinter as Tk

class Weather(Tk.Frame):
    def __init__(self, parent):
        Tk.Frame.__init__(self, parent)
        self.parent = parent
        self.init_UI()
 
    def init_UI(self):
        self.parent.title("Weather App 1.0")

        # Search Elements
        self.search = Tk.Entry(self.parent, justify=Tk.RIGHT)
        self.search_button = Tk.Button(self.parent, text="Search Weather",
                                       command=self. check_weather)

        # Display Elements
        self.display = Tk.Text(self.parent)
        self.coordinates = Tk.Label(self.parent)
        self.country = Tk.Label(self.parent)
        self.sunrise = Tk.Label(self.parent)
        self.sunset = Tk.Label(self.parent)
        # 5 day forecast
        # Day 1
        self.weather_one = Tk.Label(self.parent)
        self.weather_one_desc = Tk.Label(self.parent)
        # Day 2
        self.weather_two = Tk.Label(self.parent)
        self.weather_two_desc = Tk.Label(self.parent)
        # Day 3
        self.weather_three = Tk.Label(self.parent)
        self.weather_three_desc = Tk.Label(self.parent)
        # Day 4
        self.weather_four = Tk.Label(self.parent)
        self.weather_four_desc = Tk.Label(self.parent)
        # Day 5
        self.weather_five = Tk.Label(self.parent)
        self.weather_five_desc = Tk.Label(self.parent)

        # Temperature and Pressure and Humidity
        self.temperature = Tk.Label(self.parent)
        self.pressure = Tk.Label(self.parent)
        self.humidity = Tk.Label(self.parent)
        self.temp_min = Tk.Label(self.parent)
        self.ftemp_max = Tk.Label(self.parent)
        # Wind
        self.wind_speed = Tk.Label(self.parent)
        self.wind_angle = Tk.Label(self.parent)
        # 
        self.cloud_percent = Tk.Label(self.parent)

        # Assign Element Positions
        self.search.grid(row=0, column=0, columnspan=4)
        self.search_button.grid(row=1, column=3, columnspan=2)
        self.display.grid(row=2, column=0, columnspan=4, rowspan=4)

    def check_weather(self):
        weather_json = self.get_weather()
        clouds = weather_json['clouds']

        self.display.insert(Tk.INSERT, str(weather_json))

    def calculate_wind_direction(self):
        

    def get_weather(self):
        url = 'http://api.openweathermap.org/data/2.5/weather?q=' + \
            self.search.get()
        print(url)
        u = urllib2.urlopen(url)
        data = u.read()
        print(data)
        return json.loads(data)

def main():
    root = Tk.Tk()
    weather = Weather(root)
    root.mainloop()

if __name__ == '__main__':
    main()
