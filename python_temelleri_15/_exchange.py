import requests
import json


api_url = "https://api.exchangeratesapi.io/v1/latest?base="

bozulan_doviz = input("Bozulan döviz: ")
alinan_döviz = input("Alınan döviz: ")
miktar = int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz? "))

result = requests.get(api_url + bozulan_doviz)
result = json.loads(result.text)

print("1 {0} = {1}  {2} ".format(bozulan_doviz, result["rates"][alinan_döviz], alinan_döviz ))

print("{0} {1} = {2} ".format(miktar, bozulan_doviz, miktar*result["rates"][alinan_döviz] ))






