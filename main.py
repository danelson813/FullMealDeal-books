from src.helpers import *
from src.log_helper import *


def main():
    results = []
    for page in range(1, 51):
        url = form_url(page)
        soup = make_soup(url)
        books = get_books(soup)
        data = parse_books(books, results)
    dataframe(data)


if __name__ == '__main__':
    main()
