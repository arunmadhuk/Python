import openpyxl
from openpyxl.utils import column_index_from_string
import re
import json


# Working class to contain an "item" (value, column)
class Item:
    def __init__(self, value, col):
        self.value = value
        self.col = col


# Example Excel reader class
class ExcelReader:
    def __init__(self, excel_file="template.xlsx"):
        # This should of course be read from the file
        self.work_book = openpyxl.load_workbook(excel_file)

        main_sheet = self.work_book['MAIN']

        start_range, end_range = main_sheet.calculate_dimension().split(':')

        first_col, row_start = re.findall(r'(\w+?)(\d+)', start_range)[0]
        # last_col, row_range = re.findall(r'(\w+?)(\d+)', end_range)[0]

        first_column_idx = column_index_from_string(first_col)
        print("first column idx -- {}".format(first_column_idx))
        self.values = []
        for row in main_sheet.rows:
            for cell in row:
                if cell.value is not None:
                    value = cell.value
                    col = cell.column - first_column_idx
                    self.values.append(Item(value, col))

        self.counter = 0

    def load_sheet_data(self, sheet_name):
        data_list = []
        selected_sheet = self.work_book[sheet_name]
        start_range, end_range = selected_sheet.calculate_dimension().split(':')

        first_col, row_start = re.findall(r'(\w+?)(\d+)', start_range)[0]
        last_col, row_end = re.findall(r'(\w+?)(\d+)', end_range)[0]
        max_column_idx = column_index_from_string(last_col)
        key_list = []

        for cell in selected_sheet[row_start]:
            if cell.value is not None:
                # print(cell.value)
                key_list.append(cell.value)
        # print(key_list)

        for row in selected_sheet.iter_rows(min_row=int(row_start) + 1, max_row=int(row_end), max_col=max_column_idx):
            new_dict = {}
            i = 0
            for cell in row:
                if cell.value is not None:
                    new_dict[key_list[i]] = cell.value
                    i = i + 1

            # print(new_dict)
            data_list.append(new_dict)

        return data_list

    def get_next(self):
        item = None
        if self.counter < len(self.values):
            item = self.values[self.counter]
            self.counter += 1

        return item

    def reset(self):
        self.counter = 0


def update_dictionary(data_lists, key, value='name'):
    updated_dict = {}
    key = re.sub('\W+', '', key)
    for data_list in data_lists:
        # print(asset_data)
        data_key = data_list[key]
        data_value = data_list[value]
        value_dict = dict()
        value_dict[data_value] = {}
        if data_key in updated_dict.keys():
            updated_dict[data_key].update(value_dict)
        else:
            updated_dict[data_key] = value_dict

    return updated_dict


# Process to generate the dictionary
def generate_dictionary(dic, prev):
    next = excel_reader.get_next()

    while next:
        if next.col < prev.col:
            return next

        if next.col == prev.col:
            dic[next.value] = {}
            prev = next
            next = excel_reader.get_next()

        elif next.col == prev.col + 1:
            dic[prev.value] = {next.value: {}}
            next = generate_dictionary(dic[prev.value], next)

        else:
            next = excel_reader.get_next()

    return None


def get_keys(dl, keys=None):
    keys = keys or []
    if isinstance(dl, dict):
        keys += dl.keys()
        _ = [get_keys(x, keys) for x in dl.values()]
    elif isinstance(dl, list):
        _ = [get_keys(x, keys) for x in dl]
    return list(set(keys))


def get_values(dl, key):

    if key in dl.keys():
        return dl[key].values()
    else:
        for d in dl.values():
            for k, v in d.items():
                print(k)
                if key == k:
                    return d[k]
                if isinstance(k,dict):

                    print("k {}".format(k))
                    val = get_values(k,key)
                    return val
                try:
                    int(key) == v
                    return k
                except ValueError:
                    continue
    return None

# def get_values(dl, keys):
#     values = [sub[keys] for sub in dl.values() if keys in sub.keys()]
#     return values

# Usage example
d = {}

excel_reader = ExcelReader()
root = excel_reader.get_next()

generate_dictionary(d, root)


# print(get_keys(d))

print(get_values(d, 'assets'))

print("\n\n")

print(" Before Asset type update d:  -- {}".format(d))

short_key = "[short_type]"
dict_keys = set()

if short_key in d["{ROOT}"]['data']['assets'].keys():
    asset_data_list = excel_reader.load_sheet_data("<ASSET>")
    data_dict = update_dictionary(asset_data_list, short_key)
    d["{ROOT}"]['data']['assets'].update(data_dict)
    d["{ROOT}"]['data']['assets'].pop(short_key, None)

sequence_key = "[sequence]"
if sequence_key in d["{ROOT}"]['shots'].keys():
    shot_data_list = excel_reader.load_sheet_data("<SHOT>")
    data_dict = update_dictionary(shot_data_list, sequence_key)
    d["{ROOT}"]['shots'].update(data_dict)
    d["{ROOT}"]['shots'].pop(sequence_key, None)

# print(d["{ROOT}"].keys())
print(" After Asset & Shot type update d:  -- {}".format(d))


# print(d["{ROOT}"])
print(get_values(d, "assets"))

with open('output.json', 'w') as json_file:
    json.dump(d, json_file, indent=4)
