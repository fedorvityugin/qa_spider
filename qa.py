# -*- coding: utf-8 -*-

import urllib
import lxml.html

def page_spider(adress):
    page = urllib.urlopen(adress)
    finPage = page.read()
    
    doc = lxml.html.document_fromstring(finPage.decode('utf-8'))

#Ссылки на страницы с вопросами

    list_of_links = []
    for link in doc.cssselect('.'): 
        list_of_links.append(link)
    
    for question in list_of_links:
        print question

page_spider('file:///home/fedor/Dropbox/New%20Questions%20-%20Quora.html') #Сюда кидаем адрес страницы
