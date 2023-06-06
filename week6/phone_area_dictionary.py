import re
def phone_area_dictionary(phone_numbers_list):
    area_codes = {}
    for phone_number in phone_numbers_list:
        if phone_number.find("(") != -1:
            area_code = re.match(r"\(\d{3}", phone_number)
            area_code = area_code.group()
            area_code = area_code[1:]
        else:
            area_code = re.match(r"\d{3}", phone_number)
            area_code = area_code.group()
        if area_code not in area_codes:
            area_codes[area_code] = list()
        area_codes[area_code].append(phone_number)
    return area_codes

print(phone_area_dictionary(["333-444-4444", "(333) 444-1234", "111-111-1111", "(111) 333-4444"]))