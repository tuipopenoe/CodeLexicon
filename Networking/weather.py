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
        self.temp_max = Tk.Label(self.parent)
        # Wind
        self.wind_speed = Tk.Label(self.parent)
        self.wind_angle = Tk.Label(self.parent)
        # 
        self.cloud_percent = Tk.Label(self.parent)

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
        self.coordinates['text'] = str(data['coord'])
        self.country['text'] = data['sys']['country']
        self.sunrise['text'] = data['sys']['sunrise']
        self.sunset['text'] = data['sys']['sunset']

        self.weather_one['text'] = data['weather'][0]['main']
        self.weather_one_desc['text'] = data['weather'][0]['description']

        self.weather_two['text'] = data['weather'][1]['main']
        self.weather_two_desc['text'] = data['weather'][1]['description']

        self.weather_three['text'] = data['weather'][2]['main']
        self.weather_three['text'] = data['weather'][2]['description']

        self.weather_four['text'] = data['weather'][3]['main']
        self.weather_four['text'] = data['weather'][3]['description']

        self.weather_five['text'] = data['weather'][4]['main']
        self.weather_five['text'] = data['weather'][4]['description']

        self.temperature['text'] = data['main']['temp']
        self.pressure['text'] = data['main']['pressure']
        self.humidity['text'] = data['main']['humidity']
        self.temp_min['text'] = data['main']['temp_min']
        self.temp_max['text'] = data['main']['temp_max']
        self.wind_speed['text'] = data['wind']['speed']
        self.wind_angle['text'] = calculate_wind_direction(data['wind']['deg'])
        self.cloud_percent['text'] = data['clouds']['all']

        self.display.insert(Tk.INSERT, str(data))

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
