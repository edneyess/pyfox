import re

from urllib.request import urlopen
from bs4 import BeautifulSoup

def load(url):
    page = urlopen(url)
    contents = page.read()
    soup = BeautifulSoup(contents, features="lxml")
    for script in soup(["script", "style"]):
        script.extract()    # rip it out
    return soup.get_text()

def check_url(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex,url) is not None

while True:
    page_search = input("type the url:")
    if(page_search == 'exit' or not check_url(page_search)):
        break
    result = load(page_search)
    print(result)