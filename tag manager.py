tags={"python","fastapi","backend"}
user=input("enter the tag:")
if user in tags:
    print("tags already exists in the set")
else:
    print("not")
    tags.add(user)
print(tags)
