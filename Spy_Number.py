num=int(input())
sum=0
pro=1
num1=num
while(num>0):
    d=num%10
    sum=sum+d
    pro=pro*d
    num=num//10
if sum==pro:
    print("Spy Number")
else:
    print("Not Spy Number")