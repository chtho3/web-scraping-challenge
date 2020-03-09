#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Dependencies
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
import requests
import pymongo


# In[2]:


# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)


# Define database and collection
db = client.news_db
collection = db.items


# In[3]:


mars_url= "https://mars.nasa.gov/news/"
jpl_url= "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[4]:


browser.visit(mars_url)


# In[6]:


# MARS NEWS DATA SCRAPING
html = browser.html
mars_soup = BeautifulSoup(html, 'html.parser')

try:
    # Identify and return title of post
    news_title = mars_soup.find('div', class_='list_text').find('a').text
    # Identify and return paragraph text
    news_p = mars_soup.find('div', class_='article_teaser_body').text

    # Run only if title, price, and link are available
    if (news_title and news_p):
        # Print results
        print(news_title)
        print(news_p)

        # Dictionary to be inserted as a MongoDB document
        post = {
            'title': news_title,
            'price': news_p
        }

        collection.insert_one(post)

except Exception as e:
    print(e)


# In[7]:


# Navigate chromedriver to jpl_url
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
browser.visit(jpl_url)


# In[8]:


#JPL DATA IMG SCRAPING
html = browser.html
jpl_soup = BeautifulSoup(html, 'html.parser')
intro_url="https://www.jpl.nasa.gov"

try:
    # Identify and return title of post
    featured_image_url = jpl_soup.find('div', class_="img").img['src']
    
    # Run only if title, price, and link are available
    if (featured_image_url):
        # Print results
        print(intro_url + featured_image_url)

        # Dictionary to be inserted as a MongoDB document
        post = {
            'featured_image_url': intro_url + featured_image_url        }

        collection.insert_one(post)

except Exception as e:
    print(e)


# In[9]:


#MARS WEATHER
twit_url='https://twitter.com/marswxreport?lang=en'

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
browser.visit(twit_url)


# In[10]:


html = browser.html
twit_soup = BeautifulSoup(html, 'html.parser')

#Scrape Twitter
try:
    # Identify and return weather
    mars_weather = twit_soup.find('div', class_="css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0").text
    
    # Run only if available
    if (mars_weather):
        # Print results
        print(mars_weather)

        # Dictionary to be inserted as a MongoDB document
        post = {
            'mars_weather': mars_weather       }

        collection.insert_one(post)

except Exception as e:
    print(e)


# In[11]:


#MARS FACTS
facts_url = "https://space-facts.com/mars/"

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
browser.visit(facts_url)


# In[12]:


html = browser.html
table_soup = BeautifulSoup(html, 'html.parser')

#Scrape Stats
try:
    # Identify and return weather
    mars_stats = table_soup.find('table', class_="tablepress tablepress-id-p-mars").find('tbody')
    # Run only if available
    if (mars_stats):
        # Print results
        print(mars_stats)

        # Dictionary to be inserted as a MongoDB document
        post = {
            'mars_facts_html': mars_stats       }

        collection.insert_one(post)

except Exception as e:
    print(e)


# In[13]:


#MARS HEMISPHERES (img 1)
usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
browser.visit(usgs_url)


# In[14]:


html = browser.html
usgs_soup = BeautifulSoup(html, 'html.parser')
usgs_prefix = "https://astrogeology.usgs.gov"

hemi_1 = usgs_soup.find('div', class_='description').find('a').text
results_get = usgs_soup.find('div', class_='description').find('a')['href']
print(hemi_1)

results_url = usgs_prefix + results_get

browser.visit(results_url)
html = browser.html
usgs_soup_1 = BeautifulSoup(html, 'html.parser')

usgs_img_1 = usgs_soup_1.find('div', class_='downloads').find('a')['href']
print(usgs_img_1)


# In[18]:


#MARS HEMISPHERES (img 2)
usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
browser.visit(usgs_url)


# In[19]:


html = browser.html
usgs_soup = BeautifulSoup(html, 'html.parser')
usgs_prefix = "https://astrogeology.usgs.gov"

hemi_2 = usgs_soup.find_all('div', class_='description')[1].find('a').text
results_get = usgs_soup.find_all('div', class_='description')[1].find('a')['href']
print(results_get)

results_url = usgs_prefix + results_get

browser.visit(results_url)
html = browser.html
usgs_soup_2 = BeautifulSoup(html, 'html.parser')

usgs_img_2 = usgs_soup_2.find('div', class_='downloads').find('a')['href']
print(usgs_img_2)


# In[20]:


#MARS HEMISPHERES (img 3)
usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
browser.visit(usgs_url)


# In[21]:


html = browser.html
usgs_soup = BeautifulSoup(html, 'html.parser')
usgs_prefix = "https://astrogeology.usgs.gov"

hemi_3 = usgs_soup.find_all('div', class_='description')[2].find('a').text
results_get = usgs_soup.find_all('div', class_='description')[2].find('a')['href']
print(results_get)

results_url = usgs_prefix + results_get

browser.visit(results_url)
html = browser.html
usgs_soup_3 = BeautifulSoup(html, 'html.parser')

usgs_img_3 = usgs_soup_3.find('div', class_='downloads').find('a')['href']
print(usgs_img_3)


# In[22]:


#MARS HEMISPHERES (img 4)
usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
browser.visit(usgs_url)


# In[23]:


html = browser.html
usgs_soup = BeautifulSoup(html, 'html.parser')
usgs_prefix = "https://astrogeology.usgs.gov"

hemi_4 = usgs_soup.find_all('div', class_='description')[3].find('a').text
results_get = usgs_soup.find_all('div', class_='description')[3].find('a')['href']
print(results_get)

results_url = usgs_prefix + results_get

browser.visit(results_url)
html = browser.html
usgs_soup_4 = BeautifulSoup(html, 'html.parser')

usgs_img_4 = usgs_soup_4.find('div', class_='downloads').find('a')['href']
print(usgs_img_4)


# In[29]:


# Add to collection
if (usgs_img_1 and usgs_img_2 and usgs_img_3 and usgs_img_4):
    # Print results
    print(hemi_1)
    print(hemi_2)
    print(hemi_3)
    print(hemi_4)
    print(usgs_img_1)
    print(usgs_img_2)
    print(usgs_img_3)
    print(usgs_img_4)

    # Dictionary to be inserted as a MongoDB document
    hemisphere_image_urls = [
    {"title": hemi_1, "img_url": usgs_img_1},
    {"title": hemi_2, "img_url": usgs_img_2},
    {"title": hemi_3, "img_url": usgs_img_3},
    {"title": hemi_4, "img_url": usgs_img_4}
    ]


    collection.insert_many(hemisphere_image_urls)


# In[7]:


# Convert this jupyter notebook file to a python script
# ! jupyter nbconvert --to python --output scrape_mars.py


# In[ ]:




