# -*- coding: utf-8 -*-

import urllib

import lxml.html

def grab_quora_link(adress):
    new_page = urllib.urlopen(adress)
    fin_page = new_page.read()
    
    doc = lxml.html.document_fromstring(fin_page.decode('utf-8'))

    list_of_urls = []
    for question in doc.cssselect('.question_link'):
        list_of_urls.append(question.get('href'))
    
    for url in list_of_urls[:15]:
        extract_quora_question(url)
        
        
def extract_quora_question(link):
    end_page = urllib.urlopen(link)
    final_page = end_page.read()
                
    doc = lxml.html.document_fromstring(final_page.decode('utf-8'))
    
    list_of_questions = []
    for question in doc.cssselect('.w5.question_text_edit.row>h1'):
        list_of_questions.append(question.text_content())
     
    for link in list_of_questions:
        print link

grab_quora_link('file:///home/fedor/Dropbox/Science/qa_spider/saved_pages/New%20Questions%20-%20Quora.html') #Сюда кидаем адрес страницы

