import json
import sys
import  time
from pprint import pprint
import requests

# response = requests.post(
#     url=f'https://randommer.io/free-valid-bulk-telephones-generator?number=20&twoLettersCode=AG&X-Requested-With=XMLHttpRequest')
# print(response.json())


with open('data/Country_Codes.json','r') as file:
    data = json.load(file)

with open('data/numbers.json', 'w') as file1:
    file1.write('[')
    for item in data:
        try:
            country_dic = {
                "Country": "",
                "Code": "",
                "Numbers": []
            }
            number_count = 100
            code = item['code'].upper()
            country_name = item['name']
            print(country_name)
            response = requests.post(url=f'https://randommer.io/free-valid-bulk-telephones-generator?number={number_count}&twoLettersCode={code}&X-Requested-With=XMLHttpRequest')
            time.sleep(1)
            print(response.json())
            country_dic['Country'] = country_name
            country_dic['Code'] = code
            country_dic['Numbers'].append(response.json())
            file1.write(json.dumps(country_dic)+',')
        except Exception:
            pass
    file1.write(']')
# with open('data.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)
# # pprint(data)
#
# country_list = list(set([item['Country or unrecognized territory'] for item in data]))
# print(len(country_list))
# pprint(sorted(country_list))