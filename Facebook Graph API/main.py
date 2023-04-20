import requests
import json


#extracted a photo from facebook account
url = "https://graph.facebook.com/v16.0/1886382211557451?fields=link%2Cimages&access_token=EACAyCY5vsToBAD7IrBHWtNH8G7pxCQBjA2b6tP3YP9GWdKEZByClkP7gfH7nQMpCcVZCJGnzhVM1cZBwTpjbh" \
      "yKdCMcfnKWQi0bm1MR99O76y8OIywC3m1zCQgreZBzj0K1wSvU1Ggg4Jqa7rIEFMnkrRd3hpjeobVWEHZBCY94mqzz12m2DQsNb14zRHJK44lyvx8YFbQYZAe8Bvt9ZCLd4XmJ2LZANPdc4siwA0BhnhzqZCWbQnOA5O"



response = requests.get(url)


data = response.text

data = json.loads(data)
image_url = (data['images'][0]['source'])

image_bytes = requests.get(image_url).content


with open('image.jpg', 'wb') as file:
    file.write(image_bytes)