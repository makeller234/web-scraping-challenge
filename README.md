# Mars Information

This repository scarpes the following website to gather information about Mars:
* [NASA Mars News Site](https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest)
    * To get the headline and introductory sentence for the latest article
* [JPL Mars Space Images](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars)
    * To get the featured image on the page
* [Mars Weather Twitter](https://twitter.com/marswxreport?lang=en)
    * To get the weather from the latest weather tweet
* [USGS Astrogeology](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)
    * To get the high resolution images of the 4 hemispheres of Mars

Jupyter notebook was used for the initial scrapping as it's quicker to see the results from the scrape. Once the code was working, it was moved to the scrap_mars.py file so that it could be made into a function to scrape all the information when the user clicks the button on the main index.html page. Scraped information is stored in MongoDB as a Python Dictionary.  This information is queried and rendered in an HTML template.

### Built With
* Web Scraping
    * Pandas
    * Splinter
    * Beautiful Soup
* App
    * Python
    * Flask
    * PyMongo
* Website
    * HTML
    * CSS/Bootstrap
