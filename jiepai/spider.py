from urllib.parse import urlencode
import requests
from requests import RequestException


def get_page_index(offset,keyword):
    data = {
        'aid':'24',
        'app_name':'web_search',
        'offset':offset,
        'format':'json',
        'keyword':keyword,
        'autoload':'true',
        'count':'20',
        'en_qc':'1',
        'cur_tab':'1'
    }
    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(data)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求失败')
        return None

def main():
    html = get_page_index(0,'街拍')
    print(html)

if __name__ == '__main__':
    main

#this is beautiful