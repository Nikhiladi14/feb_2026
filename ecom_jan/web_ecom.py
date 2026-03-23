import requests
import pandas as pd 
from bs4 import BeautifulSoup

response = requests.get("https://sportscorner.qa/en/mens/footwear.html?brand=5662")

print(response)

soup = BeautifulSoup(response.content,'html.parser')
# # print(soup)

names = soup.find_all('a',class_ ="product-item-link")
# # print(names)
name = []
for i in names[0:10]:
    name.append(i.get_text(strip=True))
# # print(name)

prices = soup.find_all('span',class_ = "price")
# print(prices)
price = []

for i in prices[0:10]:
    d = i.get_text().replace('QR','').strip()
    price.append(d)
# print(price)

images = soup.find_all('img', class_="product-image-photo")
# print(images)
image = []

for i in images[0:10]:
    d = i['src']
    image.append(d)
# print(image)

df = pd.DataFrame()
# print(df)
df['Names'] = name
df['prices'] = price
df['images'] = image
print(df)

df.to_csv("shoesmar.csv")