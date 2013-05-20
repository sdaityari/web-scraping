#! /usr/bin/python

from bs4 import BeautifulSoup
from urllib import urlopen

import xlwt

def make_file(headers, data):
    workbook = xlwt.Workbook(encoding = 'ascii')
    worksheet = workbook.add_sheet('Details')
    col = 1
    row = 0
    worksheet.write(0, 0, label = 'Sno')
    for header in headers:
        worksheet.write(row, col, label = header)
        col += 1
    row = 1
    for x in data:
        worksheet.write(row, 0, label = row)
        worksheet.write(row, 1, label = x['title'])
        worksheet.write(row, 2, label = x['header'])
        worksheet.write(row, 3, label = x['details'])
        worksheet.write(row, 4, label = x['links'])
        row += 1
    workbook.save('data-bootsnall.xls')

class BootsnallPage():
    
    def __init__(self, page):
        print "Getting page " + str(page) + " ..."
        if page == '1':
            page = ''
            self.webpage = urlopen('http://travelers.bootsnall.com/').read()
        else:
            self.webpage = urlopen('http://travelers.bootsnall.com/?page='+page).read()
        self.soup = BeautifulSoup(self.webpage)
       
    def get_profile_links(self):
        links = []
        boxes = self.soup.find_all(class_="travelerBox")
        for box in boxes:
            links.append(box.a['href'])
        return links

class ProfilePage():
    
    def __init__(self, url):
        print "Getting profile page:  " + str(url)
        self.url = url
        self.webpage = urlopen(url).read()
        self.soup = BeautifulSoup(self.webpage)
   
    def get_information(self):
        section = self.soup.find("section")
        info = {}    
        info['title'] = section.h1.string
        info['header'] = section.header.p.string
        info['details'] = section.find(class_='tripDetails').text.replace("\n"," | ")
        links = []
        a_list = section.find(class_='profileSocial').find_all("a")
        for y in a_list:
            try:
                if y['href'] not in ['http://twitter.com/share', self.url]:
                    links.append(y['href'])
            except:
                continue
        info['links'] = " | ".join(links)
        return info

if __name__ == '__main__' :
    headers = ['Name', 'Title', 'Details', 'Links']
    details = []
    for i in range(1,28):
        page = BootsnallPage(str(i))
        for link in page.get_profile_links():
            profile = ProfilePage(link)
            details.append(profile.get_information())
        print "\n"
    make_file(headers, details)
