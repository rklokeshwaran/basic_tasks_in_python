def set_data():
    while True:
        with open("data.txt","a") as file:
            a=input("enter the topic : ")
            b=input("enter the description : ")
            file.write("\n")
            file.write(a)
            file.write(" : "+b)
            file.write("\n")