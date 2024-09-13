#import libriares
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Create a driver who interact with browser
driver = webdriver.Chrome()

#Setting the Search Query and File Counter
query="Mobile"
file=0

#Looping Through Search Result Pages
for i in range(1,20):
    driver.get(f'https://www.flipkart.com/search?q={query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&page={i}')

    elems=driver.find_elements(By.CLASS_NAME,'tUxRFH') #Finding Elements on Each Page
    print(f"{len(elems)} item found")
    for elem in elems: #Saving Each Element's HTML Content
        d=elem.get_attribute('outerHTML')
        with open(f'C:/Users/nikhi/PycharmProjects/pythonProject1/data/{query}_{file}.html',"w",encoding='utf-8') as f:
            f.write(d)
            file+=1
    time.sleep(2)  #Pausing Between Page Loads
driver.close()      #Closing the Browse



