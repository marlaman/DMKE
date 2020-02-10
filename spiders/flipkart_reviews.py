import time
from bs4 import BeautifulSoup
from selenium import webdriver
import sys
import os
import numpy as np
import pandas as pd

# link = "https://www.flipkart.com/poco-f1-graphite-black-64-gb/product-reviews/itmf8fyjyssnt25c?&pid=MOBF85V7A6PXETAXpage"
link = "https://www.flipkart.com/apple-macbook-air-core-i5-5th-gen-8-gb-128-gb-ssd-mac-os-sierra-mqd32hn-a-a1466/product-reviews/itmevcpqqhf6azn3?&pid=COMEVCPQBXBDFJ8C&lid=LSTCOMEVCPQBXBDFJ8C4V6AHG&marketplace=FLIPKART&page={}"
alltitles = []
allreviews = []
allstars = []
path = 'chromedriver'
# sys.path.append(path)
driver = webdriver.Chrome(os.path.join(os.getcwd(), 'chromedriver'))
#If necessary, define the chrome path explicitly
for page_num in range(1,5):
    driver.get(link.format(page_num))
    [item.click() for item in driver.find_elements_by_class_name("_1EPkIx")]
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    print(len(soup.findAll("div", class_= '_1PBCrt')))
    for items in soup.findAll("div", class_= '_1PBCrt'):
        print(items)
        title = items.select_one("p._2xg6Ul").text
        review = ' '.join(items.select_one(".qwjRop").text.split())
        stars = items.select_one("div", class_="hGSR34 E_uFuv").text[0]
        alltitles.append(title)
        allreviews.append(review)
        allstars.append(stars)
        print(f'{title}\n{review}\n')
    print(alltitles)
    print(allreviews)
mainreviews = pd.DataFrame([])
mainreviews['Title'] = np.array(alltitles)
mainreviews['Review'] = np.array(allreviews)
mainreviews['Stars'] = np.array(allstars)

mainreviews.to_csv('flipkartreviews.csv')


driver.quit()
