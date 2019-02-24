![](https://github.com/JoannePeel/Mission-to-mars/blob/master/Martian.jpg)

# Mission-to-Mars

Build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines what you need to do.
# Step 1 - Scraping

Using Jupyter Notebook called [mission_to_mars.ipynb](https://github.com/JoannePeel/Mission-to-mars/blob/master/mission_to_mars.ipynb), BeautifulSoup, Pandas, and Requests/Splinter, a code was developed to scrape the following information:

* Scrape [NASA Mars News Site](https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest) and collect the latest News Title and Paragraph Text.

* [JPL Featured Space Image](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars)

* [Mars Weather twitter account](https://twitter.com/marswxreport?lang=en) and scrape the latest Mars weather tweet from the page.

* Scrape the [Mars Facts webpage](https://space-facts.com/mars/) using Pandas, to scrape the table containing facts about the planet.

* [USGS Astrogeology site](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

# Step 2 - MongoDB and Flask Application

I used MongoDB with Flask templating to create a [new HTML page](https://github.com/JoannePeel/Mission-to-mars/blob/master/screen_shot_mars_mission.png) that displays all of the information that was scraped from the URLs above.

This was achieved converting the jupyter notebook into a Python script called [test.py](https://github.com/JoannePeel/Mission-to-mars/blob/master/test.py) and a PYTHON script calles [app.py](https://github.com/JoannePeel/Mission-to-mars/blob/master/app.py) with a function called _scrape_ that executes all the scraping code and returns one Python dictionary containing all of the scraped data.

Two routes were created:
* /scrape which imports  [test.py](https://github.com/JoannePeel/Mission-to-mars/blob/master/test.py) script and calls the scrape function.
* route / which queries a Mongo database and passes the mars data into an HTML template to display the data.

* Finally, a template HTML file [index.html](https://github.com/JoannePeel/Mission-to-mars/blob/master/templates/index.html) was created which takes the mars data dictionary and displays all of the data in the appropriate HTML elements. 

The final product looks as follows and data can be refreshed, clicking on the "Get Mars Data!" button.

![](https://github.com/JoannePeel/Mission-to-mars/blob/master/screen_shot_mars_mission.png)
