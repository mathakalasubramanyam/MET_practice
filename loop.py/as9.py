tuple=("sam","john","alex","bob")
for i in tuple:
    if len(i)<=3:
        print(i.upper())
    else:
        print(i.capitalize())