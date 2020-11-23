import csv
import codecs
import urllib2, cookielib
import sys  
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


reload(sys)  
sys.setdefaultencoding('utf8')

f = codecs.open('email_output.txt','r','utf-8')
g = codecs.open('actual_link.txt','w','utf-8')
g.close()
for line in f:
        #print line 
        fields = line.split('\t')
        s = fields[1].strip()
        end_index = s.find("&ct=ga&cd")
        actual_link = s[42:end_index]
        email_id = fields[0]
        if(actual_link.startswith('http')) :
            #print actual_link
            g=codecs.open('actual_link.txt','a','utf-8')
            g.write(email_id+"\t"+actual_link)
            g.write('\n')
            g.close
            
f.close()
        
g = codecs.open('actual_link.txt','r','utf-8')

for i, line in enumerate(g):
    data = line.split('\t')

    #source_name = source_name[]
    req = urllib2.Request(data[1], headers={'User-Agent' : "Magic Browser"})

    try:
        response = urllib2.urlopen(req, context=ctx, timeout=5000000)
    except urllib2.HTTPError, e:
        print e
    except urllib2.URLError, e:
        print e
    contents = response.read()
    headers = response.info()
    #print headers
    page_name = "C:\Users\Satanu\htmls\\"+str(i)+data[0]+".html"
    print i
    
    if contents:
        f_html = codecs.open(page_name, 'w')
    
        f_html.write(contents)
        f_html.close()
