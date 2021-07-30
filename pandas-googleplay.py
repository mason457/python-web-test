import pandas as pd
#讀取資料
data = pd.read_csv("googleplaystore.csv") #把CSV資料轉換成DataFrame
#觀察資料
print("資料數量",data.shape)
print("資料欄位",data.columns)
print("----------------------------------------")
#分析資料:評分各種統計數據
condition = data["Rating"] <= 5
data = data[condition]
print("平均數",data["Rating"].mean())
print("中位數",data["Rating"].median())
print("前100應用程式平均",data["Rating"].nlargest(100).mean())
print("----------------------------------------")
#分析資料:安裝數量的各種統計數據
data["Installs"] = pd.to_numeric(data["Installs"].str.replace("[,+]","").replace("Free",""))
print("平均數",data["Installs"].mean())
condition = data["Installs"] > 100000
print("安裝數大於10萬",data[condition].shape[0])
print("----------------------------------------")
#基於資料的應用:關鍵字搜尋應用程式名稱
keyword = input("請輸入關鍵字:")
condition = data["App"].str.contains(keyword,case = False)
print(data[condition])
print("包含關鍵字的應用程式數量",data[condition].shape[0])
