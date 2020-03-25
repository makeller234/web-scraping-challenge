## Step 1: Gathering Information

### NASA Mars News
* Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

### JPL Mars Space Images - Featured Image
* Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.

### Mars Weather
* Visit the Mars Weather twitter account here and scrape the latest Mars weather tweet from the page. Save the tweet text for the weather report as a variable called mars_weather.

### Mars Facts
* Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
* Use Pandas to convert the data to a HTML table string.

### Mars Hemispheres
* Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
* You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
* Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.

## Step 2: MongoDB and Flask Application
* Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.
* Convert jupyternotebook to python so that it can be used for Flask templating
* Create a route called /scrape that will import your scrape_mars.py script and call your scrape function and store the return value in Mongo as a Python dictionary.
* Create a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.
* Create a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements.
