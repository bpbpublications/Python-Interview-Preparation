import requests
from bs4 import BeautifulSoup
from collections import deque
import threading
 
class MultithreadedWebCrawler:
    def __init__(self, start_url, max_depth, num_threads):
        self.start_url = start_url
        self.max_depth = max_depth
        self.visited = set()
        self.to_visit = deque([(start_url, 0)])
        self.num_threads = num_threads
        self.lock = threading.Lock()
 
    def crawl(self):
        threads = []
        for _ in range(self.num_threads):
            thread = threading.Thread(target=self.worker)
            threads.append(thread)
            thread.start()
 
        for thread in threads:
            thread.join()
 
    def worker(self):
        while True:
            with self.lock:
                if not self.to_visit:
                    break
                url, depth = self.to_visit.popleft()
 
            if depth <= self.max_depth and url not in self.visited:
                self.visited.add(url)
                print(f"Crawling: {url}, Depth: {depth}")
                links = self.fetch_links(url)
                with self.lock:
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
        valid_links = []
        for link in links:
            if link.startswith('http'):
                valid_links.append(link)
            elif link.startswith('/'):
                valid_links.append(base_url + link)
        return valid_links
