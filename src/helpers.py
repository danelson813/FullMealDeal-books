# src/helpers.py

import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from src.log_helper import *
from src.db_books import *

def form_url(page: int):
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    logger.info(f"Working on page: {page}")
    return url


def make_soup(url: str):
    page = requests.get(url)
    soup = bs(page.text, 'html.parser')
    return soup


def get_books(soup):
    return soup.find_all("article")


def parse_books(books: list, results: list):
    base = 'https://books.toscrape.com/'

    for book in books:
        title = book.find('div', class_='image_container').find('a').find('img')['alt']
        price = book.find('p', class_='price_color').get_text()[2:]
        link = base + 'catalogue/' + book.find('div', class_='image_container').find('a')['href']
        img_link = base + book.find('div', class_='image_container').find('a').find('img')['src'][3:]

        result = {'title': title, 'price': price, 'link': link, 'img_link': img_link}
        results.append(result)

    return results


def dataframe(results: list):
    df = pd.DataFrame(results)
    df.to_csv('data/books.csv', index=False, encoding='UTF-8')
    df.to_sql('books', conn, if_exists='replace', index=False)
    logger.info("******************** JOB FINISHED ********************")

