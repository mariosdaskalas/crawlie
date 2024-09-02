import requests
import re
import urllib.parse as urlparse

target = "http://127.0.0.1:8090"
target_link = []

def extract(url):
    resp = requests.get(url)
    return re.findall('(?:href=")(.*?)"', resp.content.decode(errors="ignore"))

def crawl(url):
    hrefs = extract(url)
    for link in hrefs:
        link = urlparse.urljoin(url, link)

        if "#" in link:
            link = link.split("#")[0]

        if target in link and link not in target_link:
            target_link.append(link)
            print(link)
            crawl(link)

crawl(target)