#coding=utf-8

import sys
from selenium import webdriver
import time
import re

reload(sys)
sys.setdefaultencoding('utf-8')

browser = webdriver.Chrome()

browser.get('https://10.44.192.156')

browser.maximize_window()
browser.implicitly_wait(10)

browser.find_element_by_id('iptUserName').send_keys('Administrator')
browser.implicitly_wait(1)
browser.find_element_by_id('iptPassword').send_keys('Huawei12#$')
browser.find_element_by_id("btnLogin").click()
browser.implicitly_wait(10)
#iframe = browser.find_element_by_xpath('//*[@id="rightMid"]')



browser.switch_to.default_content()
browser.switch_to.frame("rightMid")
#SN = browser.find_element_by_id('floatTitle').text
#BMCIP = browser.find_element_by_css_selector("#txtBMCIp").text()
#SN = browser.find_element_by_partial_link_text("序列")#BMCIP = browser.switchTo().frame("left_frame").findElement(By.id("txtBMCIp"))
#BMCIP = browser.find_element_by_id('txtBMCIp').text
#browser.find_element_by_css_selector("#lnkNetWorkCfg").click()
browser.find_element_by_id('btnLightBlink').click()
#BMCIP = browser.find_element_by_id("server_name_hidden").get_attribute("value")
def write_to_file():
    with open('result.txt','w') as f:
#        f.write( BMCIP + '\n')
#        f.write( SN + '\n')
        f.write( '哇哈哈' + '\n')
        f.close()
write_to_file()
#time.sleep(10)
#browser.quit()
