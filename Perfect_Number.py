a=int(input())
f=0
for i in range(1,a):
    if a%i==0:
        f=f+i
if f==a:
    print('True')
else:
    print('False')
        
    