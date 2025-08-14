a = input()
num =  a.replace(" ", "")

d = input()
x = int(num[1])
y = int(num[2])
num1 = int(d[x-1])
num2 = int(d[y-1])
if(num1%num2 == 0) or (num2%num1 == 0):
    print("YES")
else:
    print("NO")



