#! /usr/bin/python

from bs4 import BeautifulSoup
from urllib import urlopen

trip_id = raw_input("Enter trip id: ")

print "Getting webpage..."
webpage = urlopen('http://tripoto.com/trips/view/'+trip_id).read()
soup = BeautifulSoup(webpage)

if soup.title.string == 'Errors':
    print "Sorry. Trip id doesn't exist."
else:
    print "Title: " + soup.find_all(class_="trip-name")[0].string
    print "Travel Agent:" + soup.find_all(class_="view-visitor-block")[0].contents[1].string
    places = []
    content = soup.find_all("ul", id="my-list")[0]
    for child in content.findChildren():
        if child.a:
            places.append(child.a.get("title"))
    print "Places: " + ", ".join(places) 
