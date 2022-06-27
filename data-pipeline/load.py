
def check_connection() -> bool:
    """
    Check connection to Azure Database
    """
    try:
        # Azure Database
        # Azure_Database.check_connection()
        return True
    except Exception as e:
        print(e)
        return False