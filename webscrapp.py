#Diya kudchi
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
url = "https://openlibrary.org/?msclkid=b9c10303cea211eca08cb602f82cc7eb"
r = requests.get(url)
htmlContent = r.content
print(htmlContent)

soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup.prettify)

title = soup.title
print(type(title.string))

#print all paragraphs from the page
paras = soup.find_all('p')
print(paras)

#get anchor tags from the page
anchors = soup.find_all('a')

#get links on the page
for link in anchors:
    print(link.get('href'))
    
    

#matplotlib
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()
