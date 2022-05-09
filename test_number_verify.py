import os.path
import json
from number_verify import phone_number_validation_helper
from number_verify import PHONE_NUMBER_STATUSES

CSV_FILE = "C:\\Users\\Mohammad Touseef\\Downloads\\Hexa-Reports_00.csv"

"""
Phone Numbers in phone_data.json are generated using following website
https://randommer.io/free-valid-bulk-telephones-generator
"""

PHONE_NUMBER_DATA = os.path.join(os.path.dirname(__file__), 'phone_data.json')
STATUS = 'phone_number_status'

# From Hexa-Reports_00.csv File
invalid_undelivered_numbers = ['13453455452345', '91836890022', '9188302661458', '91860277591', '656594290637',
                               '91987654321', '9112462430113', '626281903196998', '626281903196998',
                               '915403925418', '915403925418', '9115403925418', '91918217793096', '91996570313',
                               '91918217793096', '92313131175', '4479832383372']


def test_report():
    """
    Testing for Undelivered Valid Numbers
    :return:
    """
    print('\nThese numbers are Undelivered and does not exist but valid numbers according to phonenumbers library')
    with open(CSV_FILE, 'r') as file:
        for line in file.readlines():
            if line.startswith('Note:'):
                break
            status = line.split(',')[5]
            if status == 'Undelivered':
                number = line.split(',')[3]
                if number not in invalid_undelivered_numbers:
                    print(number)
                    country = line.split(',')[0]
                    print(country)
                    assert phone_number_validation_helper(f'+{number}')[STATUS] == PHONE_NUMBER_STATUSES['VALID']


with open(PHONE_NUMBER_DATA, 'r', encoding='utf-8') as file1:
    data1 = json.load(file1)


def test_valid_numbers():
    """
    Testing for Positive cases using phone_data.json
    The for loop reads all the numbers for the countries and Validate it
    """
    count = 0
    for item in data1:
        count += 1
        print(item['Country'])
        for numbers in item['valid_numbers']:
            assert phone_number_validation_helper(numbers)[STATUS] == PHONE_NUMBER_STATUSES['VALID']
    print(count)


def test_numbers_less_than_specified_length():
    """
    Testing for Numbers by reducing the number of digits .
    Let's say if India has 10 digits then this function tests the Indian Numbers with 9 digits
    and make assertion that it is invalid
    :return:
    """
    country_count = 0
    for item in data1:
        size = item['Length of Number']
        if len(size) >= 1:
            size = size[0]
            country = item['Country']
            country_count += 1
            print(country)
            for number in item['valid_numbers']:
                number = ''.join(number.split(' ')[1:])
                if number.count('-'):
                    number = ''.join(number.split('-'))
                elif number.count('.'):
                    number = ''.join(number.split('.'))
                number = number[:size-1]
                print(number)
                assert phone_number_validation_helper(number)[STATUS] == PHONE_NUMBER_STATUSES['INVALID']
    print(country_count)


# negative_exceptional_countries = ['Serbia', 'Vatican City']
negative_exceptional_countries = []


def test_numbers_greater_than_specified_length():
    country_count = 0
    for item in data1:
        size = item['Length of Number']
        country = item['Country']
        if country not in negative_exceptional_countries and len(size) >= 1:
            size = max(size)
            country_count += 1
            print(country)
            for number in item['valid_numbers']:
                if number.count('-'):
                    number = ''.join(number.split('-'))
                elif number.count('.'):
                    number = ''.join(number.split('.'))
                number_size = len(list(''.join(number.split(' ')[1:])))
                difference = size - number_size + 1
                end = ''.join(map(str, range(1, difference + 1)))
                number = number + end
                print(number)
                assert phone_number_validation_helper(number)[STATUS] == PHONE_NUMBER_STATUSES['INVALID']
    print(country_count)


