import pandas as pd
import requests
from splinter import Browser
from bs4 import BeautifulSoup

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars_data = {}

    # nasa mars news site
    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)
    #parse with BeautifulSoup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    #extract article title and text
    article = soup.find('div', class_='list_text')
    news_title = article.find('div', class_='content_title').text
    news_p = article.find('div', class_='article_teaser_body').text

    # jpl mars space images
    images_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(images_url)
    #expand full size image
    fullsize = browser.find_by_id("full_image")
    fullsize.click()
    #expand more info
    browser.is_element_present_by_text("more info", wait_time=1)
    moreinfo = browser.find_link_by_partial_text("more info")
    moreinfo.click()
    #parse with BeautifulSoup
    html_image = browser.html
    soup = BeautifulSoup(html_image, 'html.parser')
    featured_image_url = soup.select_one("figure.lede a img").get("src")
    #combine base url with image url
    featured_image_url = f"https://www.jpl.nasa.gov{featured_image_url}"

    # mars weather
    weather_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(weather_url)
    #use requests library to get tweet
    response = requests.get(weather_url)
    soup = BeautifulSoup(response.text, 'lxml')
    mars_weather = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text.strip()

    # mars facts
    facts_url = "https://space-facts.com/mars/"
    browser.visit(facts_url)
    html_url = browser.html
    #retieve first table
    mars_df = pd.read_html(facts_url)[0]
    #rename columns and set index
    mars_df.columns=["Description", "Value"]
    mars_df.set_index("Description", inplace=True)
    #convert table to html string
    mars_df.to_html('table.html')

    # mars hemispheres
    hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemispheres_url)
    html_hemispheres = browser.html
    soup = BeautifulSoup(html_hemispheres, "html.parser")
    #empty list for hemisphere image urls
    hemisphere_image_urls = []
    results = soup.find("div", class_ = "results" )
    images = results.find_all("div", class_="item")
    #looping through hemisphere images to extract urls abd titles
    for image in images:
        title = image.find("h3").text
        title = title.replace("Enhanced", "")
        endlink = image.find("a")["href"]
        img_url = "https://astrogeology.usgs.gov/" + endlink
        browser.visit(img_url)
        html_links = browser.html
        soup = BeautifulSoup(html_links, "html.parser")
        downloads = soup.find("div", class_="downloads")
        img_url = downloads.find("a")["href"]
        hemisphere_image_urls.append({"title": title, "img_url": img_url})

    # Store data in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_weather": mars_weather,
        "mars_df": mars_df,
        "hemisphere_image_urls": hemisphere_image_urls
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data


if __name__ == '__main__':
    scrape()
