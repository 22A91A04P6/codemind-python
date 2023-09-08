n=int(input())
s=n*n
a=s%10
b=s//10
c=s//100
d=a+b+c
if d==n:
    print("Neon Number")
else:
    print("Not Neon Number")