import feedparser
from bs4 import BeautifulSoup
import lxml

def get_mastodon_feed(mastodon_user_url:str):
    request_mastodon_feed = feedparser.parse(mastodon_user_url)
    text_of_feed = ""
    
    for i in range(0,15):
        text_of_feed += request_mastodon_feed.entries[i].summary + '\n' + '___' + '\n'

    soup_cleaned = BeautifulSoup(text_of_feed, "lxml")

    return soup_cleaned

example_feed = get_mastodon_feed("https://fedi.simonwillison.net/@simon.rss")
print(example_feed.text)
