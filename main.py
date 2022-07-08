DESIRED_HUBS = ['дизайн', 'фото', 'web', 'python']
HEADERS = {'User-Agent':
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'}
import requests
from bs4 import BeautifulSoup
from task import task
from task_with_star import task_with_star

if __name__ == '__main__':

    req = requests.get('https://habr.com/ru/all/', headers = HEADERS)
    soup = BeautifulSoup(req.text, 'html.parser')
    article = soup.find_all('article')

    while True:
        command = int(input('''            Просто задача  --> 1 
            Задача со звездочкой --> 2  
            Выйти --> 0
            Ваш выбор: '''))
        if command == 1:
             task(article, DESIRED_HUBS)
        elif command == 2:
            task_with_star(article, DESIRED_HUBS)
        elif command == 0:
            break


