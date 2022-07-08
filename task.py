

def task(article, DESIRED_HUBS, ):
    for ar in article:
        preview = ar.find(class_ = 'article-formatted-body').find_all('p')
        for prev in preview:
            prev_lower = prev.text.lower()
            if any([prev_lower in desired for desired in DESIRED_HUBS]):
                date = ar.find(class_ = 'tm-article-snippet__datetime-published').find('time')
                title = ar.find(class_ = 'tm-article-snippet__title-link').find('span')
                link = ar.find('a', class_ = 'tm-article-snippet__title-link')
                print(date.attrs.get('datetime'))
                print(title.text)
                print(link.attrs.get('href'))
                print()
                break