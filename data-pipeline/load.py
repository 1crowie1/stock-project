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



check_connection()