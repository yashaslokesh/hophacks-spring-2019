""" 
This module only needs to be run once, in order to write the html souce of the page
to a file, page.html.
It's kept here for reference

A 'chromedriver' must be installed in order to use this script
"""
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
base_url = "https://johnshopkins.campuslabs.com"
orgs_url = base_url + "/engage/organizations"
driver.get(orgs_url)

load_more_button = driver.find_element_by_css_selector("span[style='position: relative; opacity: 1; font-size: 16px; letter-spacing: 0px; text-transform: uppercase; font-weight: 500; margin: 0px; user-select: none; padding-left: 16px; padding-right: 16px; color: rgb(0, 0, 0);']")

button_id = 'LoadMore'

driver.execute_script('arguments[0].id = "LoadMore";', load_more_button)

script = """
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

var element = document.getElementById("LoadMore");

async function clicker() {
    var i;
    for (i = 0; i < 45; i++) {
        element.click();
        await sleep(500);
    }
}

clicker();
"""

driver.execute_script(script)
time.sleep(30)
html = driver.page_source

soup = BeautifulSoup(html)

with open("page.html", 'w') as f:
    f.write(soup.prettify())