import os
import nltk
import codecs
import sys
from bs4 import BeautifulSoup
import lxml
from lxml.html.clean import Cleaner
import re
from cStringIO import StringIO
import unicodedata

reload(sys)  
sys.setdefaultencoding('utf8')
cleaner = Cleaner()
cleaner.script = True # This is True because we want to activate the javascript filter
cleaner.style = True 
cleaner.kill_tags = ['a','img','href']
cleaner.remove_tags = ['div','span','li']


directory1 = "C:\Users\Satanu\html_test\\"
directory2 = "C:\Users\Satanu\text\\"
for filename in os.listdir(directory1):
    to_write = []
    html = codecs.open(directory1+filename,'r','utf-8')
    raw = lxml.html.tostring(cleaner.clean_html(lxml.html.parse(directory1+filename)))
    name = filename.strip('html') 
    
    text = codecs.open(directory2+filename,'w','utf-8')
    
    text.write(raw)
    
    soup = BeautifulSoup(raw,'html')
    
    title = soup.div.find_next(string=True).strip()
    date = soup.p.find_next(string=True).strip()
    
    #print title
    #print date
    to_write.append(title)
    #title1=nltk.word_tokenize(title)
    #print title1
    #for strong_tag in soup.find_all('date'):
        #print strong_tag.text, strong_tag.next_sibling
    buf = StringIO
    tup = ()
    for strong_tag in soup.find_all('p'):
        tup = strong_tag.text, strong_tag.next_sibling
        content = str(tup[0])
        content =  content.strip("<p>")
        """cleaner2 = Cleaner()
        cleaner2.remove_tags=['p']
        content2 = lxml.html.tostring(cleaner.clean_html(lxml.html.parse(content)))"""
        to_write.append(content)
        to_write.append('\n')
    result = ''.join(to_write)
    
    plain_string = result.encode('utf-8')
    #plain_string = plain_string.encode('ascii')
    print plain_string
        #tokens = nltk.word_tokenize(str(content))
        #text = nltk.Text(tokens)
        #text.concordance('fracking')
            
    """raw = BeautifulSoup(html).get_text()
    print BeautifulSoup(html).get_text()
    tokens = nltk.word_tokenize(raw)
    print tokens
    text = nltk.Text(tokens)
    print text"""
    #print text.concordance('fracking')
    
    text = codecs.open(directory2+name+'txt','w','utf-8')
    text.write(plain_string)
    
#sentence = "This is a sentence to test nltk"
#tokens = nltk.word_tokenize(sentence)
