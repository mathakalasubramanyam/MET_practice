#FOR LOOP is used to definitive items
fruits=["banana","apple","kiwi"]
for item in fruits:
    print(item)
    if item=="kiwi":
      break
#continue
name="beautiful"
count=0
for item in name:
   if item in ["a","e","i","u"]:
      continue
print(item)
   
fruits=("banana","apple","kiwi")
for item in fruits:
    print(item)

fruits={"banana","apple","kiwi"}
for item in fruits:
    print(item)

fruits={
   "name1":"banana"
   "name2":"kiwi"
}
for item in fruits.keys():
   print(item)

   fruits={
   "name1":"banana"
   "name2":"kiwi"
}
a=[fruits,fruits,fruits]
b=fruits.copy()
a=[fruits,b,fruits]
for item in a.keys():
   print(item)


 