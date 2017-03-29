import sys
sys.path.append('C:\\Python\\Lib\\site-packages')
import urllib.request
from bs4 import BeautifulSoup as BS
import requests as req

def findurl(name):
    f=open(name, 'r')
    lines=f.readlines()
    f.close()
    c=lines[0]
    listc=c.split("\\")
    htp=[]
    htpreal=[]
    for i in range(len(listc)):
        if 'http:' in listc[i]:
            j=listc[i].find('http:')
            jj=listc[i][j:]
            k=jj.find(")")
            kk=jj.find('(')
            km=jj.find("\"")
            #print(jj)
            #print(k, km)
            if kk<k and kk>0:
                continue
            elif k<km and k>0:
                htp.append(jj[:k])
            elif km>0:
                htp.append(jj[:km])
            else:
                htp.append(jj)
#    for i in range(len(htp)):
#        if htp[i]:
#            htpreal.append(htp[i])
    return htp

def main():
    url1='http://mypi.ruliweb.com'
    url2='http://www.ruliweb.com'
    endsent="웹페이지를 출력했습니다."
    q1="보고 싶은 웹 페이지의 url를 정확하게 적어주세요. 예) http://www.naver.com\n"
    mypi=['mypi', 'Mypi', '마이피']
    hdr={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13F69 Safari/601.1',
         'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
         'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
         'Accept-Encoding':'none',
         'Connection':'keep-alive'}
    
    reqt=urllib.request.Request(url1, headers=hdr)

    test=input(q1)
    if len(test)>8:
        url=test
        reqt=urllib.request.Request(url, headers=hdr)
        res=req.get(url)
    elif test in mypi:
        reqt=urllib.request.Request(url1)
        res=req.get(url1)
    else:
        reqt=urllib.request.Request(url2)
        res=req.get(url2)
    sp=BS(urllib.request.urlopen(reqt).read(), 'html.parser')
    print('%s의 %s'%(res.url,endsent))
    #print(sp.prettify())
    dt=""
    i=0
    f=open('test.html', 'r')
    lines=f.readlines()
    f.close()
    f=open('test.html', 'w')
    f.write('<html><body>')
    f.close()
    for lk in sp.find_all('a'):
        gg=lk.get('class')
        g=str(lk)
        #print(gg)
        if 'mypi' in g and gg==["subject", "deco"]:
            if str(lk) not in lines:
                g=g+'<br></br>'
                f=open('test.html', 'a')
                f.write(g)
                f.close()
    f=open('test.html', 'a')
    f.write('</body></html>')
    f.close()
        
        #try:
        #    dt+="<a href=\"%s\">%s</a>\n"%(str(lk.get('href')),str(lk.get_text()))
        #except:
        #    continue
    #print(len(dt))
        

    data=urllib.request.urlopen(reqt).read()
    if 'www' in test:
        name=test[test.find('w.')+2:]
    else:
        name=test[test.find('//')+2:]
    name=name[:name.find('.')]

    #print(data)
    f=open('%s.html'%name, 'wb')
    f.write(data)
    f.close()
    return sp


if __name__=='__main__':
    print('This is crawler test file')
    main()

#import webbrowser
#webbrowser.open(url)
