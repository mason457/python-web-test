#載入pandas
import pandas as pd
#建立Series
data = pd.Series([20,10,15])
#基本操作
print("Max",data.max())
print("Median",data.median())
data = data * 2
print(data)

data = data ==20
print(data)

#建立DataFrame
data = pd.DataFrame({
    "name":["Amy","John","Bob"],
    "salary":[30000,50000,40000]
    })
#基本DataFrame操作
print(data)
#取得特定欄
print(data["name"])
#取得特定列
print("----------------------------------")
print(data.iloc[0])

#Series
#資料索引
data = pd.Series([5,4,-2,3,10],index = ["a","b","c","d","e"])
#print(data)
#觀察資料型態
print("資料型態:",data.dtype)
print("資料數量:",data.size)
print("資料索引:",data.index)
print("----------------------------------")
#取得資料:根據順序 索引
print(data[2],data[0])
print(data["e"],data["d"])
print("----------------------------------")
#數字運算:基本 統計 順序
print("最大值:",data.max())
print("總和:",data.sum())
print("標準差:",data.std())
print("中位數:",data.median())
print("最大的三個位數:",data.nlargest(3))
print("----------------------------------")
#字串運算:基本 串接 搜尋 取代
data = pd.Series(["您好","Python","pandas"])
print(data.str.lower())  #變小寫
print(data.str.len()) #每個字串長度
print(data.str.cat(sep=","))
print(data.str.contains("P"))
print(data.str.contains("好"))
print(data.str.replace("您好","hello"))


#以字典資料為底 建立DataFrame
data = pd.DataFrame({
    "name":["Amy","Bob","Chill"],
    "salary":[30000,40000,50000],
    },index = ["a","b","c"])
print(data)
print("----------------------------------")
#觀察資料
print("資料數量:",data.size)
print("資料形狀(列,欄):",data.shape)
print("資料索引",data.index)
print("----------------------------------")
#取得列(Row)的Series資料:根據順序 索引
print("取得第二列",data.iloc[1],sep = "\n")
print("取得第C位",data.loc["c"],sep = "\n")
print("----------------------------------")
#取得欄(Column)的Series資料:根據欄位名稱
print("取得name欄位",data["name"],sep = "\n")
names = data["name"] #取得series資料
print("把name全轉大寫:",names.str.upper(),sep = "\n")
print("----------------------------------")
#計算薪水的平均值
salaries = data["salary"]
print("薪水平均值",salaries.mean())
print("----------------------------------")
#建立新的欄位
data["revenue"] = [500000,40000,50000000] #data[新蘭位名稱]=列表
data["rank"] = pd.Series([3,6,1],index = ["a","b","c"]) #data[新蘭位名稱]=Series的資料
data["CP"] = data["revenue"] / data["salary"]
print(data)

print("----------------------------------")
#篩選資料-Series
data = pd.Series([20,10,15])
condition = data > 18
print(condition)
filteredData = data[condition]
print(filteredData)
print("----------------------------------")
data = pd.Series(["您好","Python","pandas"])
condition = data.str.contains("P")
print(condition)
filteredData = data[condition]
print(filteredData)
print("----------------------------------")
#篩選資料-DataFrame
data = pd.DataFrame({
     "name":["Amy","Bob","Chill"],
     "salary":[30000,40000,50000]
    })
print(data)
condition = data["salary"] >= 40000
print(condition)
filteredData = data[condition]
print(filteredData)
print("----------------------------------")
condition = data["name"] == "Amy"
print(condition)
filteredData = data[condition]
print(filteredData)