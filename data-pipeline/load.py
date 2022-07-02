import pyodbc
import logging
import pandas as pd

class log_style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

class Database:
    def __init__(self) -> None:
        var_list = ['server', 'database', 'username', 'password']
        self.credentials = pd.read_csv('storage/azure_credentials.csv', names=var_list)
        self.driver = '{SQL Server}'
    
    def post_azure_query(self, query: str) -> list:
        with pyodbc.connect('DRIVER='+self.driver+';SERVER=tcp:'+self.credentials['server'][0]+';PORT=1433;DATABASE='+self.credentials['database'][0]+';UID='+self.credentials['username'][0]+';PWD='+self.credentials['password'][0]) as self.conn:
            with self.conn.cursor() as self.cursor:
                self.cursor.execute(query)
                results = self.cursor.fetchall()
        return results

def log(message: str, color: str) -> None:
    level = logging.DEBUG
    script_name = __file__.split('\\')[-1]
    fmt = f'[%(levelname)s] {log_style.YELLOW}{script_name}{log_style.RESET} %(asctime)s: {color}%(message)s{log_style.RESET}'
    logging.basicConfig(level=level, format=fmt)
    logging.info(message)


def check_connection() -> bool:
    """
    Check connection to Azure Database
    """
    try:
        d = Database()
        query = "SELECT @@Version"
        results = d.post_azure_query(query)
        log(results[0][0], log_style.GREEN)
        return True
    except Exception as e:
        log(e, log_style.RED)
        return False

def load_reddit_data(data: pd.DataFrame) -> None:
    """
    Loads reddit data into Azure Database
    """
    try:
        d = Database()
        query = "INSERT INTO dbo.reddit_data (sub_id, post_user, post_title, post_text, post_time) VALUES (?, ?, ?, ?, ?)"
        data.apply(lambda x: d.post_azure_query(query, x), axis=1)
        log("Reddit data loaded successfully.", log_style.GREEN)
    except Exception as e:
        log(e, log_style.RED)

def load_twiter_data(data: pd.DataFrame) -> None:
    """
    Loads twitter data into Azure Database
    """
    try:
        d = Database()
        query = "INSERT INTO dbo.twitter_data (tweet_date, tweet_user, tweet_text, stock_id) VALUES (?, ?, ?, ?, ?)"
        data.apply(lambda x: d.post_azure_query(query, x), axis=1)
        log("Twitter data loaded successfully.", log_style.GREEN)
    except Exception as e:
        log(e, log_style.RED)

def update_reddit_data(data: pd.DataFrame) -> None:
    """
    Updates sentiment and stock reddit post data in Azure Database
    """
    try:
        d = Database()
        query = "UPDATE dbo.reddit_data SET stock_id = ?, sentiment = ?, use_tag = ? WHERE post_id = ?"
        data.apply(lambda x: d.post_azure_query(query, x), axis=1)
        log("Reddit data updated successfully.", log_style.GREEN)
    except Exception as e:
        log(e, log_style.RED)

def update_twitter_data(data: pd.DataFrame) -> None:
    """
    Updates sentiment twitter post data in Azure Database
    """
    try:
        d = Database()
        query = "UPDATE dbo.twitter_data SET sentiment = ?, use_tag = ? WHERE tweet_id = ?"
        data.apply(lambda x: d.post_azure_query(query, x), axis=1)
        log("Twitter data updated successfully.", log_style.GREEN)
    except Exception as e:
        log(e, log_style.RED)