api = "cf0940f5649d0e7718e82197e447f9ec"
import requests


def get_weather(city, api_key = api, units = "metric"):
    url = (f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api}&units={units}")
    r = requests.get(url=url)
    content = r.json()
    print(content)


    list = content['list']

    name = (content['city']['name'])


    for dict in list:
        datetime = dict['dt_txt']
        temp = dict['main']['temp']
        condition =dict['weather'][0]['description']

        with open("data.txt", 'a') as file:
            file.write(str(name) + ', ')
            file.write(str(datetime) + ', ')
            file.write(str(temp) + ', ')
            file.write(str(condition) + ', ')
            file.write("\n")



get_weather(city='Karachi')

