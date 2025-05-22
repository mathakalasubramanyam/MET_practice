students={"alice":(85,90,78),
          "bob":(50,45,60)}
user=input("enter the name:")
if user in students:
    avg=(students[user][0]+students[user][1]+students[user][2])/3
    print(avg)
    if avg>=60:
        print("passed")
    else:
        print("Failed")
else:
    print("students are not allowed")
    
