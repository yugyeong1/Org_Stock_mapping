from pandas import options
from selenium import webdriver
from time import sleep

companylist = ['facebook','google']
base_url ='https://www.google.com/search?q='

for company in companylist:
    driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
    tail = company + "+" + "stock"
    url = base_url+tail
    driver.get(url)

    driver.implicitly_wait(time_to_wait=5)
    stock_xpath = driver.find_element_by_xpath('//*[@id="rcnt"]/div[1]/div/div/div[3]/div[1]/div/div[2]/div/div/div/div[2]/div[1]')
    stock = stock_xpath.text
    driver.quit()
    sleep(1)

    print(stock)

