
# big number in n numbers
n = int(input())
num = []
for i in range(n):
    m= int(input())
    num.append(m)
    
max_num = num[0]
for j in num:
    if j > max_num :
        max_num = j 
print(f"bigget number is {max_num}")
