# hophacks-spring-2019

****************
Contributors:
Egzona Rexhepi, 
Yashas Lokesh,
Christopher Xu
****************

OVERVIEW:
 	
 	Orient is a web app that acts as a virtual counselor chatbot for students who are new to a college. The app's flagship feature is the clubs and organizations page, which requires a parser to customize search results for each school. The page also implements filter abilities. Additionally, the application assists students with time management skills to alleviate academic stresses using a personal digital assistant.

INCLUDED FILES:

	README.md - this file
	main.py - the final flask app
	clubs.db - a database of organizations accessed through the parser
	forms.py - filtering abilities for the clubs and organizations page
	jhu-orgs-html-getter.py - the parser for a clubs and organizations page using Selenium
	orgs-parser - creates a database using the aforementioned parser


PROGRAM DESIGN AND IMPORTANT CONCEPTS:


	The club information was gathered by a python parser that we built with Beautiful Soup and Selenium and ran it on https://johnshopkins.campuslabs.com/engage/organizations. The parser stored the data into a SQL lite database. We then built a website using HTML, CSS, Javascript and Flask and integrated the database into the website. Finally, the calculator was built using HTML input components and javascript and the chatbot was created using DialogFlow.


DISCUSSION:
 
	Our biggest issue when creating this project was training the chatbot. Originally, we were planning to build a chatbot using Python and NLTK or Chatterbot. After a few hours we realized that building a chatbot oriented webapp was unfeasible and had to re-evaluate our goals and refocus our project.