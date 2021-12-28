# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 16:10:50 2021

@author: Dominik Chodounský
"""

import urllib.request
from collections import deque # thread safe
from bs4 import BeautifulSoup
import re
import time

class Page():
    
    def __init__(self, url, depth):
        self.url = url
        self.depth = depth
        self.prev = ''
        
    # __hash__ and __eq__ must be defined in order to be able to use class in dict
    def __hash__(self):
        return hash(self.url)

    def __eq__(self, other):
        return self.url == other.url
    
    def __str__(self):
        return self.url
        

def filter_pages(page):
    """ Skips over some largely branching domains. """
    to_filer = ['facebook.com', 'youtube.com', 'twitter.com', 'google.com']
    for f in to_filer:
        if f in page.url:
            return False
    return True


def backtrack(page):
    """ Backtracks the URL path from the found target. """
    if page.depth == 0:
        print(page.depth, page.url)
    
    else:
        print(page.depth, page.url)
        prev = page.prev
        if prev:
            backtrack(prev)
        else:
            print('Error: Page has no previous inlinking page')
            return

def retrieve_links(page_url, depth):
    """ Retrieves href outlinks leading from given page and converts them into pages. """
    html_string = ''
    try:
        response = urllib.request.urlopen(page_url)
        if 'text/html' in response.getheader('Content-Type'):
            html_bytes = response.read()
            html_string = html_bytes.decode('utf-8')
            
        soup = BeautifulSoup(html_string, 'html.parser')
        outlinks = set()
            
            
        # get a (hyperlink) tags of href type which begins with https:// or http://
        for link in soup.find_all('a', attrs={'href': re.compile("^(https|http)://")}):
            #print(link.get('href'))
            new_page = Page(link.get('href').rstrip('/'), depth)
            outlinks.add(new_page)

        return outlinks
    except:
        #print('Error: Could not crawl page ' + page_url)
        return set()
        

def main():
    source_url = 'http://fit.cvut.cz'
    target_url = 'mit.edu'
    
    source_page = Page(url=source_url, depth=0)
    visited = set()
    q = deque([source_page])  
    
    visited_cnt = 0
    
    while q:
        page = q.popleft()
        visited_cnt += 1
        current_links = retrieve_links(page.url, page.depth + 1)
        if len(current_links) == 0:
            continue
        
        new_links = current_links - visited
        new_links = {x for x in new_links if filter_pages(x)}
        q.extend(new_links)
        
        for link in new_links:
            link.prev = page
            
            if target_url in link.url:
                print('\n --- Target ' + str(link.url) + ' acquired! ---\nURL path:\n')
                backtrack(link)
                return visited_cnt

if __name__ == '__main__':
    start = time.time()
    cnt = main()
    print('\nSearch duration: ' + str(time.time() - start) + ' s')
    print('Visited pages: ' + str(cnt))
    
                

    