def odd_or_even(a):
    if a%2==0:
        return "Even"
    else:
        return "Odd"
user=int(input("enter the number here : "))
print(odd_or_even(user))