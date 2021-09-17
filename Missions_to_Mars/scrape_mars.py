
# Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


def scrape():
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
    # print(soup.prettify())

    # redplanet results
    news_title = soup.find('div', class_='content_title').text
    # print(news_title)
    news_p = soup.find('div', class_='article_teaser_body').text
    # print(news_p)
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
    # print(soup.prettify())

    # https://spaceimages-mars.com/image/featured/mars3.jpg

    # redplanet results

    news_title = soup.find_all('div', class_='floating_text_area')
    print(news_title)


    for news in news_title:
        try:
            # Identify title
            title = news.find('h1', class_='media_feature_title').text
            print(f"title: {title}")
            hyperlink = news.find('a', class_='showimg fancybox-thumbs')
            print(f"link 1: {hyperlink}")
            
            link = url + "/" +news.a['href']
            print(link)
            # print(f"link:{url}/{link}")
        except Exception as e:
            print(e)

    browser.quit()

    # https://galaxyfacts-mars.com
    url = 'https://galaxyfacts-mars.com'    
    
    tables = pd.read_html(url)
    df = tables[1]
    df.style.hide_index()
    # df.head()

    # instructions from https://www.geeksforgeeks.org/how-to-render-pandas-dataframe-as-html-table/
    html = df.to_html(index=False, header=False)
    print(html)
    text_file = open("mars.html", "w")
    text_file.write(html)
    text_file.close()

    first_image = {"title": "Cerberus Hemisphere", "img_url": "https://marshemispheres.com/images/cerberus_enhanced.tif"}
    second_image = {"title": "Schiaparelli Hemisphere", "img_url": "https://marshemispheres.com/images/schiaparelli_enhanced.tif"}
    third_image = {"title": "Syrtis Major", "img_url": "https://marshemispheres.com/images/syrtis_major_enhanced.tif"}
    fourth_image = {"title": "Valles Marineris", "img_url": "https://marshemispheres.com/images/valles_marineris_enhanced.tif"}

    hemisphere_image_urls = []

    first_image_copy = first_image.copy()
    hemisphere_image_urls.append(first_image_copy)

    second_image_copy = second_image.copy()
    hemisphere_image_urls.append(second_image_copy)

    third_image_copy = third_image.copy()
    hemisphere_image_urls.append(third_image_copy)

    fourth_image_copy = fourth_image.copy()
    hemisphere_image_urls.append(fourth_image_copy)

    print(hemisphere_image_urls)

    # Initialize PyMongo to work with MongoDBs
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)

    
    # Define database and collection
    db = client.mars_db
    collection = db.webitems