#import the feedparser library first
import feedparser 

#url is any rss feed url of website where you want to read rss fedds of
url='https://news.google.com/news/rss/?ned=in&hl=en-IN'


feed=feedparser.parse(url)

#t print the title of news 
#you can also print summary and other contents like date and all using that variable like news.summary etc
for news in feed.entries:
  print(news.title)
