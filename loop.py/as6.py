dict={
    "apple":2,
    "banana":3,
    "apricot":4,
    "berry":5
}
multiply=1
for i in dict:
    if i[0]=='a':
        multiply=multiply*dict[i]
print("product of values:",multiply)
        