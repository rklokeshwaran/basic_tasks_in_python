n=int(input())
str1=str(n)
p=len(str1)
s=0    
for i in str1:
    s+=int(i)**p
if n==s:
    print("It is amstrong number")
else:
    print("it is not a amstrong number")