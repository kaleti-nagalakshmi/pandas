import pandas as pd
data = {
    "Roll_no" : (1,2,3,4,5,6,6,7,8),
    "Names" :("hari","aswini","anjali","sandya","naga","devi","devi","bhavani","vasu"),
    "gender":("m","f","f","f","f","f","f","f","m"),
    "section":("A","B","C","A","A","C","C","B","A"),
    "maths" :(12,34,67,45,72,79,79,34,58),
    "science" : (35,57,89,24,69,67,67,67,23),
    "telugu" : (46,68,86,25,89,45,45,35,38)
}
df = pd.DataFrame(data)
print(df)

print(df.head())
print(df.tail(3))
print(df.columns)
print(df.shape)
print(df.Names)
print(df[["Names","maths"]])
print(df.head(4))
df["total"] = df["maths"]+df["telugu"]+df["science"]
print(df) 
print(df["total"]/3)

df["average"] = df["total"]/3
print(df)




     
maths = df.loc[df["maths"] > 80] 
print(maths)

english_1 = df.loc[df["telugu"]<50]
print(english_1)

grade = df.loc[df["total"]>200]
print(grade)

sort_maths=df.sort_values("maths")
print(sort_maths)
total_sort= df.sort_values("total",ascending=False)
print(total_sort)


df.loc[df["Names"]=="naga","maths"]=56
print(df)

df.loc[df["Names"]=="naga","Names"]="lakshmi"
print(df)

drop =df.drop(columns="maths")
print(drop)

df=df.drop([2,5])
print(df)

df.loc[len(df)] = 9 ,"lakshmi","f","A",45,67,38,150,50.00
print(df)

duplicate = df.duplicated()
print(duplicate)
remove_du=df.drop_duplicates()
print(remove_du)

print(df.isnull())

print(df.isnull().sum())

print(df.isnull().values.any())

# intermediate tasks :
maths_sum= df.groupby("section")["maths"].sum()
print(maths_sum)

tel_avg = df.groupby("section")["telugu"].max()
print(tel_avg)

eng_min = df.groupby("section")["science"].min()
print(eng_min)

# max marks and name
print(df["maths"].max())
print(df.loc[df["maths"].idxmax(),["Names","maths"]])
# value counts
print(df["gender"].value_counts())

print(df["maths"].sum()/3)
print(df["maths"].mean())

print(df.describe()["maths"]["max"])
print("\n")
print(df.describe()["telugu"].max())
print(df.describe()["science"].min())

df.to_csv("file.excel", index=False)
print(df)



import pandas as pd
data = {
    "year":("jan","feb","mar","apl","may","jun","jul","aug","sep","oct","nov","dec"),
    "sales_1":(12,45,34,34,62,35,14,26,29,30,37,48),
    "sales_2":(24,5,78,96,35,49,50,28,49,25,14,68),
    "sales_channel":["online","store","online","store","online","store","online","store",
                     "online","store","online","store"]
}
s = pd.DataFrame(data)
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(len(s["year"]))
w = 0.4

plt.bar(x-w/2,s["sales_1"],width=w,label = "sales 1")
plt.bar(x+w/2,s["sales_2"],width=w,label ="sales 2")
plt.xlabel("order year")
plt.ylabel("sales")
plt.title("comparing sales of two products ")

plt.xticks(x,s["year"])
plt.show()






















