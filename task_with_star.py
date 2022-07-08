HEADERS = {'User-Agent':
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'}
import requests
from bs4 import BeautifulSoup

def task_with_star(article, DESIRED_HUBS):
    for ar in article:
        link = ar.find('a', class_ = 'tm-article-snippet__title-link')
        req_link = requests.get(f'https://habr.com{link.attrs.get("href")}', headers=HEADERS)
        soup_article_body = BeautifulSoup(req_link.text, 'html.parser')
        article_body = soup_article_body.find(class_ ='article-formatted-body').find_all('p')

        for p in article_body:
            article_body_lower = p.text.lower()
            if any([article_body_lower in desired for desired in DESIRED_HUBS]):
            # for i in DESIRED_HUBS:
            #     if i in article_body_lower:
                    # if any([prev_lower in i for i in DESIRED_HUBS]):
                date = soup_article_body.find(class_='tm-article-snippet__datetime-published').find('time')
                title = soup_article_body.find(class_='tm-article-snippet__title').find('span')
                link = ar.find('a', class_ = 'tm-article-snippet__title-link')
                print(date.attrs.get('datetime'))
                print(title.text)
                print(link.attrs.get('href'))
                print()
                break
