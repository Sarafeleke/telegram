import requests
from bs4 import BeautifulSoup
import  time
url = 'http://www.alemcinema.com/'
response = requests.get(url)

con = response.content
# print(content)
soup = BeautifulSoup(con, 'html.parser')
# print(soup.prettify())
# print(soup.td)
titles = soup.find_all("div",attrs={"id":"fh5co-board"})
# print(titles)
for card in titles:
    title_tag2 = card.find("div",attrs={"class":"item"})
    title2 = title_tag2.text.strip("ስለፊልሙ አስተያየቶን ይስጡ") if title_tag2 else "Title not found" 
    image_tag = card.find("img")
    image_url = image_tag["src"] if image_tag and "src" in image_tag.attrs else "Image URL not found"
    url ='https://api.telegram.org/bot6312354572:AAEVL8qY06V7xcMj-EVL6zSoetezuBk4tmY/sendPhoto?chat_id=-1001775234264&photo='+image_url
    base_url='https://api.telegram.org/bot6312354572:AAEVL8qY06V7xcMj-EVL6zSoetezuBk4tmY/sendMessage?chat_id=-1001775234264&text='+title2
    requests.post(url)
    requests.get(base_url)
    print(title2)
    # print(title4)
    # print(title3)
    print(image_url)
    
   

