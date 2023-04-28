

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# The Instagram account link you want to scrape
url = 'https://www.instagram.com/artistpng/'

# Start the WebDriver and navigate to the page
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get(url)

# Find the profile name
profile_name_element = driver.find_element('css selector', 'rhpdm')
profile_name = profile_name_element.text


# Find the username
username_element = driver.find_element_by_xpath('//a[contains(@class, "sqdOP yWX7d") and contains(@class, "_8A5w5") and contains(@class, "ZIAjV ")]')
username = username_element.text

# Find the bio
bio_element = driver.find_element_by_xpath('//div[@class="-vDIg"]//span')
bio = bio_element.text

# Find the followers count
followers_element = driver.find_element_by_xpath('//span[@class="g47SY "]')
followers = followers_element.get_attribute('title')

# Find the following count
following_elements = driver.find_elements_by_xpath('//span[@class="g47SY "]')
following = following_elements[1].get_attribute('title')

# Find the posts count
posts = following_elements[0].get_attribute('title')

# Quit the WebDriver
driver.quit()

# Print the results
print('Profile Name:', profile_name)
print('Username:', username)
print('Bio:', bio)
print('Followers:', followers)
print('Following:', following)
print('Posts:', posts)

