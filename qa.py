# -*- coding: utf-8 -*-

import urllib
import lxml.html

def QuoraLinkSpider(adress):
    newPage = urllib.urlopen(adress)
    finPage = newPage.read()
    
    doc = lxml.html.document_fromstring(finPage.decode('utf-8'))

    list_of_urls = []
    for question in doc.cssselect('.question_link'):
        list_of_urls.append(question.get('href'))
    
    for url in list_of_urls[:15]:
        QuoraQuestionExtractor(url)    
        
        
def QuoraQuestionExtractor(link):
    endPage = urllib.urlopen(link)
    finalPage = endPage.read()
                
    doc = lxml.html.document_fromstring(finalPage.decode('utf-8'))
    
    list_of_questions = []
    for question in doc.cssselect('.w5.question_text_edit.row>h1'):
        list_of_questions.append(question.text_content())
     
    for link in list_of_questions:
        print link

QuoraLinkSpider('file:///home/fedor/Dropbox/Science/qa_spider/saved_pages/New%20Questions%20-%20Quora.html') #Сюда кидаем адрес страницы

