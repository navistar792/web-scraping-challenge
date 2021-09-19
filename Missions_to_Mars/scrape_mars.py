
# Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import json

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
    
    df = tables[1]
    df = df.rename(columns={0:'metric',1:'value'})
    df = df.set_index('metric')

    json_list = df.to_dict('index')

    # main dictionary - add fourth element
    dictionary['4']={}
    dictionary['4']['table'] = json_list

    # Hemisphere images

    first_image = {"title": "Cerberus Hemisphere", "img_url": "https://marshemispheres.com/images/cerberus_enhanced.tif"}
    second_image = {"title": "Schiaparelli Hemisphere", "img_url": "https://marshemispheres.com/images/schiaparelli_enhanced.tif"}
    third_image = {"title": "Syrtis Major", "img_url": "https://marshemispheres.com/images/syrtis_major_enhanced.tif"}
    fourth_image = {"title": "Valles Marineris", "img_url": "https://marshemispheres.com/images/valles_marineris_enhanced.tif"}

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
