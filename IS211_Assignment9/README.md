# IS211_Assignment9
IS211_Assignment9

Up until this week, we have focused on building up some of your practical skills with Python, including using common modules, processing text and unit testing. We have also focused on some more abstract knowledge, like best OOP design practices and design patterns.  We will take a different approach in the second half of this course, focusing on learning how to build a very simple Python-based web backend. Being comfortable with web technologies, and understanding how to build useful services with them is something most programmers need to be skilled in. Our intention is to give you a some understanding of all the layers in what people call the ‘web stack’. This week, we will be starting off by learning some of the basic technologies that form the basis of the web, and how we can use them in Python.

Required Content: Reading
Please read the lecture notes for links to all the readings. Here is a list for reference:
HTTP: The Protocol Every Web Developer Must Know - Part 1
http://code.tutsplus.com/tutorials/http-the-protocol-every-web-developer-must-know-part-1--net-31177
HTML Beginner's Guide
http://htmldog.com/guides/html/beginner/
CSS Beginner's Guide
http://htmldog.com/guides/css/beginner/
Intro to BeautifulSoup
https://programminghistorian.org/en/lessons/intro-to-beautiful-soup
Understanding JSON
http://code.tutsplus.com/tutorials/understanding-json--active-8817
json Module
http://pymotw.com/2/json/
Tutorials:
https://www.digitalocean.com/community/tutorials/how-to-scrape-web-pages-with-beautiful-soup-and-python-3
https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/
Item
Optional Content: Reading
Here is a list of links that should elaborate on all the topics covered this week:
HTTP Status Codes - An official listing of HTTP status codes and what they mean
http://en.wikipedia.org/wiki/List_of_HTTP_status_codes
HTML cheat sheet - Listing of most common tags
http://www.simplehtmlguide.com/cheatsheet.php
W3CSchool's Tutorial on HTML - Another beginners guide to HTML
http://www.w3schools.com/html/default.asp
BeautifulSoup's documentation - which is a good rundown of the available options as well as a nice tutorial on how BeautifulSoup works
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
Another good reference on what is available from BeautifulSoup
http://omz-software.com/editorial/docs/ios/beautifulsoup_ref.html

Optional Content: Useful Links
Here is a listing of some great tools that can help you understand HTTP and other web technologies we learned this week:
Chrome Browser Developer Tools - Use it to find the elements you need.
https://developers.google.com/web/tools/chrome-devtools/dom
Firefox Web Developer Inspector - Same as above but for Firefox
https://developer.mozilla.org/en-US/docs/Tools/Page_Inspector/How_to/Open_the_Inspector
Firebug - Firefox extension that can show you live HTTP information for web pages you are loading
http://getfirebug.com/
cURL - Command line program for accessing URLs and inspecting HTTP headers
http://curl.haxx.se/
Speaking of cURL, you can use the examples at httpbin.org to see how to use cURL and JSON

Week 9 Assignment
Write two scripts (2) that will scrape data from the web and printed their content to the screen. Here are some examples:

CBS Football Stats

Go to the CBS NFL Stats webpage, located here
http://www.cbssports.com/nfl/stats
For this example, lets look at the league leaders in any category, for example Scoring.
Change the drop down to regular. This should be the URL https://www.cbssports.com/nfl/stats/player/scoring/nfl/regular/qualifiers/
Write a script called “football_stats.py” that will load this URL, parse it using BeautiulSoup, andoutput the list of top 20 players, including the player’s position, team and total number oftouchdowns

Stock Data

Another important task in the real world is to download stock data for future analysis. There are manyservices that you can get this kind of data from in a convenient format, but many of these services are forpay. We can do better! For this part of the assignment, we’ll scrape stock data for Apple from Yahoo.
To get data about Apple’s stock, we’ll use Yahoo Finance, located at https://finance.yahoo.com/quote/AAPL/history?p=AAPL
To get Apple Historical Prices, you can go right into https://finance.yahoo.com/quote/AAPL/history?p=AAPL.
Write a script called “apple_stock.py” that will load this URL, parse it using BeautifulSoup, and output the close price and date for all the dates shown on the page

Wikipedia

Go To Wikipedia and scrape any table that you might find useful. For Example:
List of Superbowl Champions https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions
List of World Series Champions https://en.wikipedia.org/wiki/List_of_World_Series_champions
Any other table you find of interest
You can pick any two websites that you want to scrape data from if you find some interesting datasource of your own. Please include the link in your script.
You only need to submit two scripts. Make sure to include the link you are scraping in a comment in your script.
