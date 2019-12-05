#coding=utf-8

import sys
from selenium import webdriver
import time
import re

reload(sys)
sys.setdefaultencoding('utf-8')

browser = webdriver.Chrome()

browser.get('https://10.44.192.118')

browser.maximize_window()
browser.implicitly_wait(10)

browser.find_element_by_id('iptUserName').send_keys('Administrator')
browser.implicitly_wait(1)
browser.find_element_by_id('iptPassword').send_keys('Admin@9000')
browser.find_element_by_id("btnLogin").click()

browser.switch_to_frame('mainFrame')
Select(driver.find_element_by_id("txtBMCIp")).select_by_index(1)
BMCIP = Select(driver.find_element_by_id("txtBMCIp")).select_by_index(1)
#SN = browser.find_element_by_id('txtSequence').text
#pattren = re.compile('<p.*?"txtBMCIp".*?>(\d+.\d+.\d+.\d+)<')
#BMCIP = re.search(pattren.html)

def write_to_file():
    with open('result.txt','a') as f:
        f.write( BMCIP +'\n')
        f.close()
write_to_file()
#time.sleep(10)
#browser.quit()
