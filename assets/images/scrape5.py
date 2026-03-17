import os
import re
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

BASE_URL = "https://www.exmusicsummerschool.co.uk/"
SAVE_DIR = "images"

os.makedirs(SAVE_DIR, exist_ok=True)

HEADERS = {"User-Agent": "Mozilla/5.0"}

visited = set()
to_visit = [BASE_URL]
images = set()


def extract_images(html):
    pattern = r"https://static\.wixstatic\.com/media/[^\"]+"
    return re.findall(pattern, html)


print("Crawling site...")

while to_visit:
    url = to_visit.pop()

    if url in visited:
        continue

    visited.add(url)

    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        html = r.text

        print("Scanning:", url)

        # extract wix images
        imgs = extract_images(html)
        for img in imgs:
            img = re.sub(r"/v1/.*", "", img)
            images.add(img)

        soup = BeautifulSoup(html, "html.parser")

        # find internal links
        for a in soup.find_all("a", href=True):
            link = urljoin(BASE_URL, a["href"])

            if BASE_URL in link and link not in visited:
                to_visit.append(link)

    except Exception as e:
        print("Error:", e)


print("\nFound", len(images), "unique images")


def download(url):
    filename = os.path.basename(urlparse(url).path)
    path = os.path.join(SAVE_DIR, filename)

    try:
        r = requests.get(url, headers=HEADERS, timeout=20)

        if r.status_code == 200:
            with open(path, "wb") as f:
                f.write(r.content)

            print("Downloaded:", filename)

    except:
        print("Failed:", url)


for img in images:
    download(img)
