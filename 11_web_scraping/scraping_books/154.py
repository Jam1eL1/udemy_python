import re
from bs4 import BeautifulSoup

page_path = input('Enter the .html file path or name: ')

class ParsedItem:
    """
    A class to take in an HTML page or content, and find properties of an item
    in it.
    """
    def __init__(self, page_path):
        with open(page_path, 'r')as f:
            page_content = f.read()
            self.soup = BeautifulSoup(page_content, 'html.parser')

    def name(self):
        locator = 'article.product_pod h3 a'
        item_name = self.soup.select_one(locator).attrs['title']
        return item_name

    def link(self):
        locator = 'article.product_pod h3 a'
        item_url = self.soup.select_one(locator).attrs['href']
        return item_url

    def price(self):
        locator = 'article.product_pod p.price_color'
        item_price = self.soup.select_one(locator).string

        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        return float(matcher.group(1))

    def rating(self):
        locator = 'article.product_pod p.star-rating'
        star_rating_element = self.soup.select_one(locator)
        classes = star_rating_element.attrs['class']
        rating_classes = filter(lambda x: x != 'star-rating', classes)
        return next(rating_classes)


item = ParsedItem(page_path)
print(item.price())