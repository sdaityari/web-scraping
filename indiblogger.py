#! /usr/bin/python

from bs4 import BeautifulSoup
from urllib import urlopen

import sys    # sys.setdefaultencoding is cancelled by site.py
import operator

reload(sys)    # to re-enable sys.setdefaultencoding()
sys.setdefaultencoding('utf-8')

WEBSITE = "http://www.indiblogger.in/"

class Indiblogger() :
    
    def __init__(self, page, topic, total) :
        if page > 0:
            url = WEBSITE + 'topic.php?pageNum_ThisVine=' + str(page) + '&totalRows_ThisVine=' + str(total) + '&topic=' + str(topic) + '&sort=popular'
        else:
            url = WEBSITE + 'topic.php?topic=' + str(topic) + '&sort=popular'
        print "Getting webpage " + url
        self.webpage = urlopen(url).read()
        self.soup = BeautifulSoup(self.webpage)

    def get_links(self) :
        listings = self.soup.find_all(class_ = 'listing')
        links = []
        for item in listings :
            links.append(WEBSITE + item.a['href']) #gets the first link in item
        return links

if __name__ == '__main__' :
    topic = int(raw_input('Enter Topic ID: '))
    total = int(raw_input('Enter Total posts: '))
    pages = total // 10 + 1
    bloggers = dict()
    for i in range(pages):
        webpage = Indiblogger(i, topic, total)
        links = webpage.get_links()
        for link in links:
            if link in bloggers:
                bloggers[link] += 1
            else:
                bloggers[link] = 1
    print max(bloggers.iteritems(), key=operator.itemgetter(1))[0]
