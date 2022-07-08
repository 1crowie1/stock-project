import transform
import scrape_reddit
import scrape_twitter

def main() -> None:
    """
    Extract data from data sources and pass to transform module
    """
    subs_data = scrape_reddit.scrape_subreddits()
    transform.format_reddit_data(subs_data)
    return

if __name__ == '__main__':
    main()