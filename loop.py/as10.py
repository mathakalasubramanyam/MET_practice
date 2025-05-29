dict={
    "name":"alice",
    "city":"new york",
    "hobby":"coding"
}
for i in dict:
    if len(dict[i])>5:
        print(dict[i].upper())
    else:
        print(dict[i].lower())

