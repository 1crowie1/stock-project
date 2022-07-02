import pyodbc
import pandas as pd

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


def check_connection() -> bool:
    """
    Check connection to Azure Database
    """
    try:
        d = Database()
        query = "SELECT @@Version"
        results = d.post_azure_query(query)
        print(results[0])
        return True
    except Exception as e:
        print(e)
        return False

print(check_connection())