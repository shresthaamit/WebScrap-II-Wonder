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

def get_page_title(soup):
    my_title= soup.find('h1',attrs={'class':'post-title'})
    return my_title.text
    
def get_content_author(soup):
    get_author  = soup.find('span', attrs={'class':'meta-item post-author'})
    by_name =  get_author.find('span', class_='by').text.strip()
    author = get_author.find('a').text.strip()
    return by_name,author
    
def get_category(soup):
    get_category = soup.find('span', attrs={'class': 'cat-label'})
    get_category_name = get_category.find('a')
    return get_category_name.text.strip().split()[0]

def get_side_categories(soup):
    get_all_categories = soup.find('li', attrs={'id':'categories-5'})
    inside_categories = get_all_categories.find('ul')
    allcategories_list=[]
    for categories in inside_categories.find_all('li',attrs={'class':'cat-item'}):
        get_link = categories.find('a')
                
        if get_link:
            allcategories_list.append(get_link.text.strip())
    return allcategories_list
def extract_detail(url):
    detail = {}
    # print("URL:", url)
    htmlpage = get_page_info(url)
    soup = bs4.BeautifulSoup(htmlpage,'lxml')
    detail['title'] = get_page_title(soup)
    detail['author'] = get_content_author(soup)
    detail['category'] = get_category(soup)
    detail['allsidecategories'] = get_side_categories(soup)
    print(detail)


if __name__ == "__main__":
    with open('wonder.csv') as file:
        reader = csv.reader(file,delimiter=',')
        for i in reader:
            url = i[0]
            extract_detail(url)
            