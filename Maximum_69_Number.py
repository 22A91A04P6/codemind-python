n=int(input())
l=int(n%10)
n=n/10
t=int(n%10)
n=n/10
s=int(n%10)
n=n/10
f=int(n%10)
n=n/10
if f==6:
    f=9
elif s==6:
    s=9
elif t==6:
    t=9
elif l==6:
    l=9
print(f"{f}{s}{t}{l}")