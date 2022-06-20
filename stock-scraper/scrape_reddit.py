import praw
import pandas as pd

class Reddit_Scraper:
    def __init__(self) -> None:
        self.credentials = pd.read_csv('reddit_credentials.csv')
        self.reddit_read_only = praw.Reddit(client_id=credentials['client_id'][0], 
                                       client_secret=credentials['client_secret'][0], 
                                       user_agent=credentials['user_agent'][0])
    
    def get_authenticated_reddit_client(self) -> praw.Reddit:
        return self.reddit_read_only

def scrape_wsb_sub() -> None:
    wsb_instance = Reddit_Scraper()
    wsb_client = wsb_instance.get_authenticated_reddit_client()
    wsb_sub = wsb_client.subreddit('wallstreetbets')

    return

def scrape_stockmarket_sub() -> None:
    stockmarket_instance = Reddit_Scraper()
    stockmarket_client = stockmarket_instance.get_authenticated_reddit_client()
    stockmarket_sub = stockmarket_client.subreddit('StockMarket')
    return

def scrape_stocks_sub() -> None:
    stocks_instance = Reddit_Scraper()
    stocks_client = stocks_instance.get_authenticated_reddit_client()
    stocks_sub = stocks_client.subreddit('stocks')
    return

def scrape_subreddits() -> None:
    scrape_wsb()
    return


def main() -> None:
    scrape_subreddits()
    return

if __name__ == '__main__':
    main()