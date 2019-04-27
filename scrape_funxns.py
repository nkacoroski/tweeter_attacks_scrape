import requests
import time
import random

def get_article_links(browser):
    '''Get article links from query page.
        Returns a list of urls.'''
    sel = 'dt a'
    links = browser.find_elements_by_css_selector(sel)
    urls = [link.get_attribute('href') for link in links]
    return urls

    
def get_data_from_article(browser):
    '''Returns a dictionary'''
    data = {}
    data['title'] = browser.find_element_by_tag_name('h1').text
    print(type(data['title']))
    data['title'] = data['title'][11:] # removes "[TWEETER]"
    data['author'] = browser.find_elements_by_tag_name('b')[0].text
        # the first bolded is our author
    data['date'] = browser.find_element_by_tag_name('i').text
    data['text'] = browser.find_elements_by_tag_name('body')[0].text
    text_start_index = data['text'].find('author ]\n') + 9 
    data['text'] = data['text'][text_start_index:]
    return data

def next_query_page():
    pass

def scrape_articles_of_page(browser, links):
    for link in links:
        browser.get(link)
        time.sleep(2 + random.random()*10)
        yield get_data_from_article(browser)
