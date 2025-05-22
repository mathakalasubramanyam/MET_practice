data=[{"name":"prasanth",
      "age":45},
     {
         "name":"kareem",
         "age":45
     }]
print(data)
def extract_names(details):
    name_1=details[0]["name"]
    name_2=details[1]["name"]
    return [name_1,name_2]
def extract_ages(ages):
    age_1=ages[0]["age"]
    age_2=ages[1]["age"]
    return [age_1,age_2]

names= extract_names(data)
print(names)
age_3=extract_ages(data)
print(age_3)
