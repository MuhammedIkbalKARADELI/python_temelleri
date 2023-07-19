# json modülü ile yazılım tiplerinden veriyi kendi dilinin yapısını çevirmeye yarar.

import json


#person = {"Name":"Ali", "Language": ["Python","C#"]}   # bu bir dictionary veri tipidir.


###### json  turn the string to dict
person_string = '{"Name":"Ali", "Language": ["Python","C#"]}'  # bu dict ifadesi şuan bir str ifade olur ve dict metodlarrı işe yaramayacaktır.
print(person_string)   # {"Name":"Ali", "Language": ["Python","C#"]}
print(type(person_string))   # <class 'str'>

#**********
person_dict = json.loads(person_string)  # json str ifadeyi dict e çevirdi. 

print(person_dict)   #  {"Name":"Ali", "Language": ["Python","C#"]}
print(person_dict["Name"])  # Ali
print(type(person_dict))   # <class 'dict'>



with open("person.json") as f:
    data = json.load(f)  # dosyadaki bilgi dict olduğundan load dedik.
    print(data) # {"Name":"Ali", "Language": ["Python","C#"]}   verir  ve dosyayı okumuş olur. 
    print(data["Language"])   # ['Python', 'C#']




######## json  turn the dict to sitring

dict = {
    "Name":"Ahmet",
    "Language": ["C++","Python","Java"]
}

print(dict)
print(type(dict)) # <class 'dict'>

#**********
str = json.dumps(dict)   # json ile dict ifadeyi str ye çevirdi

print(str)
print(type(str))   # <class 'str'>


with open("person1.json","w") as file:
    json.dump(dict,file)



#***************
print(json.dumps(dict, indent=4))   # daha okunabilir analiz edilebilir bir yapı haline getirir.



#########   ############

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))    # creates more readable pfrase 
