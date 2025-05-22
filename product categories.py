categories={
     "clothes":["shirts","jeans"],
     "electronics":["phone","charger"]}
users=input("enter the name:")
if users in categories:
    print(categories[users])
else:
    print("invalid categories")


