from datetime import datetime
import requests
import csv
import bs4

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
REQUEST_HEADER = {
    'User-Agent':USER_AGENT,
    'Accept-Language':'en-US,en;q=0.5',
}

def get_page_info(url):
    resp = requests.get(url=url,headers=REQUEST_HEADER)
    return resp.content

def extract_detail(url):
    detail = {}
    print("URL:", url)
    htmlpage = get_page_info(url)
    print(htmlpage)



if __name__ == "__main__":
    with open('wonder.csv') as file:
        reader = csv.reader(file,delimiter=',')
        for i in reader:
            url = i[0]
            extract_detail(url)
            