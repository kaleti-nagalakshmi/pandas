import pandas as pd
data = {
    "name":["ram","sam","raj","ravi"],
    "roll_No":[1,2,3,4],
    "age":[20,26,13,24]

}
df  = pd.DataFrame(data)
print(df)

col_index = df["name"]
col_index1 = df["roll_No"]
print(col_index)
print(col_index1)

slicing = df[1:3]
print(slicing)






n = pd.read_excel("C:\\Users\\Shyam\\Downloads\\20_students_data.xlsx")
print(n)
print(n.describe())

print(df.head())
print(df.tail(2))

print(n.shape)
print(n[0:20:2])
print(n["Name"][10:20:2])
print(n[["Name","Age"]][5:10:2])
for i in n.iterrows():
    print(i)
print("\n")

# loc stop index included 

print(n.loc[5])
print(n.loc[4,["Name"]])
print(n.loc[2:8])
print("\n")
print(n.loc[4:9,"Name"])
print("\n")
print(n.loc[1:5,["Name","Roll Number"]])
print("\n")


# iloc : access columns through index and stop index excluded

print(n.iloc[2:10,1:3])
print(n.iloc[5,2])
print(n.iloc[1:7,3])
print(n.iloc[[1,2,3]])
print(n.iloc[:,[1,2,3]])
print(n.iloc[12:18,[1,2,3]])
print("\n")

print("sorting") 
print(n.sort_values("Name",ascending = False))
print("\n")
print(n.sort_values(["Name","Age"]))
print("\n")
print(n.sort_values(["Age","marks"],ascending = [0,1]))
print("\n")

print("adding columns")

n["total"]=n["Age"]+n["marks"]
print(n)
print("\n")

n["percentage"]=(n["total"]/300)*100
print(n)
print("\n")
n["status"] = "PASS/FAIL"
print(n)
print("\n")


print("removing columns")
n.drop(columns= "status",inplace=True)
print(n)
print("\n")
n.drop(columns="percentage",inplace=True)
print(n)

# removing duplicates from dataframe
print("removing duplicates")

n.duplicated()
print(n)

n.drop_duplicates(inplace=True)
print(n)

print("\n")

print("data filtering and conditional changes")

fil_1=n.loc[n["Age"]>20]
print(fil_1)

print("\n")

fil_2 = n.loc[n["marks"]>70]
print(fil_2)

start = n.loc[n["Name"].str.startswith("N")]
print(start)
print("\n")

print("export dataframe to excel , csv and text files")

print("\n")

n_1 = pd.read_excel("C:\\Users\\Shyam\\Downloads\\student_marks_10_members.xlsx")
print(n_1)

n_1["Total"]=n_1["Telugu"] + n_1["English"] +n_1["Maths"]+n_1["Science"]+n_1["Social"]
print(n)

n_1["percentage_marks"] = (n_1["Total"]/500)*100
print(n)

n_1.loc[n_1["percentage_marks"]>80,["Grade"]]="First" 
print(n_1)
n_1.loc[(n_1["percentage_marks"] >= 50.0) & (n_1["percentage_marks"] < 80.0),["Grade"]]="Pass"
print(n_1)

monthly = (
    n_1.groupby("Roll Number",as_index = False)["Total"]
    .sum()
    .sort_values("Roll Number")
)
print(monthly)































