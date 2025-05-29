a=input("enter the five names:")
b=a.split(",")
for i in b:
    if i== "yamini":
        print("name is exists")
        break
else:
    print("does not exists") 

