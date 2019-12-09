#coding=utf-8

import sys
from selenium import webdriver
from threading import Thread,Semaphore
import time
import re
import subprocess
from selenium.webdriver.support.ui import WebDriverWait

reload(sys)
sys.setdefaultencoding('utf-8')


file = open("information.txt", "r") #用户名文件
ip_list = []
for i in file.readlines():
    i_array = i.split("\t")
    ip_list.append(i_array[0])
file.close()
sem = Semaphore(5)

def get_info(ip,username='Administrator',passwd='Admin@9000'):
    
    try:
        browser = webdriver.Chrome()
        browser.get('https://%s'%ip)
        browser.set_page_load_timeout(10)
        print  '%s is runnung ...'%ip
        browser.maximize_window()
        browser.implicitly_wait(10)
        
        browser.find_element_by_id('iptUserName').send_keys('%s'%username)
        browser.implicitly_wait(1)
        browser.find_element_by_id('iptPassword').send_keys('%s'%passwd)
        browser.find_element_by_id("btnLogin").click()
        browser.implicitly_wait(10)
    
        browser.switch_to.default_content()
        browser.switch_to.frame("rightMid")
        browser.implicitly_wait(30)
        WebDriverWait(browser, 10).until(lambda the_driver:the_driver.find_element_by_id('txtSequence').is_displayed())
        SN = browser.find_element_by_id('txtSequence').text
        BMCIP = browser.find_element_by_id('txtBMCIp').text
        
        with open('result.txt','a') as f:
            f.write( BMCIP +';'+ SN +'\n')
            f.close()
        sem.release()
        browser.quit()
    except Exception as SN:
        SN = 'Unable to connection'
        with open('result.txt','a') as f:
            f.write( ip +';'+ SN +'\n')
            f.close()
        browser.quit()
 


def main():
    for ip in ip_list:
        sem.acquire()
        t = Thread(target=get_info,args=(ip,))
        t.start()
                
    #time.sleep(10)
    

if __name__=="__main__":
    main()
