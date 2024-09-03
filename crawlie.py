import requests
import argparse

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

parser = \
    argparse.ArgumentParser(epilog='Command : python3 crawlie.py -u "cybernotes.uk"'
                            )
parser.add_argument('-u',
                    help='Add URL for crawler',
                    required=True)
args = parser.parse_args()
target = args.u
c1 = 0
c2 = 0

with open("subdomains.txt", "r") as wordlist:
    for line in wordlist:
        word = line.strip()
        target2 = word + "." + target
        response = request(target2)
        if response:
            c1 = c1 + 1
            print(f"{c1}:[+]: Subdomain Found: " + target2)
        else:
            c1 = c1 + 1
            print(f"{c1}:[+] Subdomain Not Found: " + target2)

with open("common.txt", "r") as wordlist:
    for line in wordlist:
        word = line.strip()
        target2 = target + "/" + word
        response = request(target2)
        if response:
            c2 = c2 +1
            print(f"{c2}:[+] Domain Found: " + target2)
        else:
            c2 = c2 + 1
            print(f"{c2}:[+] Domain Not Found: " + target2)
