locations=[(12.9716,77.5946)]
user=float(input("enter the latitude:"))
user1=float(input("enter the longitude"))
tuple2=(user,user1)
print(tuple2)
if tuple2==locations:
    print("location is already exists")
else:
    print("no")
    locations.append(tuple2)
print(locations)
