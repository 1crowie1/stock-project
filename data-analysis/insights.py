import dbapi
import logging

def main() -> None:
    script_name = __file__.split('\\')[-1]
    level = logging.DEBUG
    fmt = f'[%(levelname)s] \033[33m{script_name}\033[0m %(asctime)s: %(message)s'
    logging.basicConfig(level=level, format=fmt)

    logging.info('\033[34m\033[4mApplication Started\033[0m')

    if not dbapi.check_conn():
        logging.warning('\033[31mDatabase connection failed.\033[0m')
        return
    logging.info('\033[32mDatabase connection successful.\033[0m')

if __name__ == '__main__':
    main()