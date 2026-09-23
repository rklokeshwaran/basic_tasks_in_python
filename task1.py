n=int(input("enter the number : "))
a=list()
sum_of_list=0
for i in range(1,n):
    if n%i==0:
        a.append(i)
    else:
        continue
for i in a:
    sum_of_list+=i
if n==sum_of_list:
    print("it is the perfect number")
else:
    print("it is not perfect number")