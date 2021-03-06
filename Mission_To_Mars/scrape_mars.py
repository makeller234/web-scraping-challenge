import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests

def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():

    browser = init_browser()

    mars_deets = {}

    # find article title and paragraph info
    articleURL = "https://mars.nasa.gov/news"
    browser.visit(articleURL)
    html = browser.html
    soup = bs(html, "html.parser")
    x = 0
    while x == 0:
        try:
            articleTitle = soup.find("div", class_="list_text")
            title = articleTitle.find('div', class_="content_title")
            news_title = title.text
            x = 1
        except AttributeError:
            x = 0
 
    # in the .ipynb I needed to have another x = 1 outside the loop to make it stop, but here that doesn't seem to be necessary
    # still seems a little spotty on weather (pun intended) it works on the first try, but it ususally works on the first try here in the .py 
        
    news_p = soup.find('div', class_='article_teaser_body').text

    mars_deets["title"] = news_title
    mars_deets["news"] = news_p


    # mars feature image
    marsURL = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    browser.visit(marsURL)
    marsHTML = browser.html
    marsSoup = bs(marsHTML, "html.parser")


    featureImage = marsSoup.find('article')

    close = featureImage.find('footer')
    gettingCloser = close.find('a')
    bingo = gettingCloser['data-fancybox-href']

    featured_image_url = "https://www.jpl.nasa.gov" + bingo

    mars_deets["featured_image"] = featured_image_url

    # mars twitter weather
    weatherURL = "https://twitter.com/marswxreport?lang=en"

    weatherResponse = requests.get(weatherURL)
    weatherSoup = bs(weatherResponse.text, 'html.parser')

    weatherTweets = weatherSoup.find_all('div', class_="js-tweet-text-container")

    for tweet in weatherTweets:
        mars_weather = tweet.find('p').text
        if "InSight" and "sol" in mars_weather:
            mars_deets["weather"]=mars_weather
            break
        else:
            pass


    # mars facts
    tableURL = "https://space-facts.com/mars/"

    table = pd.read_html(tableURL)
    information = table[0]
    marsFacts = information.to_html(header=False, index=False)

    mars_deets["facts"] = marsFacts

    # hemispheres
    hemisphere_image_urls = []
    imageBeginURL = "https://astrogeology.usgs.gov"

    cerberusURL = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
    browser.visit(cerberusURL)
    cerberusHTML = browser.html
    cerberusSoup = bs(cerberusHTML, "html.parser")

    cerberusImage = cerberusSoup.find('img', class_="wide-image")
    hemisphere_image_urls.append({"title":"Cerberus Hemisphere", "URL": imageBeginURL + cerberusImage['src']})


    schiaparelliURL = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
    browser.visit(schiaparelliURL)
    schiaparelliHTML = browser.html
    schiaparelliSoup = bs(schiaparelliHTML, 'html.parser')

    schiaparelliImage = schiaparelliSoup.find('img', class_="wide-image")
    schiaparelliImage['src']

    hemisphere_image_urls.append({"title": "Schiaparelli Hemisphere", "URL": imageBeginURL + schiaparelliImage['src']})


    syrtismajorURL = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
    browser.visit(syrtismajorURL)
    syrtismajorHTML = browser.html
    syrtismajorSoup = bs(syrtismajorHTML, 'html.parser')

    syrtismajorImage = syrtismajorSoup.find('img', class_="wide-image")
    hemisphere_image_urls.append({"title": "Syrtis Major Hemisphere", "URL": imageBeginURL + syrtismajorImage['src']})


    vallesmarinerisURL = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
    browser.visit(vallesmarinerisURL)
    vallesmarinerisHTML = browser.html
    vallesmarinerisSoup = bs(vallesmarinerisHTML, 'html.parser')

    vallesmarinerisImage = vallesmarinerisSoup.find('img', class_="wide-image")
    hemisphere_image_urls.append({"title": "Valles Marineris Hemisphere", "URL": imageBeginURL +vallesmarinerisImage['src']})

    mars_deets["hemisphere_images"] = hemisphere_image_urls

    browser.quit()
    # print(mars_deets)
    return mars_deets