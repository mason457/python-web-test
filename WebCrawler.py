#抓取資料
import json
#抓取網頁原始碼(html)
import urllib.request as req
url = "https://www.ptt.cc/bbs/movie/index.html"
#建立一個Request物件 附加Request Headers的訊息
request = req.Request(url, headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"
})
with req.urlopen(request) as response:
    data = response.read().decode("UTF-8")
# print(data)
#解析原始碼 取得標題
import bs4
root = bs4.BeautifulSoup(data, "html.parser")
#print(root.title.string)
titles = root.find_all("div", class_ = "title") #尋找 class="title"的標籤
#print(titles)
for title in titles:
    if title.a != None:   #如果標題包含
        print(title.a.string)
