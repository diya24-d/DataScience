import requests
from bs4 import BeautifulSoup
import pandas as pd


PhoneName = []
PhoneRating = []
PhoneSpecs = []
Price = []

url = "https://www.flipkart.com/search?q=mobile%20phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
request = requests.get(url).content
soup = BeautifulSoup(request, "html.parser")
data = soup.findAll('a', href=True, attrs={'class': '_1fQZEK'})

for i in data:
    pName = i.find('div', attrs={'class': '_4rR01T'})
    pRating = i.find('div', attrs={'class': '_3LWZlK'})
    
    pPrice = i.find('div', attrs={'class': '_30jeq3 _1_WHN1'})

    PhoneName.append(pName.text)
    PhoneRating.append(pRating.text)
    
    Price.append(pPrice.text)

df = pd.DataFrame({'Phone Name': PhoneName, 'Rating': PhoneRating, 'Price': Price})
print(df)
df.to_csv('asu.csv', index=False, encoding='utf-8')