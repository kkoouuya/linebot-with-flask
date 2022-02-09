from bs4 import BeautifulSoup
import requests

def getNews(word):
  
  url = f"https://news.yahoo.co.jp/search?p={word}&ei=utf-8&aq=0"

  res = requests.get(url)
  soup = BeautifulSoup(res.text, "html.parser")
  
  titles = soup.find_all('div', class_={'newsFeed_item_title'})
  titles = [title.text for title in titles]
  links =  soup.find_all('a', class_={'newsFeed_item_link'})
  links = [link.get('href') for link in links]
  
  articles = []
  for title, link in zip(titles, links):
      articles.append(title)
      articles.append(link)
      if len(articles) == 10:
        break
  
  if type(articles) is not list:
    pass
  
  result = '\n'.join(articles)
      
  return result