#! /usr/bin/python

from bs4 import BeautifulSoup
from urllib import urlopen

class TripotoTrip():
    
    def __init__(self, trip_id):
        print "Getting webpage..."
        self.webpage = urlopen('http://tripoto.com/trips/view/'+trip_id).read()
        self.soup = BeautifulSoup(self.webpage)
    
    def check_errors(self):
        if self.soup.title.string == 'Errors' :
            return True
        else :
            return False
    
    def __str__(self):
        soup = self.soup
        string = "Title: " + soup.find(class_="trip-name").string + "\n"
        string += "Travel Agent: " + soup.find(class_="view-visitor-block").contents[1].string + "\n"
        places = []
        content = soup.find("ul", id="my-list")
        for child in content.findChildren():
            if child.a:
                try:
                    places.append(child.a.get("title").decode("utf-8"))
                except:
                    places.append(" ")
        string += "Places: " + ", ".join(places)
        return string

if __name__ == '__main__':
    trip_id = raw_input("Enter trip id: ")
    trip = TripotoTrip(trip_id)
    if trip.check_errors():
        print "Sorry. Trip id doesn't exist."
    else:
        print (trip)
