import sys
sys.path.append('C:\\Python\\Lib\\site-packages')
from bs4 import BeautifulSoup as BS
import requests as req

def main():
    url1='http://mypi.ruliweb.com'
    url2='http://www.ruliweb.com'

    test=input('보고 싶은 웹 페이지의 url를 정확하게 적어주세요. 예: http://www.naver.com')
    if test[:8]=='http://':
        url=test
        res=req.get(url)
    else:
        res=req.get(url1)
    sp=BS(res.text, 'html.parser')
    print(sp)

if __name__=='__main__':
    print('This is crawler test file')
    main()
