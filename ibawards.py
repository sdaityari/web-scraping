#! /usr/bin/python

from bs4 import BeautifulSoup
from urllib import urlopen

import sys
import xlwt

reload(sys)
sys.setdefaultencoding('utf-8')

INDI = "http://www.indiblogger.in"
IBA = "http://www.indiblogger.in/iba/" #IBAWARDS
EDITION = 1
CATEGORIES = 75

# Categories from 1 to 75
class CategoryPage():
    def __init__(self, category, page):
        webpage = IBA + 'entries.php?pageNum_entries=' + str(int(page)-1) \
                  +'&edition=' + str(EDITION) + '&cat=' + str(category)
        print 'Getting Webpage: ' + webpage
        self.soup = BeautifulSoup(urlopen(webpage).read())

    def is_empty(self):
        try:
            self.soup.find(style = 'margin-top:50px; margin-bottom:200px;').text
            return True
        except Exception as e:
            return False

    def get_total_entries(self):
        return int(self.soup.find(id = 'entries').span.text.replace('(','').replace(')',''))

    def get_category_name(self):
        string = self.soup.find(id = 'entries').text
        return string[:string.index('(')][:-1]

    def get_links(self):
        entries = self.soup.find_all(class_ = 'entry')
        information = []
        for entry in entries:
            temp = []
            temp.append(entry.img['alt'][:-1]) # Blogger Name #Indi glitch has space after each name
            temp.append(INDI + entry.a['href']) # Blogger Profile Link
            div = entry.find(class_ = 'entry_blog')
            temp.append(div.a.text) # Blog name, might contain UTF
            temp.append(div.text.replace(div.a.text, '').replace('\n','')) # Blog link
            temp.append(IBA + div.a['href']) # entry link in IBA
            information.append(temp)
        return information

if __name__ == '__main__':
    workbook = xlwt.Workbook(encoding = 'ascii')
    worksheet = workbook.add_sheet('Details')
    worksheet.write(0, 0, label = 'Sno')
    worksheet.write(0, 1, label = 'Name')
    worksheet.write(0, 2, label = 'Profile')
    worksheet.write(0, 3, label = 'Blog')
    worksheet.write(0, 4, label = 'Blog Link')
    worksheet.write(0, 5, label = 'Entry Link')
    worksheet.write(0, 6, label = 'Category Name')
    row = 1
    try:
        for cat in range(1, CATEGORIES + 1):
            category = CategoryPage(cat, 1)
            if category.is_empty():
                continue
            name = category.get_category_name()
            total = int(category.get_total_entries())
            pages = total // 10 + 1
            for page in range(pages):
                if page > 1:
                    category = CategoryPage(cat, page)
                for entity in category.get_links():
                    worksheet.write(row, 0, label = row)
                    worksheet.write(row, 1, label = entity[0])
                    worksheet.write(row, 2, label = entity[1])
                    worksheet.write(row, 3, label = entity[2])
                    worksheet.write(row, 4, label = entity[3])
                    worksheet.write(row, 5, label = entity[4])
                    worksheet.write(row, 6, label = name)
                    row += 1
        workbook.save('data-indiblogger.xls')
    except Exception as e:
        print e
        workbook.save('data-indiblogger.xls')
