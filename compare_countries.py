import json


with open('merge.json', 'r') as file:
    data = json.load(file)
    with open('phone_data.json', 'w') as phone_data:
        phone_data.write('[')
        for item in data:
            if len(item['Length of Number']) == 0:
                lower = 100
                upper = 0
                for number in item['valid_numbers']:
                    number = ''.join(number.split(' ')[1:])
                    if number.count('-'):
                        number = ''.join(number.split('-'))
                    if upper < len(number):
                        upper = len(number)
                    if lower > len(number):
                        lower = len(number)
                if upper == lower:
                    item['Length of Number'].append(upper)
                else:
                    item['Length of Number'].append(lower)
                    item['Length of Number'].append(upper)
                phone_data.write(json.dumps(item)+',')
            else:
                phone_data.write(json.dumps(item)+',')
        phone_data.write(']')
"""with open('countries.json', 'r') as file1:
    data = json.load(file1)
    count = 0
    with open('Truth/valid_numbers.json', 'r') as file2:
        with open('merge.json', 'w') as file3:
            file3.write('[')
            data1 = json.load(file2)
            for item in data:
                for item1 in data1:
                    # if item['Country_Name'].strip().count(item1['Country'].strip()) > 0:
                    if item1['Country'].strip().count(item['Country_Name'].strip()) > 0:
                        item1['Length of Number'] = item['Length of Number']
                        file3.write(json.dumps(item1)+',')
                        print(item['Country_Name'] + '\t' + item1['Country'])
                        count += 1
            file3.write(']')
        print(count)
"""