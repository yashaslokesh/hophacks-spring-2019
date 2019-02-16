""" This script needs only be run once each time the web page source is re generated.
This script will create an SQLite database
"""

from bs4 import BeautifulSoup
import sqlite3

def club_info_generator():
    # All org/club websites are based off this base url
    base_url = "https://johnshopkins.campuslabs.com"
    # The html file with the page source. Extracted with the 'jhu-orgs-html-getter' module
    html_file = 'page.html'

    # Create BeautifulSoup object
    with open(html_file) as f:
        soup = BeautifulSoup(f.read(), features='html.parser')

    # Get all links in the page. Each link corresponds to another website
    links = soup.find_all('a', style='display: block; text-decoration: none; margin-bottom: 20px;')

    for link in links:
        # Each 'link' is just a <a></a> tag with some extra goodies inside.
        url_addon = link['href']
        final_url = base_url + url_addon
        # Name of organization, accesses the innermost div which has the name
        print()
        name = link.div.div.div.div.div.div.contents[0].strip()
        # This condition is only true if a organization does not have an image, and has a 
        # letter in the image spot instead. This causes us to find that single letter instead
        # of the organization's full name
        if len(name) == 1:
            name = link.div.div.div.div.select('div > div')[2].contents[0].strip()
        print(name)
        print()
        descr = link.find('p').contents[0].strip()

        yield name, final_url, descr

def create_and_populate_database():
    conn = sqlite3.connect('clubs.db')
    curs = conn.cursor()
    curs.execute("CREATE TABLE clubs (name text, url text, descr text)")

    for name, url, descr in club_info_generator():
        curs.execute("INSERT INTO clubs VALUES (?, ?, ?)", (name, url, descr,))
        # print()
        # print(name)
        # print(url)
        # print(descr)
        # print()
        conn.commit()

    conn.close()

create_and_populate_database()