import json
from pprint import pprint
from number_verify import phone_number_validation_helper


"""
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

negative_case = {
    "Country_Name": "",
    "Length of Number": []
}

output = []
with open('countries.json', 'w') as file:
    file.write('[')
    for item in data:
        country = item['Country or unrecognized territory']
        country = country if country.count('[') == 0 else country.split('[')[0]
        if country not in negative_case['Country_Name']:
            if negative_case['Country_Name'] != "":
                file.write(json.dumps(negative_case)+',')
                negative_case['Country_Name'] = ""
                negative_case["Length of Number"] = []
            negative_case['Country_Name'] = country
        size = item['Size ofNN (NSN) [notes 2]']
        if size not in negative_case['Length of Number']:
            if isinstance(size, str):
                if size.count('-'):
                    [negative_case['Length of Number'].append(int(x)) for x in size.split('-') if int(x) not in negative_case['Length of Number']]
            else:
                negative_case['Length of Number'].append(size)
    file.write(']')
pprint(output)





# valid_code = '91'
# for i in range(0, 10):
#     for j in range(0, 10):
#         for k in range(0, 10):
#             valid_number = '6' + str(i) + str(j) + str(k) + '200447'
#             print(valid_number)
#             print(phone_number_validation_helper(valid_number, valid_code))

# for i in range(0, 10):
#     for j in range(0, 10):
#         for k in range(0, 10):
#             valid_number = '7' + str(i) + str(j) + str(k) + '200447'
#             print(valid_number)
#             print(phone_number_validation_helper(valid_number, valid_code))

# for i in range(0, 10):
#     for j in range(0, 10):
#         for k in range(0, 10):
#             valid_number = '8' + str(i) + str(j) + str(k) + '200447'
#             print(valid_number)
#             print(phone_number_validation_helper(valid_number, valid_code))

# for i in range(0, 10):
#     for j in range(0, 10):
#         for k in range(0, 10):
#             valid_number = '6' + str(i) + str(j) + str(k) + '200000'
#             print(valid_number)
#             print(phone_number_validation_helper(valid_number, valid_code))

# valid_number = '1800 103 8181'
#
# print(phone_number_validation_helper(valid_number, '91'))
# for i in range(1, 6):
#     invalid_number = str(i) + '13200447'
#     print(invalid_number)
#     print(phone_number_validation_helper(invalid_number, valid_code))

# for i in range(0, 6):
#     invalid_number = str(i) + '000200447'
#     print(invalid_number)
#     print(phone_number_validation_helper(invalid_number, valid_code))

# code = '93'
# # prefix_list = [20, 26, 30, 40, 50, 60, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]
# prefix_list = [2, 3, 4, 5, 6, 7]
#
# for prefix in prefix_list:
#     for i in range(10):
#         number = str(prefix) + str(i) + '7128891'
#         print(number)
#         print(phone_number_validation_helper(number, code))

# number = '1234567899'
# telphone = ''
#
#
# print(phone_number_validation_helper(number, valid_code))
"""