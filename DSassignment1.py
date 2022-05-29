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

#output :
   """phone rating price
0          realme C11 2021 (Cool Grey, 32 GB)    4.4   ₹7,499
1            realme C31 (Light Silver, 32 GB)    4.5   ₹9,299
2              realme C31 (Dark Green, 64 GB)    4.4   ₹9,999
3                POCO C31 (Royal Blue, 64 GB)    4.4   ₹8,499
4          realme C11 2021 (Cool Blue, 64 GB)    4.3   ₹8,999
5          realme C11 2021 (Cool Blue, 32 GB)    4.4   ₹7,499
6          realme C11 2021 (Cool Grey, 64 GB)    4.3   ₹8,999
7            realme C31 (Light Silver, 64 GB)    4.4   ₹9,999
8                POCO C31 (Royal Blue, 32 GB)    4.4   ₹7,499
9              realme C31 (Dark Green, 32 GB)    4.5   ₹9,299
10          realme C35 (Glowing Black, 64 GB)    4.4  ₹11,999
11            MOTOROLA G60 (Moonless, 128 GB)    4.2  ₹14,999
12              POCO C31 (Shadow Gray, 64 GB)    4.4   ₹8,499
13  REDMI Note 10T 5G (Metallic Blue, 128 GB)    4.3  ₹13,999
14           vivo T1 44W (Starry Sky, 128 GB)    4.5  ₹15,999
15           vivo T1 44W (Starry Sky, 128 GB)    4.5  ₹14,499
16           vivo T1 44W (Starry Sky, 128 GB)    4.5  ₹17,999
17      vivo T1 44W (Midnight Galaxy, 128 GB)    4.5  ₹14,499
18      REDMI Note 10S (Deep Sea Blue, 64 GB)    4.4  ₹12,999
19          realme C35 (Glowing Green, 64 GB)    4.4  ₹11,999
20   REDMI Note 10T 5G (Metallic Blue, 64 GB)    4.5  ₹11,999
21            MOTOROLA e40 (Pink Clay, 64 GB)    4.1   ₹9,999
22      REDMI 9i Sport (Metallic Blue, 64 GB)    4.4   ₹8,799
23              POCO C31 (Shadow Gray, 32 GB)    4.4   ₹7,499 """
