Yet another thing I came up with because I was lazy! Here's how to run it.
Note: Do not use it for commercial purposes.

###Install dependencies:
>sudo apt-get install python-bs4

#####Alternate installation:
>sudo apt-get install python-pip   
>sudo pip install beautifulsoup4

###Clone the repository:
>git clone https://github.com/sdaityari/web-scraping

##Tools
#####trpt.py
Prints out trip information about a trip in tripoto. Takes in trip id as input.

>azure@ubuntu:~/web-scraping$ python trpt.py  
>Enter trip id: 273  
>Getting webpage...  
>Title: The Handicraft Tour  
>Travel Agent: Royal Tours India  
>Places: New Delhi, Agra, Jaipur, Jodhpur, Udaipur  

#####bootsnall.py
Gets information about all world travelers from travelers.bootsnall.com and saves it in an xls file!

#####fb_page_feed_check.php
Run it in your web browser. Fill in the arrays of misleading words and terms to check for in the feed. Also put it the fb page id.

#####indiblogger.py
Gets the highest no of posts by any blogger in a given contest
