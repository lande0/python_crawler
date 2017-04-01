import sys
sys.path.append('C:\\Python\\Lib\\site-packages')
import urllib.request
from bs4 import BeautifulSoup as BS
import requests as req
import webbrowser
url_front='file:\\\\\\C:\\Python\\test\\python_crawler\\'


def findurl_short(name, keyword):
    try:
        f=open('%s'%name, 'r')
        lines=f.readlines()
        f.close()
        htp=[]
        if lines!=[]:
            listc=lines[0].split("\\")
    except:
        listc=[]
        listd=[]
        htp=[]
        url_full='%s%s'%(url_front, name)
        url_req=urllib.request.Request(url_full)
        url_bs=BS(urllib.request.urlopen(url_req).read(), 'html.parser')
        lines=url_bs.find_all('a')
        for ln in lines:
            c=ln.get('href')
            d=ln.string
            if type(c)==str:
                listc+=[c]
                listd+=[d]    
    ii=0
    hhtp={}
    for i in range(len(listc)):
        if 'http:' and keyword in listc[i]:
            j=listc[i].find('http:')
            jj=listc[i][j:]
            k=jj.find(")")
            kk=jj.find('(')
            km=jj.find("\"")
            if kk<k and kk>0:
                continue
            elif k<km and k>0:
                htp.append(jj[:k])
            elif km>0:
                htp.append(jj[:km])
            else:
                htp.append(jj)
            hhtp[listc[ii]]=listd[ii]
        ii+=1
    return hhtp


def findurl_long(name, type_of_file, keyword):
    try:
        f=open('%s.%s'%(name, type_of_file), 'r')
        lines=f.readlines()
        f.close()
        htp=[]
        if lines!=[]:
            listc=lines[0].split("\\")
    except:
        listc=[]
        listd=[]
        htp=[]
        url_full='%s%s.%s'%(url_front, name, type_of_file)
        url_req=urllib.request.Request(url_full)
        url_bs=BS(urllib.request.urlopen(url_req).read(), 'html.parser')
        lines=url_bs.find_all('a')
        for ln in lines:
            c=ln.get('href')
            d=ln.string
            if type(c)==str:
                listc+=[c]
                listd+=[d]    
    ii=0
    hhtp={}
    for i in range(len(listc)):
        if 'http:' and keyword in listc[i]:
            j=listc[i].find('http:')
            jj=listc[i][j:]
            k=jj.find(")")
            kk=jj.find('(')
            km=jj.find("\"")
            if kk<k and kk>0:
                continue
            elif k<km and k>0:
                htp.append(jj[:k])
            elif km>0:
                htp.append(jj[:km])
            else:
                htp.append(jj)
            hhtp[listc[ii]]=listd[ii]
        ii+=1
    return hhtp

def findurl():
    idea=input('url를 검색하고 싶은 파일명과 검색하고 싶은 키워드를 적어주세요.\n').split(',')
    if '.' in idea[0] and len(idea)>1:
        c=findurl_short(idea[0], idea[1])
    elif '.' in idea[0] and len(idea)==1:
        c=findurl_short(idea[0], '')
    elif '.' not in idea[0] and len(idea)>1:
        data_type=input('확장자명을 적어주세요. ex) txt\n')
        c=findurl_long(idea[0], data_type, idea[1])
    else:
        data_type=input('확장자명을 적어주세요. ex) txt\n')
        c=findurl_long(idea[0], data_type, '')
    return c

def search(url_dic, keyword):
    keylist=list(url_dic.keys())
    itemlist=list(url_dic.values())
    c={}
    i=0
    j=0
    for key in keylist:
        if keyword in key:
            print("%s - %s : %s"%(keyword, key, itemlist[i]))
            c[key]=itemlist[i]
            j=1
        elif itemlist[i]!=None and keyword in itemlist[i]:
            print("%s - %s : %s"%(keyword, key, itemlist[i]))
            c[key]=itemlist[i]
            j=1
        
        i+=1
    if j==0:
        print('%s를 포함한 결과가 없습니다.'%keyword)
        c=url_dic
    return c

def dosearch(url_dic, keywords):
    ur=url_dic
    for key in keywords:
        ur=search(ur, key)
    return ur

def main():
    url1='http://mypi.ruliweb.com'
    url2='http://www.ruliweb.com'
    test_url='file:\\\\\\C:\\Python\\test\\python_crawler\\test.html'
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
    name_read=input('If you want to open the file, please input the name of file precisely.')
    if name_read=="mypi":
        f=open('test.html','r')
        lines=f.readlines()
        f.close()
        urid='file:\\\\\\C:\\Python\\test\\python_crawler\\ruliweb_id.html'
        ruli_sp=BS(urllib.request.urlopen(urllib.request.Request(urid)).read(), 'html.parser')
        ruli_lines=str(ruli_sp.find_all('form')[0])
        print(ruli_lines)

        f=open('test.html', 'w')
        f.write("""<html><body>
                    %s"""%ruli_lines)
        f.close()
        for line in lines:
            f=open('test.html', 'a')
            f.write(line)
            f.close()
        f=open('test.html', 'a')
        f.write('</body></html>')
        f.close()
        f=open('test2.html', 'w')
        f.write("""<html><body><iframe src="%s"></iframe>
                    """%urid)
        f.close()
        for line in lines:
            f=open('test2.html', 'a')
            f.write(line)
            f.close()
        f=open('test2.html', 'a')
        f.write('</body></html>')
        f.close()
        webbrowser.open(test_url)
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
