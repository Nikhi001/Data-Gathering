# Importing Required Libraries
from bs4 import BeautifulSoup
import os
import pandas as pd


d={'title':[],'price':[],'link':[]} #Initializing a Dictionary to Store Data
for file in os.listdir('data'):     #Iterating Over HTML Files
    try:
        with open(f'C:/Users/nikhi/PycharmProjects/pythonProject1/data/{file}') as f:
            html_doc=f.read()
        soup=BeautifulSoup(html_doc,'html.parser')
        #Title scrap hua
        t=(soup.find('div',class_="KzDlHZ")) #Extracting the Product Title
        title=t.get_text()

        #Link scrap hua
        i=(soup.find('div'))    #Extracting the Product Link
        l=i.find('a')
        link="https://www.flipkart.com"+l['href']

        # Price
        p = (soup.find('div', class_="Nx9bqj _4b5DiR"))     #Extracting the Product Price
        price=p.get_text()
        #print(title,link,price)
                     #subtitude print(t.string) use kar sakte h without used get_text()
        d['title'].append(title)    #Storing the Extracted Data in the Dictionary
        d['price'].append(price)
        d['link'].append(link)
    except Exception as e:      #Error Handling
        print(e)
df= pd.DataFrame(data=d)        #Creating a DataFrame and Saving to CSV
df.to_csv('Filpkart01.csv')