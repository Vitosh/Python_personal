import urllib.request 
from bs4 import BeautifulSoup 

class SiteCrawler():
    def __init__(self, url, level):
        self.links = set()
        self.initial_url = url
        self.levels = level
        self.counter_frequency = 10
        self.counter = 0

    def scrape_site(self):
        links_previous_level = self.get_links(self.initial_url)
        self.links = links_previous_level.copy()

        for i in range (self.levels):
            links_this_level = set()
            for link in links_previous_level:
                link_to_visit = link[0]
                self.counter = self.counter + 1
                self.print_if_needed(link)

                new_set = self.get_links(link_to_visit)
                links_this_level = links_this_level.union(new_set)

            links_previous_level = links_this_level.copy()
            self.links.union(links_this_level)


    def get_links(self, url):    
        try:
            resp = urllib.request.urlopen(url)
            soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'), features="html.parser")
            hrefs = soup.find_all('a', href=True)
            links = set()
            for href in hrefs:        
                href_to_append = href['href']
                if (href_to_append[:4] == "http"):
                    tuple_to_append = tuple([href_to_append, url])
                    if(tuple_to_append not in self.links):
                        links.add(tuple_to_append)                                            
            return links
        except:            
            print("NOT ALLOWED -> " + url)
            return set(tuple(["Scraping problem -" + url, url]))

    def print_if_needed(self, text_to_print):
        if self.counter % self.counter_frequency == 0:
            print(text_to_print)
