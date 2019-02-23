from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd 


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    # executable_path = {"executable_path": "/usr/local/bin/chromedriver"} # Mac
    executable_path = {"executable_path": "chromedriver.exe"} # Windows
    return Browser("chrome", **executable_path, headless=False)
mars_data = {}
# NASA MARS NEWS
def scrape_news():
    # Initialize browser 
    browser = init_browser()

    # get news
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Find the news title and news paragraph
    title = soup.find('div', class_='content_title').find('a').text
    news = soup.find('div', class_='article_teaser_body').text


    # Dictionary entry from MARS NEWS
    mars_data["title"] = title
    mars_data["news"] = news
    
    browser.quit()
    return mars_data

# FEATURED IMAGE

def scrape_mars_image():

    # Initialize browser 
    browser = init_browser()

    # Visit Mars Space Images 
    image_url_featured = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_url_featured)# Visit Mars Space Images 

    time.sleep(1)
    # HTML Object 
    
    html_image = browser.html

    # Parse HTML with Beautiful Soup
    soup = bs(html_image, 'html.parser')

    # Retrieve background-image url from style tag 
    featured_image_url  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]

    # Website Url 
    main_url = 'https://www.jpl.nasa.gov'

    # Concatenate website url with scrapped route
    featured_image_url = main_url + featured_image_url

    # Display full link to featured image
    featured_image_url
    
    mars_data["img"] = featured_image_url
    return mars_data
    
    browser.quit()

# Mars Weather 
def scrape_mars_weather():

    # Initialize browser 
    browser = init_browser()

    # Visit Mars Weather Twitter through splinter module
    weather_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(weather_url)

    # HTML Object 
    html_weather = browser.html

    # Parse HTML with Beautiful Soup
    soup = bs(html_weather, 'html.parser')

    # Find all elements that contain tweets
    

    latest_tweets = soup.find_all('div', class_='js-tweet-text-container')


    for tweet in latest_tweets: 
            weather = tweet.find('p').text
            if 'Sol' and 'pressure' in weather:
                print(weather)
                break
            else: 
                pass

    s = weather.split("pic.")
    weather_tweet = s[0]
    mars_data['weather_tweet'] = weather_tweet
     
    return mars_data
    

    browser.quit()


    #make facts table
def scrape_mars_facts():

    # Visit Mars facts url 
    facts_url = 'http://space-facts.com/mars/'

    
    mars_facts = pd.read_html(facts_url)

    # Find the mars facts DataFrame in the list of DataFrames as assign it to `mars_df`
    mars_df = mars_facts[0]

    # Assign the columns `['Description', 'Value']`
    mars_df.columns = ['Description','Value']

    # Set the index to the `Description` column without row indexing
    #mars_df.set_index('Description', inplace=True)

    # Make html code for df
    data = mars_df.to_html()

    # Dictionary entry from MARS FACTS
    
    mars_data['mars_facts'] = data

    return mars_data

def scrape_mars_hemispheres():

    # Initialize browser 
    browser = init_browser()

    # Visit hemispheres website through splinter module 
    hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemispheres_url)

    # HTML Object
    html_hemispheres = browser.html

    # Parse HTML with Beautiful Soup
    soup = bs(html_hemispheres, 'html.parser')

    # Retreive all items that contain mars hemispheres information
    items = soup.find_all('div', class_='item')

    # Create empty list for hemisphere urls 
    hemisphere_image_urls = []

    # Store the main_ul 
    hemispheres_main_url = 'https://astrogeology.usgs.gov' 

    # Loop through the items previously stored
    for i in items: 
    # Store title
        title = i.find('h3').text
            
            # Store link that leads to full image website
        partial_img_url = i.find('a', class_='itemLink product-item')['href']
            
            # Visit the link that contains the full image website 
        browser.visit(hemispheres_main_url + partial_img_url)
            
            # HTML Object of individual hemisphere information website 
        partial_img_html = browser.html
            
            # Parse HTML with Beautiful Soup for every individual hemisphere information website 
        soup = bs( partial_img_html, 'html.parser')
            
            # Retrieve full image source 
        img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
            
            # Append the retreived information into a list of dictionaries 
        hemisphere_image_urls.append({"title" : title, "img_url" : img_url})

        mars_data['hemisphere_image_urls'] = hemisphere_image_urls

        
            # Return mars_data dictionary 

        return mars_data
    

        browser.quit()    
