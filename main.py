#!/usr/bin/python
import sys
import json
import requests
from datetime import datetime

from load_config import *
from articles_store import *
from binance_annoucements import *
from telegram import *


# loads local default configuration ('config.default.json') 
# and overrides with user configuration ('config.user.json')
config = load_config()

def debug(msg):
    print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] {msg}")

def send_telegram_alert(catalogs):
    if len(catalogs) <= 0:
        return

    catalogs_html = []

    for catalog in catalogs:
        htmlContent = '<b>' + catalog['name'] + '</b>\n'

        articles_html = '\n'.join(map(lambda article: f"&#8226;<a href='{article['url']}'>{article['title']}</a>", catalog['articles']))

        htmlContent = f"{htmlContent}{articles_html}"

        catalogs_html.append(htmlContent)

    bot_token = config['telegram']['bot_token']
    user_id = config['telegram']['user_id']

    telegram_send_message(bot_token, user_id, '\n\n'.join(catalogs_html))
    
def main():
    # Load article ids of already known articles
    articles_store_file = config['store']['articles_file']

    article_ids_store = load_articles(articles_store_file)

    # Scrape data from Binance announcements page
    catalogs = get_binance_announcement_catalogs()
    
    # Find new articles
    catalogs_with_new_articles = []

    for catalog in catalogs:
        new_articles = []

        for article in catalog['articles']:
            article_id = article['id']
            
            if article_id not in article_ids_store:
                # Build article url
                article['url'] = f"https://www.binance.com/en/support/announcement/{article['code']}"
                
                new_articles.append(article)

                article_ids_store.append(article_id)
        
        # Did we found new articles for this catalog?
        if len(new_articles) > 0:
            debug(f"Catalog '{catalog['catalogName']}': Found {len(new_articles)} new article(s)")

            debug("\n".join(map(lambda article: f"\tFound new article {article['title']}", new_articles)))

            catalogs_with_new_articles.append({ 'name': catalog['catalogName'], 'articles': new_articles })
        else:
            debug(f"Catalog '{catalog['catalogName']}': No new articles found.")
            
    # Send alert to telegram
    send_telegram_alert(catalogs_with_new_articles)

    # Saver article ids back to store
    save_articles(articles_store_file, article_ids_store)

# Notify of exceptions
def exceptions_hook(exctype, value, traceback):
    bot_token = config['telegram']['bot_token']
    user_id = config['telegram']['user_id']

    telegram_send_message(bot_token, user_id, repr(value))

    sys.__excepthook__(exctype, value, traceback)

sys.excepthook = exceptions_hook

if __name__ == "__main__":    
    debug("Starting...")
    
    main()
