def crawling(url):
    import requests
    from bs4 import BeautifulSoup

    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    return soup