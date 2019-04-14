import re

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)

def search():
    try:
        browser.get('https://www.taobao.com')
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#q'))
        )
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_TSearchForm > div.search-button > button')))
        input.send_keys('美食')
        submit.click()
        browser.get('http://uland.taobao.com/sem/tbsearch?keyword=%E7%BE%8E%E9%A3%9F&refpid=mm_15891853_2192459_8654707&clk1=0370d6ae0b3faa38fc51f5ee6851746c&upsid=0370d6ae0b3faa38fc51f5ee6851746c')
        total = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#J_waterfallPagination > div > div > span.totalPage'))
        )
        get_products()
        return total.text
    except TimeoutException:
        return True

def first_page():
    submit = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_waterfallPagination > div > div > a:nth-child(2)'))
    )
    submit.click()
    get_products()

def next_page(page_number):
    try:
        # input = wait.until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, '#Jumper'))
        # )
        # submit = wait.until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_waterfallPagination > div > div > a.pageConfirm'))
        # )
        # input.clear()
        # input.send_keys(page_number)
        # submit.click()
        # wait.until(EC.text_to_be_present_in_element(
        #     (By.CSS_SELECTOR,'#J_waterfallPagination > div > div > span.page-cur'),str(page_number))
        # )

        selector = '#J_waterfallPagination > div > div > a:nth-child(%d)'%(page_number + 2)
        submit = wait.until(
             EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
         )
        # print(submit)
        submit.click()
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR,'#J_waterfallPagination > div > div > span.page-cur'), str(page_number + 1))
        )
        # selector = '#J_waterfallPagination > div > div > a:nth-child(%d)' % (page_number + 2)
        # print(selector)
    except TimeoutException:
        return next_page(page_number)

def normal_page(page_number):
    try:
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_waterfallPagination > div > div > a:nth-child(7)'))
        )
        # print(submit)
        submit.click()
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '#J_waterfallPagination > div > div > span.page-cur'), str(page_number + 1))
        )
    except TimeoutException:
        return  normal_page(page_number)

def get_products():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#searchResult.ItemWrapper.item')))
    html = browser.page_source
    doc = pq(html)
    items = doc('#searchResult.ItemWrapper.item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('src'),
            'price': item.find('.price').text(),
        }
        print(product)


def main():
    total = search()
    total = int(re.compile('(\d+)').search(total).group(1))
    first_page()
    for i in range(2, 5):
        next_page(i)
    for i in range(6, total):
        normal_page(i)

if __name__ == '__main__':
    main()



