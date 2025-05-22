users={("john","1234"):"admin",("alice","abcd"):"editor"}
username=input("enter the username:")
password=input("enter the password:")
tuple=(username,password)
print(tuple)
if tuple in users:
    print("welcome")
else:
    print("invalid login")