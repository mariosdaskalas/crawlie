import requests
import re
import urllib.parse as urlparse
import argparse

target_link = []

parser = \
    argparse.ArgumentParser(epilog='Command : python3 spider.py -u "https://cybernotes.uk"'
                            )
parser.add_argument('-u',
                    help='Add URL for spider',
                    required=True)
args = parser.parse_args()
target = args.u

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