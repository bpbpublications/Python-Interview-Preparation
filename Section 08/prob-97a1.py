import requests
from bs4 import BeautifulSoup
from collections import deque
 
class WebCrawler:
    def __init__(self, start_url, max_depth):
        self.start_url = start_url
        self.max_depth = max_depth
        self.visited = set()  # Track visited URLs
        self.to_visit = deque([(start_url, 0)])  # URLs to visit, along with their depth
 
    def crawl(self):
        while self.to_visit:
            url, depth = self.to_visit.popleft()
 
            if depth > self.max_depth:
                continue
 
            if url not in self.visited:
                self.visited.add(url)
                print(f"Crawling: {url}, Depth: {depth}")
 
                links = self.fetch_links(url)
                for link in links:
                    if link not in self.visited:
                        self.to_visit.append((link, depth + 1))
 
    def fetch_links(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            links = [a.get('href') for a in soup.find_all('a', href=True)]
            return self.filter_links(links, url)
        except requests.RequestException as e:
            print(f"Failed to fetch {url}: {e}")
            return []
 
    def filter_links(self, links, base_url):
        # Normalize and filter valid links
        valid_links = []
        for link in links:
            if link.startswith('http'):
                valid_links.append(link)
            elif link.startswith('/'):
                valid_links.append(base_url + link)
        return valid_links
