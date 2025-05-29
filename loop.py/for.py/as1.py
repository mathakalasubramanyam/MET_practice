a=list(input("enter the five numbers:"))
print(a)
key=input()
for item in a:
        if item in key:
            print("found")
            break
else:
     print("not found") 