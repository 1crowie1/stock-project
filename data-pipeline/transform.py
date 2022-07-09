import load
import pandas as pd

def format_reddit_data(subs_data: pd.DataFrame) -> pd.DataFrame:
    """
    Format data for loading into Azure Database
    """
    columns = ['sub_id', 'post_user', 'post_title', 'post_text', 'post_time']
    return