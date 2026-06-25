
import pandas as pd
data = {
    "year":("jan","feb","mar","apl","may","jun","jul","aug","sep","oct","nov","dec"),
    "sales_1":(12,45,34,34,62,35,14,26,29,30,37,48),
    }
s = pd.DataFrame(data)
# s = dg.sort_values("year")

import matplotlib.pyplot as plt
# plt.figure(figsize=(10,4))
# plt.bar(s["year"],s["sales_1"],color="blue")

# plt.title("yearly total units sold trend",color="purple")
# plt.xlabel("order year",color="green")
# plt.ylabel("yearly sales",color="green")
# plt.xticks(s["year"],rotation=45)

# plt.grid(False)
# plt.show()


# line chart

plt.figure(figsize=(10,4))
plt.plot(s["year"],s["sales_1"],marker="o",color="green")

plt.title("yearly total units sold trend",color="purple")
plt.xlabel("order year",color="blue")
plt.ylabel("yearly sales",color="blue")
plt.xticks(s["year"],rotation=90)

plt.grid(True)
plt.tight_layout()
plt.show()



 # histogram
# import pandas as pd
# marks_student = {
#      "marks":(4, 50, 30, 60, 65, 70, 5, 80, 60, 90, 95, 90, 75, 80)
# }
# marks_1 = pd.DataFrame(marks_student)

# import matplotlib.pyplot as plt
# plt.figure(figsize=(12,4))
# plt.hist(marks_1["marks"],bins=40,color="green")

# plt.title("students marks",color="blue")
# plt.xlabel("marks",color="blue")
# plt.ylabel("frequency",color = "green")

# plt.grid(False)
# plt.tight_layout()
# plt.show()

# import seaborn as sns
# data_1={
# "total_revenue":[20,24,34,23,56,89,56,34,23,1,2],
# "profit":[34,59,66,74,76,28,40,58,34,28,10],
# "sales_channel":["online","store","online","store","online","store","online","store","online","store","online"]
# }
# df = pd.DataFrame(data_1)
# plt.figure(figsize=(12,4))
# sns.barplot(
#     data = df,
#     x = "total_revenue",
#     y = "profit", 
#     hue = "sales_channel", 
    
# )
# plt.title("revenue vs profit")
# plt.tight_layout()
# plt.show() 