# def test_invalid_numbers():
#     for item in data1:
#         print(item['Country'])
#         for number in item['valid_numbers']:
#             if item['Country'] == 'Namibia':
#                 # number_wihtout_code = ''.join(number.split(' ')[1:])
#                 # length = len(number_wihtout_code)
#                 # number = number[:-(length//3)]
#                 number = number + '0'
#                 print(number)
#                 assert phone_number_validation_helper(number)[STATUS] == PHONE_NUMBER_STATUSES['INVALID']
#

# with open('Truth/data.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)
#     data
# # INDIA_PHONE_METADATA = [item for item in data if item['Country or unrecognized territory'] == 'India']
# def test_count():
#     count = 0
#     for item in data:
#         if item['Size ofNN (NSN) [notes 2]'] == '?':
#             count += 1
#     print(count)
"""

# def test_combinations():
#     for item in data:
#         if item['Country or unrecognized territory'] == 'Germany' and item['Mobile Prefix [notes 1]'].count('x') > 0:
#             lower_bound = 0
#             upper_bound = 9
#             try:



# # India
# def test_valid_indian_numbers():
#     """
#     Tests all Mobile number patterns available for India
#     on https://en.wikipedia.org/wiki/List_of_mobile_telephone_prefixes_by_country
#     :return:
#     """
#     for record in range(len(INDIA_PHONE_METADATA)):
#         series = str(INDIA_PHONE_METADATA[record]['Mobile Prefix [notes 1]'])
#         code = str(INDIA_PHONE_METADATA[record]['Interna-tionalCallingCode'])
#         total_digits = INDIA_PHONE_METADATA[record]['Size ofNN (NSN) [notes 2]']
#         # no_of_x are x available in 6xx or any series
#         no_of_x = 0
#         sequence = ''
#
#         # if we have prefix like 6xx , 7xx , 8xx
#         if series.count('x') > 0:
#             no_of_x = series.count('x')
#             series = series.split('x')[0]
#         # 0 to 9 sequence
#         if no_of_x:
#             sequence = ''.join(map(str, range(10)))
#
#         # generating combinations 000 001 002 e.t.c up to 999
#         if sequence:
#             combinations = list(itertools.product(sequence, repeat=no_of_x))
#             end_part_length = total_digits-(len(series)+no_of_x)
#             end = ''.join(map(str, range(end_part_length)))
#             for combination in combinations:
#                 # 9 + xx + 1234567
#                 valid_number = series + ''.join(combination) + end
#                 assert phone_number_validation_helper(valid_number, code)[STATUS] == PHONE_NUMBER_STATUSES['VALID']
#         else:
#             valid_number = series + ''.join(map(str, range(len(total_digits)-len(series))))
#             assert phone_number_validation_helper(valid_number, code)
#
#
# countries_exception_list = ['Antigua and Barbuda', 'Australian Antarctic Territory','Bahamas','Brazil','Colombia','Dominica', 'Faroe Islands','Grenada','Ireland','Kenya','Kiribati','Moldova','Mongolia','Pakistan','People\'s Republic of China','United Kingdom[12]','Venezuela','Yemen','Zambia']
#
#
# def test_valid_numbers_all_country():
#     for record in range(len(data)):
#
#         if isinstance(data[record]['Size ofNN (NSN) [notes 2]'], int) and \
#                 data[record]['Country or unrecognized territory'] not in countries_exception_list:
#         # if isinstance(data[record]['Size ofNN (NSN) [notes 2]'], int) and data[record]['Country or unrecognized territory'] == 'Germany':
#             series = str(data[record]['Mobile Prefix [notes 1]'])
#             code = str(data[record]['Interna-tionalCallingCode'])
#             total_digits = data[record]['Size ofNN (NSN) [notes 2]']
#
#             # no_of_x are x available in 6xx or any series
#             no_of_x = 0
#             sequence = ''
#             print(data[record]['Country or unrecognized territory'])
#
#             # if we have prefix like 6xx , 7xx , 8xx
#             if series.count('x') > 0:
#                 if series.count('x') > 3:
#                     continue
#                 no_of_x = series.count('x')
#                 series = series.split('x')[0]
#
#             # 0 to 9 sequence
#             if no_of_x:
#                 sequence = ''.join(map(str, range(10)))
#
#             # generating combinations 000 001 002 e.t.c up to 999
#             if sequence:
#                 combinations = list(itertools.product(sequence, repeat=no_of_x))
#                 series_length = len(series)
#
#                 if series.count(' ') > 0:
#                     series_length = series_length - series.count(' ')
#                 end_part_length = total_digits-(series_length+no_of_x)
#                 end = ''.join(map(str, range(end_part_length)))
#
#                 for combination in combinations:
#                     # 9 + xx + 1234567
#                     valid_number = series + ''.join(combination) + end
#                     print(valid_number)
#                     assert phone_number_validation_helper(valid_number, code)[STATUS] == PHONE_NUMBER_STATUSES['VALID']
#             else:
#                 series_length = len(series)
#                 if series.count(' ') > 0:
#                     series_length = series_length - series.count(' ')
#                 valid_number = series + ''.join(map(str, range(total_digits - series_length)))
#                 print(valid_number)
#                 assert phone_number_validation_helper(valid_number, code)[STATUS] == PHONE_NUMBER_STATUSES['VALID']
#
#
# def test_valid_number_starting_with_7xxx():
#     series = '7'
#     valid_code = '91'
#
#     # 0 to 9 sequence
#     sequence = ''.join(map(str, range(10)))
#     # generating combinations 000 001 002 e.t.c up to 999
#     combinations = list(itertools.product(sequence, repeat=3))
#
#     for combination in combinations:
#         valid_number = series + ''.join(combination) + '200447'
#         assert phone_number_validation_helper(valid_number, valid_code)[STATUS] == PHONE_NUMBER_STATUSES['VALID']
#
#
# def test_valid_number_starting_with_8xxx():
#     series = '8'
#     valid_code = '91'
#
#     # 0 to 9 sequence
#     sequence = ''.join(map(str, range(10)))
#
#     # generating combinations 000 001 002 e.t.c up to 999
#     combinations = list(itertools.product(sequence, repeat=3))
#
#     for combination in combinations:
#         valid_number = series + ''.join(combination) + '200447'
#         assert phone_number_validation_helper(valid_number, valid_code)[STATUS] == PHONE_NUMBER_STATUSES['VALID']
#
#
# def test_valid_number_starting_with_9xxx():
#     series = '9'
#     valid_code = '91'
#
#     # 0 to 9 sequence
#     sequence = ''.join(map(str, range(10)))
#
#     # generating combinations 000 001 002 e.t.c up to 999
#     combinations = list(itertools.product(sequence, repeat=3))
#
#     for combination in combinations:
#         valid_number = series + ''.join(combination) + '200447'
#         assert phone_number_validation_helper(valid_number, valid_code)[STATUS] == PHONE_NUMBER_STATUSES['VALID']
#
#
# # def test_invalid_number_starting_with_1_to_5():
# #     valid_code = '91'
# #     for i in range(1, 6):
# #         invalid_number = str(i) + '033200447'
# #         print(invalid_number)
# #         assert phone_number_validation_helper(invalid_number, valid_code)[STATUS] == PHONE_NUMBER_STATUSES['INVALID']
#
# #
#
#
# def test_numbers_less_than_10_digits():
#     number = '2444'
#     code = '91'
#     for i in range(1, 6):
#         prefix = 9
#         number = str(prefix) + number
#         print(number)
#         assert phone_number_validation_helper(number, code)[STATUS] == PHONE_NUMBER_STATUSES['INVALID']
#
#
# def test_numbers_11_digits():
#     series = '9'
#     valid_code = '91'
#
#     # 0 to 9 sequence
#     sequence = ''.join(map(str, range(10)))
#
#     # generating combinations 000 001 002 e.t.c up to 999
#     combinations = list(itertools.product(sequence, repeat=3))
#
#     for combination in combinations:
#         valid_number = series + ''.join(combination) + '2004478'
#         assert phone_number_validation_helper(valid_number, valid_code)[STATUS] == PHONE_NUMBER_STATUSES[
#             'INVALID']
#
#
# def test_10_digits_exceptions():
#     # All 10 digit 5's and 1's and 0's are invalid
#     valid_code = '91'
#     for i in range(2, 10):
#         if i == 5:
#             continue
#         number = str(i)*10
#         print(number)
#         assert phone_number_validation_helper(number, valid_code)[STATUS] == PHONE_NUMBER_STATUSES['VALID']
#
#
# def test_10_digits_prefix_with_zero():
#     valid_code = '91'
#
#     # 0 to 9 sequence
#     sequence = ''.join(map(str, range(10)))
#
#     # generating combinations 000 001 002 e.t.c up to 999
#     combinations = list(itertools.product(sequence, repeat=3))
#
#     for h in range(6, 10):
#         for combination in combinations:
#             valid_number = '0' + str(h) + ''.join(combination) + '200447'
#             assert phone_number_validation_helper(valid_number, valid_code)[STATUS] == PHONE_NUMBER_STATUSES[
#                 'VALID']
#
#
# # def test_numbers_starting_with_2():
# #     series = '2'
# #     valid_code = '91'
# #
# #     # 0 to 9 sequence
# #     sequence = ''.join(map(str, range(10)))
# #
# #     # generating combinations 000 001 002 e.t.c up to 999
# #     combinations = list(itertools.product(sequence, repeat=3))
# #     for combination in combinations:
# #         valid_number = series + ''.join(combination) + '200447'
# #         print(valid_number)
# #         assert phone_number_validation_helper(valid_number, valid_code)[STATUS] == PHONE_NUMBER_STATUSES['INVALID']
# #
# #
# # def test_singapore():
# #     number = '8223 4555'
# #     code = '65'
# #     assert phone_number_validation_helper(number, code)[STATUS] == PHONE_NUMBER_STATUSES['VALID']
# #
# #
# # def test_afghanistan_9_digits():
# #     code = '93'
# #     # prefix_list = [20, 26, 30, 40, 50, 60, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]
# #     prefix_list = [2, 3, 4, 5, 6, 7]
# #
# #     for prefix in prefix_list:
# #         for i in range(9):
# #             number = str(prefix) + str(i) + '7128891'
# #             print(number)
# #             assert phone_number_validation_helper(number, code)[STATUS] == PHONE_NUMBER_STATUSES['VALID']
# #
# #
# # def test_afghanistan_wrong_prefix_9_digits():
# #     code = '93'
# #     prefix_list = [20, 30, 40, 50, 60, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]
# #     [prefix_list.append(int('2'+str(x))) for x in range(10)]
# #     for i in range(10):
# #         for j in range(10):
# #             prefix = str(i) + str(j)
# #             if int(prefix) not in prefix_list:
# #                 number = prefix + '7128891'
# #                 print(number)
# #                 assert phone_number_validation_helper(number, code)[STATUS] == PHONE_NUMBER_STATUSES['INVALID']
# #
# #
# # def test_afghanistan_prefix_other_than_7x_9_digits():
# #     code = '93'
# #     prefix_list = [20, 26, 30, 40, 50, 60]
# #     for prefix in prefix_list:
# #         for i in range(10):
# #             number = str(prefix) + '7128891'
# #             print(number)
# #             assert phone_number_validation_helper(number, code)[STATUS] == PHONE_NUMBER_STATUSES['VALID']
# #
# #
# # def test_afghanistan_prefix_other_than_7x_10_digits():
# #     code = '93'
# #     prefix_list = [20, 26, 30, 40, 50, 60]
# #     for prefix in prefix_list:
# #         for i in range(10):
# #             number = str(prefix) + '71288912'
# #             print(number)
# #             assert phone_number_validation_helper(number, code)[STATUS] == PHONE_NUMBER_STATUSES['INVALID']
# #
