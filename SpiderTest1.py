import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}
url = 'https://voice.hupu.com/nba' # 爬取的网址虎扑nba新闻
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'lxml')

# 找出class属性值为news-list的div
news_list = soup.find('div', {'class': 'news-list'})
# 找出news_list下的所有li标签
news = news_list.find_all('li')
news_titles = []
news_source = []

# 遍历news
for i in news:
    try:
        # 提取新闻标题
        title = i.find('h4').get_text().strip()
        # 提取新闻来源
        source = i.find('span', {'class': 'comeFrom'}).find('a').get_text().strip()
        # 存储爬取结果
        news_titles.append(title)
        news_source.append(source)
        print('新闻标题：', title)
        print('新闻来源：', source)
        print()
    except AttributeError as e:
        continue