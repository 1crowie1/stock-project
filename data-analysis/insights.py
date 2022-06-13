import dbapi

def main() -> None:
    if not dbapi.check_conn():
        print('\033[31m Database connection failed.')
        return
    print('\033[32mDatabase connection successful.')

if __name__ == '__main__':
    main()