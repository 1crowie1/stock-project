import dbapi
import logging

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

def main() -> None:
    script_name = __file__.split('\\')[-1]
    level = logging.DEBUG
    fmt = f'[%(levelname)s] {log_style.YELLOW}{script_name}{log_style.RESET} %(asctime)s: %(message)s'
    logging.basicConfig(level=level, format=fmt)

    logging.info(f'{log_style.BLUE}{log_style.UNDERLINE}Application Started{log_style.RESET}')

    if not dbapi.check_conn():
        logging.warning(f'{log_style.RED}Database connection failed.{log_style.RESET}')
        return
    logging.info('\033[32mDatabase connection successful.\033[0m')

if __name__ == '__main__':
    main()