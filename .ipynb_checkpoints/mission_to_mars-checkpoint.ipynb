{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 211,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import requests\n",
    "\n",
    "from splinter import Browser\n",
    "from selenium import webdriver\n",
    "from bs4 import BeautifulSoup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 212,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "/usr/local/bin/chromedriver\r\n"
     ]
    }
   ],
   "source": [
    "!which chromedriver"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 213,
   "metadata": {},
   "outputs": [],
   "source": [
    "#set executable path\n",
    "\n",
    "executable_path = {'executable_path': '/usr/local/bin/chromedriver'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# nasa mars news site\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 214,
   "metadata": {},
   "outputs": [],
   "source": [
    "news_url = \"https://mars.nasa.gov/news/\"\n",
    "browser.visit(news_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 215,
   "metadata": {},
   "outputs": [],
   "source": [
    "#parse with BeautifulSoup\n",
    "html = browser.html\n",
    "soup = BeautifulSoup(html, \"html.parser\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 216,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "NASA's Perseverance Mars Rover Gets Its Wheels and Air Brakes\n",
      "After the rover was shipped from JPL to Kennedy Space Center, the team is getting closer to finalizing the spacecraft for launch later this summer.\n"
     ]
    }
   ],
   "source": [
    "#extract article title and text\n",
    "article = soup.find('div', class_='list_text')\n",
    "news_title = article.find('div', class_='content_title').text\n",
    "news_p = article.find('div', class_='article_teaser_body').text\n",
    "\n",
    "print(news_title)\n",
    "print(news_p)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# jpl mars space images"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 217,
   "metadata": {},
   "outputs": [],
   "source": [
    "images_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "browser.visit(images_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 218,
   "metadata": {},
   "outputs": [],
   "source": [
    "#expand full size image\n",
    "fullsize = browser.find_by_id(\"full_image\")\n",
    "fullsize.click()\n",
    "\n",
    "#expand more info\n",
    "browser.is_element_present_by_text(\"more info\", wait_time=1)\n",
    "moreinfo = browser.find_link_by_partial_text(\"more info\")\n",
    "moreinfo.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 219,
   "metadata": {},
   "outputs": [],
   "source": [
    "#parse with BeautifulSoup\n",
    "\n",
    "html_image = browser.html\n",
    "soup = BeautifulSoup(html_image, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 220,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'/spaceimages/images/largesize/PIA19083_hires.jpg'"
      ]
     },
     "execution_count": 220,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "featured_image_url = soup.select_one(\"figure.lede a img\").get(\"src\")\n",
    "featured_image_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 221,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://www.jpl.nasa.govhttp://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg\n"
     ]
    }
   ],
   "source": [
    "#combine base url with image url\n",
    "featured_image_url = f\"https://www.jpl.nasa.gov{img_url}\"\n",
    "print(featured_image_url)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# mars weather"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 222,
   "metadata": {},
   "outputs": [],
   "source": [
    "weather_url = 'https://twitter.com/marswxreport?lang=en'\n",
    "browser.visit(weather_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 223,
   "metadata": {},
   "outputs": [],
   "source": [
    "#use requests library to get tweet\n",
    "response = requests.get(weather_url)\n",
    "soup = BeautifulSoup(response.text, 'lxml')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 224,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "InSight sol 480 (2020-04-02) low -93.0ºC (-135.5ºF) high -6.7ºC (19.9ºF)\n",
      "winds from the SW at 5.8 m/s (13.1 mph) gusting to 17.2 m/s (38.5 mph)\n",
      "pressure at 6.50 hPapic.twitter.com/8oUTHBmcXp\n"
     ]
    }
   ],
   "source": [
    "mars_weather = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text.strip()\n",
    "print(mars_weather)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# mars facts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 225,
   "metadata": {},
   "outputs": [],
   "source": [
    "facts_url = \"https://space-facts.com/mars/\"\n",
    "browser.visit(facts_url)\n",
    "html_url = browser.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 226,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Equatorial Diameter:</td>\n",
       "      <td>6,792 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Polar Diameter:</td>\n",
       "      <td>6,752 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Moons:</td>\n",
       "      <td>2 (Phobos &amp; Deimos)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Orbit Distance:</td>\n",
       "      <td>227,943,824 km (1.38 AU)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Orbit Period:</td>\n",
       "      <td>687 days (1.9 years)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Surface Temperature:</td>\n",
       "      <td>-87 to -5 °C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>First Record:</td>\n",
       "      <td>2nd millennium BC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Recorded By:</td>\n",
       "      <td>Egyptian astronomers</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                      0                              1\n",
       "0  Equatorial Diameter:                       6,792 km\n",
       "1       Polar Diameter:                       6,752 km\n",
       "2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       "3                Moons:            2 (Phobos & Deimos)\n",
       "4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       "5         Orbit Period:           687 days (1.9 years)\n",
       "6  Surface Temperature:                   -87 to -5 °C\n",
       "7         First Record:              2nd millennium BC\n",
       "8          Recorded By:           Egyptian astronomers"
      ]
     },
     "execution_count": 226,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#retieve first table\n",
    "mars_df = pd.read_html(facts_url)[0]\n",
    "mars_df\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 227,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Value</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Description</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Equatorial Diameter:</th>\n",
       "      <td>6,792 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Polar Diameter:</th>\n",
       "      <td>6,752 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mass:</th>\n",
       "      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Moons:</th>\n",
       "      <td>2 (Phobos &amp; Deimos)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Orbit Distance:</th>\n",
       "      <td>227,943,824 km (1.38 AU)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Orbit Period:</th>\n",
       "      <td>687 days (1.9 years)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Surface Temperature:</th>\n",
       "      <td>-87 to -5 °C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>First Record:</th>\n",
       "      <td>2nd millennium BC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Recorded By:</th>\n",
       "      <td>Egyptian astronomers</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                              Value\n",
       "Description                                        \n",
       "Equatorial Diameter:                       6,792 km\n",
       "Polar Diameter:                            6,752 km\n",
       "Mass:                 6.39 × 10^23 kg (0.11 Earths)\n",
       "Moons:                          2 (Phobos & Deimos)\n",
       "Orbit Distance:            227,943,824 km (1.38 AU)\n",
       "Orbit Period:                  687 days (1.9 years)\n",
       "Surface Temperature:                   -87 to -5 °C\n",
       "First Record:                     2nd millennium BC\n",
       "Recorded By:                   Egyptian astronomers"
      ]
     },
     "execution_count": 227,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#rename columns and set index\n",
    "mars_df.columns=[\"Description\", \"Value\"]\n",
    "mars_df.set_index(\"Description\", inplace=True)\n",
    "mars_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 228,
   "metadata": {},
   "outputs": [],
   "source": [
    "#convert table to html string\n",
    "mars_df.to_html('table.html')\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# mars hemispheres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 229,
   "metadata": {},
   "outputs": [],
   "source": [
    "hemispheres_url = \"https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\"\n",
    "browser.visit(hemispheres_url)\n",
    "html_hemispheres = browser.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 230,
   "metadata": {},
   "outputs": [],
   "source": [
    "soup = BeautifulSoup(html_hemispheres, \"html.parser\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 231,
   "metadata": {},
   "outputs": [],
   "source": [
    "#empty list for hemisphere image urls\n",
    "hemisphere_image_urls = []\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 232,
   "metadata": {},
   "outputs": [],
   "source": [
    "results = soup.find(\"div\", class_ = \"results\" )\n",
    "\n",
    "images = results.find_all(\"div\", class_=\"item\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 233,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[{'title': 'Cerberus Hemisphere ', 'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'}, {'title': 'Schiaparelli Hemisphere ', 'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'}, {'title': 'Syrtis Major Hemisphere ', 'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'}, {'title': 'Valles Marineris Hemisphere ', 'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'}]\n"
     ]
    }
   ],
   "source": [
    "#looping through hemisphere images to extract urls abd titles\n",
    "\n",
    "for image in images:\n",
    "    title = image.find(\"h3\").text\n",
    "    title = title.replace(\"Enhanced\", \"\")\n",
    "    endlink = image.find(\"a\")[\"href\"]\n",
    "    img_url = \"https://astrogeology.usgs.gov/\" + endlink\n",
    "    \n",
    "    browser.visit(img_url)\n",
    "    html_links = browser.html\n",
    "    soup = BeautifulSoup(html_links, \"html.parser\")\n",
    "    downloads = soup.find(\"div\", class_=\"downloads\")\n",
    "    img_url = downloads.find(\"a\")[\"href\"]\n",
    "    hemisphere_image_urls.append({\"title\": title, \"img_url\": img_url})\n",
    "\n",
    "print(hemisphere_image_urls)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
