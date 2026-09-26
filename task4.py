def factorial(f):
    a=1
    for i in range(1,f+1):
            a*=i
    return a
n=input()
s=0
for i in n:
      s+=factorial(i) 
if n==s:
      print("it is strong number")
else:
      print("it is not strong number")