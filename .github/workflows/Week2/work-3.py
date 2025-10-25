# 作業三:規則數列

def func3(index):
    y=[ -2, -3, +1, +2] # y=[0]=-2, y=[2]=+1 以此類推
    n = 25 # 從 25 開始
    for x in range(1, index+1): # index 代表迴圈走的次數 第1次 ~ 第index次
        z = y[( x - 1 ) % 4] # 4 個一循還 # 除以4之後取餘數
        n= n + z # n=25，z=y[0]=-2，n=25-2
    print(n)

func3(1)
func3(5)
func3(10)
func3(30)

# n=1
# sum=0
# while n<=10:
#     sum=sum+n
#     n+=1 # n=n+1
# print(sum)
# for x in range(11):
#     sum=sum+x
# print(sum)

# n=0
# for x in [0,1,2,3]:
#     if x%2==0:
#         continue
#     print(n)
#     n=n+1
# print("最後的 n:", n)

# n=input
# n=int(n)
# for i in range(n):
#     if i*i==n:
#         print(i)
#         break
# else:
#     print("無")

