cart=[{"id":1,"name":"shirt","qty":1}]
product_id=int(input("enter the id:"))
product_name=input("enter the string:")
car=[{"id1":product_id,"name1":product_name}]
print(car)
if car[0]["id1"]==cart[0]["id"]:
    print("item already in cart")
else:
    cart.append(car)
    print(cart)