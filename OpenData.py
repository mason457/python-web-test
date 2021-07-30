#網路連線
# import urllib.request as request
# src = "http://www.ntu.edu.tw"
# with request.urlopen(src) as response:
#     data = response.read().decode("utf-8")
# print(data)

import urllib.request as request
import json
src = "https://data.taipei/api/v1/dataset/068400d5-2b78-4bc2-8293-1ed59bf2ec42?scope=resourceAquire"
with request.urlopen(src) as response:
    data = json.load(response)
#將名稱列表
clist = data["result"]["results"]
with open("data2.txt", "w",encoding = "UTF-8") as file:
    for company in clist:
        file.write(company["行業別\\行政區"]+"\n")