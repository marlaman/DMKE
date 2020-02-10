import time
from bs4 import BeautifulSoup
from selenium import webdriver
import sys
import os
import numpy as np
import pandas as pd
from difflib import SequenceMatcher

driver = webdriver.Chrome(os.path.join(os.getcwd(), 'spiders/chromedriver'))
link = 'https://www.flipkart.com/lenovo-ideapad-s145-apu-dual-core-a6-4-gb-1-tb-hdd-windows-10-home-s145-15ast-laptop/p/itmb227f905056eb?pid=COMFMHWEKBP4TBGJ&lid=LSTCOMFMHWEKBP4TBGJI8DKMT&marketplace=FLIPKART&srno=b_1_1&otracker=hp_omu_Limited%2BPeriod%2BDeals_4_7.dealCard.OMU_Limited%2BPeriod%2BDeals_7Y9PJF4IR7ZL_5&otracker1=hp_omu_WHITELISTED_neo%2Fmerchandising_Limited%2BPeriod%2BDeals_NA_dealCard_cc_4_NA_view-all_5&fm=neo%2Fmerchandising&iid=3b18a00e-e0e0-449b-923e-aa02b549b18a.COMFMHWEKBP4TBGJ.SEARCH&ppt=browse&ppn=browse&ssid=kizs5r2kv40000001581177461592'
driver.get(link)
soup = BeautifulSoup(driver.page_source, 'lxml')
stats = soup.findAll("tr", class_= '_3_6Uyw row')
for x in stats:
    if(x.text.startswith("Model Number")):
        model = x.text[12:]
        print("Model is:",model)
x = driver.find_element_by_css_selector('.col._39LH-M a')
print(x)

# for q in x:
#     q.click()
#     break
# print(len(stats))
# driver.quit()
# modellist = model.split()
# search = ""
# for i in modellist:
#     search = search + "+" + i
# search = search[1:]
# driver = webdriver.Chrome(os.path.join(os.getcwd(), 'spiders/chromedriver'))
# amazon = 'https://www.amazon.in/s?k={}&ref=nb_sb_noss_2'
# snapdeal = 'https://www.snapdeal.com/search?keyword={}&santizedKeyword=&catId=&categoryId=0&suggested=true&vertical=&noOfResults=20&searchState=&clickSrc=suggested&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy'
# driver.get(amazon.format(search))
# soup = BeautifulSoup(driver.page_source, 'lxml')
# print(len(soup.findAll("h2", class_= 'a-size-mini')))
# # print(len(soup.find_elements_by_class_name('a-size-mini')))
# products = driver.find_elements_by_css_selector('.a-link-normal.a-text-normal')
# for w in products:
#     w.click()
#     break
# # driver.quit()
# driver = webdriver.Chrome(os.path.join(os.getcwd(), 'spiders/chromedriver'))
# driver.get(snapdeal.format(search))
# products = driver.find_elements_by_css_selector('.dp-widget-link.noUdLine.hashAdded')
# for w in products:
#     w.click()
#     break
# driver.quit
#
