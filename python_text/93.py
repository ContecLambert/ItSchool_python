import requests
from bs4 import BeautifulSoup
import re

#크롤링할 사이트 주소를 정의합니다.
source_url = "https://namu.wiki/RecentChanges"

#사이트의 HTML 구조에 기반하여 크롤링을 수행합니다.
req = requests.get(source_url)
html = req.content
# print(html)
soup = BeautifulSoup(html,'lxml')
contents_table = soup.find(name="table")
table_body = contents_table.find(name="tbody")
table_rows = table_body.find_all(name="tr")

# a 태그의 href 속성을 리스트로 추출하여 크롤링할 페이지 리스트를 생성합니다.
page_url_base = "https://namu.wiki"
page_urls = []
# print(len(table_rows))
for index in range(0,len(table_rows)):
    first_td = table_rows[index].find_all('td')[0]
    td_url = first_td.find_all('a')
    if len(td_url)>0:
        page_url = page_url_base + td_url[0].get('href')
        page_urls.append(page_url)

page_urls = list(set(page_urls))
for page in page_urls[:5]:
    print(page)