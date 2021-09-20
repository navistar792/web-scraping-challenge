
# Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import json
import time

def scrape_info():
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # URL of page to be scraped redplanetscience
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    # Retrieve page with the requests module
    # response = requests.get(url)
    # Create BeautifulSoup object; parse with 'lxml'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
   
    # redplanet results
    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text
   
    # create main dictionary for mongo append

    # dictionary = {'news_title': news_title},
    #             '2':{'news_p': news_p}}
    dictionary = {'1':{'news_title': news_title},
              '2':{'news_p': news_p}}
    
    browser.quit()
    
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # URL of page to be scraped redplanetscience
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Create BeautifulSoup object; parse with 'lxml'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
   
    # https://spaceimages-mars.com/image/featured/mars3.jpg - redplanet results

    news_title2 = soup.find_all('div', class_='floating_text_area')

    for news in news_title2:
        try:
            # Identify title
            title = news.find('h1', class_='media_feature_title').text
            hyperlink = news.find('a', class_='showimg fancybox-thumbs')
            link = url + "/" +news.a['href']
                        
        except Exception as e:
            print(e)    


    # main dictionary - add third element
    dictionary['3']={}
    dictionary['3']['link'] = link
    
    browser.quit()

    # https://galaxyfacts-mars.com
    url = 'https://galaxyfacts-mars.com'    
    
    tables = pd.read_html(url)
    
    df = tables[0]
    df.columns = df.iloc[0]
    df = df.iloc[1: , :]
    df = df.set_index('Mars - Earth Comparison')

    json_list = df.to_dict('index')

    # main dictionary - add fourth element
    dictionary['4']={}
    dictionary['4']['table'] = json_list

   ## Hemisphere 1
   # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # URL of page to be scraped
    url = 'https://marshemispheres.com/cerberus.html'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    time.sleep(8)

    # print(soup.prettify())
    # hemispheres results
    hemi_url_1= ("https://marshemispheres.com")
    cerb_1 = soup.find_all('div', class_='downloads')

    for cerb in cerb_1:
        try:
            # find link
            hyperlink = cerb.find('li')
            print(hyperlink)
            link_cerb1 = hemi_url_1 + "/" +cerb.a['href']
            print(link_cerb1)
            
        except Exception as e:
            print(e)

    browser.quit()    
   
    ## Hemisphere 2

    # Schiaparelli Hemisphere
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # URL of page to be scraped
    url = 'https://marshemispheres.com/schiaparelli.html'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    time.sleep(8)

    # print(soup.prettify())
    # Schiaparelli Hemisphereresults
    hemi_url_2 = ("https://marshemispheres.com")
    cerb_2 = soup.find_all('div', class_='downloads')

    for cerb in cerb_2:
        try:
            # find link
            hyperlink = cerb.find('li')
            print(hyperlink)
            link_cerb2 = hemi_url_2 + "/" +cerb.a['href']
            print(link_cerb2)
            
        except Exception as e:
            print(e)

    browser.quit() 

    ## Hemisphere 3

    # Syrtis Major

    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # URL of page to be scraped
    url = 'https://marshemispheres.com/syrtis.html'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    time.sleep(8)

    print(soup.prettify())

    # Syrtis Major
    # Schiaparelli Hemisphereresults
    hemi_url_3= ("https://marshemispheres.com")
    cerb_3 = soup.find_all('div', class_='downloads')

    for cerb in cerb_3:
        try:
            # find link
            hyperlink = cerb.find('li')
            print(hyperlink)
            link_cerb3 = hemi_url_3 + "/" +cerb.a['href']
            print(link_cerb3)
            
        except Exception as e:
            print(e)

    browser.quit() 

    ## Hemisphere 4
    # Valles Marineris

    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # URL of page to be scraped
    url = 'https://marshemispheres.com/valles.html'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    time.sleep(8)

    print(soup.prettify())

    # Valles Marineris Hemisphere results
 
    hemi_url_4 = ("https://marshemispheres.com")
    cerb_4 = soup.find_all('div', class_='downloads')

    for cerb in cerb_4:
        try:
            # find link
            hyperlink = cerb.find('li')
            print(hyperlink)
            link_cerb4 = hemi_url_4 + "/" +cerb.a['href']
            print(link_cerb4)
            
        except Exception as e:
            print(e)

    browser.quit() 

    # Hemisphere images

    first_image = {"title": "Cerberus Hemisphere", "img_url": link_cerb1}
    second_image = {"title": "Schiaparelli Hemisphere", "img_url": link_cerb2}
    third_image = {"title": "Syrtis Major", "img_url": link_cerb3}
    fourth_image = {"title": "Valles Marineris", "img_url": link_cerb4}

    # main dictionary - add 5-8 elements
    dictionary['5']={}
    dictionary['5']['1'] = {}
    dictionary['5']['2'] = {}
    dictionary['5']['3'] = {}
    dictionary['5']['4'] = {}
    dictionary['5']['1'] = first_image
    dictionary['5']['2'] = second_image
    dictionary['5']['3'] = third_image
    dictionary['5']['4'] = fourth_image
    
    # dictionary.pop('_id')
    # with open('troubleshooting.json', 'w') as json_file:
        # json.dump(dictionary, json_file)
    # Return results
    return dictionary
