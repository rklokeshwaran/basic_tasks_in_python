def get_data():
    while True:
        with open("data.txt", "r") as file:
            data = file.read()
            a= input("Enter what you want to search : ")
            b=data.split("\n")
            for i in b:
                if a in i:
                    print(i)
                    break