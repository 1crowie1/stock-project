from typing import Dict
import praw
import pandas as pd

class Reddit_Scraper:
    def __init__(self) -> None:
        var_list = ['client_id', 'client_secret', 'user_agent']
        self.credentials = pd.read_csv('stock-scraper/reddit_credentials.csv', names=var_list)
        self.reddit_read_only = praw.Reddit(client_id=f"{self.credentials['client_id'][0]}", 
                                       client_secret=f"{self.credentials['client_secret'][0]}", 
                                       user_agent=f"{self.credentials['user_agent'][0]}")
    
    def get_authenticated_reddit_client(self) -> praw.Reddit:
        return self.reddit_read_only

def scrape_wsb_sub() -> dict:
    wsb_instance = Reddit_Scraper()
    wsb_client = wsb_instance.get_authenticated_reddit_client()
    wsb_sub = wsb_client.subreddit('wallstreetbets')
    print(f"Subreddit: {wsb_sub.display_name}")

    wsb_posts = {'Title': [], 'PostText': []}

    posts = wsb_sub.top("month")
    for post in posts:
        wsb_posts['Title'].append(post.title)
        wsb_posts['PostText'].append(post.selftext)

    return wsb_posts

def scrape_stockmarket_sub() -> dict:
    stockmarket_instance = Reddit_Scraper()
    stockmarket_client = stockmarket_instance.get_authenticated_reddit_client()
    stockmarket_sub = stockmarket_client.subreddit('StockMarket')
    
    stockmarket_posts = {'Title': [], 'PostText': []}

    posts = stockmarket_sub.top("month")
    for post in posts:
        stockmarket_posts['Title'].append(post.title)
        stockmarket_posts['PostText'].append(post.selftext)

    return stockmarket_posts

def scrape_stocks_sub() -> dict:
    stocks_instance = Reddit_Scraper()
    stocks_client = stocks_instance.get_authenticated_reddit_client()
    stocks_sub = stocks_client.subreddit('stocks')
    
    stocks_posts = {'Title': [], 'PostText': []}

    posts = stocks_sub.top("month")
    for post in posts:
        stocks_posts['Title'].append(post.title)
        stocks_posts['PostText'].append(post.selftext)

    return stocks_posts

def scrape_subreddits() -> None:
    wsb_data = scrape_wsb_sub()
    stockmarket_data = scrape_stockmarket_sub()
    stocks_data = scrape_stocks_sub()

    wsb_output = pd.DataFrame.from_dict(wsb_data, orient='index')
    stockmarket_output = pd.DataFrame.from_dict(stockmarket_data, orient='index')
    stocks_output = pd.DataFrame.from_dict(stocks_data, orient='index')

    wsb_output.to_csv('wsb_data.csv')
    stockmarket_output.to_csv('stockmarket_data.csv')
    stocks_output.to_csv('stocks_data.csv')
    return


def main() -> None:
    scrape_subreddits()
    return

if __name__ == '__main__':
    main()