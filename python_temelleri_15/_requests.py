import requests
import json

result = requests.get('https://jsonplaceholder.typicode.com/todos')


print(result)        # <Response [200]>  # bize başarılı bir sonuç geldiğini belirtir.


result_str = result.text
print(result_str)  
print(type(result_str))    # <class 'str'>



result_dict = json.loads(result_str)
print(result_dict)
print(type(result_dict))    # <class 'list'>    liste içinde dictsler.

print(result_dict[0])   # {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
print(result_dict[0]['title'])    #  delectus aut autem


for i in result_dict:
    print(i)
    print(i['title'])
