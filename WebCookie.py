#抓取資料
import json
#抓取網頁原始碼(html)
import urllib.request as req
def getData(url):   #抓出網頁所有標題 抓出上一頁的超連結並回傳
    #建立一個Request物件 附加Request Headers的訊息
    request = req.Request(url, headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"
        ,"cookie":"over18=1"
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
    #找上一頁文字
    nextLink = root.find("a",string = "‹ 上頁") #找‹ 上頁的文字
    return nextLink["href"]

#抓取多個頁面標題
PageURL = "https://www.ptt.cc/bbs/Gossiping/index.html"
count = 0
while count < 5:
    PageURL = "https://www.ptt.cc"+getData(PageURL)
    count += 1
