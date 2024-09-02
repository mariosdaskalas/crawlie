import requests

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

target = "cybernotes.uk"

with open("subdomains.txt", "r") as wordlist:
    for line in wordlist:
        word = line.strip()
        target2 = word + "." + target
        response = request(target2)
        if response:
            print("[+] Subdomain Found: " + target2)
        else:
            print("[+] Subdomain Not Found: " + target2)
