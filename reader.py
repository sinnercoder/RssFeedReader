import feedparser
url='https://news.google.com/news/rss/?ned=in&hl=en-IN'
feed=feedparser.parse(url)
for news in feed.entries:
  print(news.title)
