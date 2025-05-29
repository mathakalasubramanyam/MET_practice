numbers=[1,2,3,4,5,6,7,8,9,10]
square=0
for i in numbers:
    if i%3==0:
        continue
    square=i*i
    print(square)
    