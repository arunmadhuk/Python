import openpyxl
from openpyxl.utils import column_index_from_string
import re
import json


# Working class to contain an "item" (value, column)
class Item:
    def __init__(self, value, col):
        self.value = value
        self.col = col


# Excel reader class
class ExcelReader:
    #TODO: don't set excel file name a default
    #TODO: add main sheet name as param?
    def __init__(self, excel_file="template.xlsx"):
        self.counter = 0
        self.values = []

        self.work_book = openpyxl.load_workbook(excel_file)
        self.get_values()

    def get_values(self):
        main_sheet = self.work_book['MAIN']
        data_range = main_sheet.calculate_dimension()
        data = main_sheet[data_range]

        # Check that first cell is not empty
        #TODO: should check if is "root" or "project" or something specific...
        if not data[0][0].value:
            #TODO: print better error
            print("Error: first cell not root")
            return

        first_column_idx = data[0][0].column

        self.values = []
        for row in data:
            for cell in row:
                if cell.value is not None:
                    value = cell.value
                    col = cell.column - first_column_idx
                    self.values.append(Item(value, col))
                    # Only 1 value per row, rest is ignored
                    break

        return self.values


    def load_sheet(self, sheet_name):
        data_list = []
        selected_sheet = self.work_book[sheet_name]
        data_range = selected_sheet.calculate_dimension()

        # Get column titles
        key_list = []
        for column_title in selected_sheet[data_range][0]:
            # Stop at first "None" value
            if not column_title.value:
                break
            key_list.append(column_title.value)

        # Create dictionary for each row of table
        for row in selected_sheet[data_range][1:]:
            # Stop at first row starting with "None" value
            if not row[0].value:
                break

            new_dict = {}
            for i in range(len(key_list)):
                cell = row[i]
                new_dict[key_list[i]] = cell.value

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


"""
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
"""


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
            # DEREK: don't change "prev", we need to keep the current one
            # prev = next
            next = excel_reader.get_next()

    return None


# Usage example
d = {}

excel_reader = ExcelReader()
root = excel_reader.get_next()

generate_dictionary(d, root)
print(" Before Asset type update d:  -- {}".format(d))

"""
# DEREK: should not have anything hardcoded, it is supposed to be fully dynamic (if not, there is no point in having a script...)
# Also, you check for example if there is the [short_type] element, and if not you skip the whole "asset" part. This doesn't work, [short_type] doesn't have to be there.
# => The process is here is much more complex, we need to handle several levels of tags with maybe different parents.
# I will do it.

short_key = "[short_type]"
dict_keys = set()

if short_key in d["{ROOT}"]['data']['assets'].keys():
    asset_data_list = excel_reader.load_sheet("<ASSET>")
    print("asset_data_list {}".format(asset_data_list))
    data_dict = update_dictionary(asset_data_list, short_key)
    d["{ROOT}"]['data']['assets'].update(data_dict)
    d["{ROOT}"]['data']['assets'].pop(short_key, None)

sequence_key = "[sequence]"
if sequence_key in d["{ROOT}"]['shots'].keys():
    shot_data_list = excel_reader.load_sheet("<SHOT>")
    data_dict = update_dictionary(shot_data_list, sequence_key)
    d["{ROOT}"]['shots'].update(data_dict)
    d["{ROOT}"]['shots'].pop(sequence_key, None)

print(" After Asset & Shot type update d:  -- {}".format(d))

with open('output.json', 'w') as json_file:
    json.dump(d, json_file, indent=4)
"""



TODO: CONTINUE FROM HERE
- read "mtachings" in each table, a use that instead of current method
    => look at "*CHANGE THIS"
- start from 0 in each "for entry in data[1:]:"
    ("for entry in data:")




####
def get_tag_values(type, dic_path):
    data = excel_reader.load_sheet(type)
    print("sheet data: {}".format(data))
    children = set()


    """
    #TODO: CHANGE "x" VALUE!
    print("TYPE-2: {}".format(type))
    if type != "x":
        first = data[0]
        for key in first:
            if first[key] == type:
                dtype = key
                break
        #else:
        #    error?
    print("TYPE-3: {}".format(dtype))
    """

    print("dic_path-sub: {}".format(dic_path))
    #for entry in data:
    for entry in data[1:]:
        #children.append(entry["name"])

        for pair in dic_path:


*CHANGE THIS
            if pair[0][0] == "<" and pair[0][-1] == ">":
                dtype = None
                # get name of column
                first = data[0]
                for key in first:
                    if first[key] == pair[0]:
                        dtype = key
                        break
                #else:
                #    error?

                if dtype:
                    print("TYPE-3: {}".format(dtype))

                    if pair[1] != entry[dtype]:
                        break


            elif pair[0] in entry.keys():
                print("entry[pair[0]]: " + entry[pair[0]])
                if pair[1] != entry[pair[0]]:
                    break
        else:
            children.add(entry["name"])

    return list(children)
####

# find in children, first with column that name (+look in brothers)
# & get all values
# ...
def get_values(dic, type, dic_path):
    values = set()
    print("TYPE: {}".format(type))
    for key in dic:
        if key[0] != "<" or key[-1] != ">":
            continue

        # Get values
        tag_values = get_tag_values(key, dic_path)
        print("tag_values - sub: {}".format(tag_values))

        data = excel_reader.load_sheet(key)
        sub_values = set()
        for entry in data[1:]:
            if type in entry:
                sub_values.add(entry[type])

        if not sub_values:
            #TODO: need to extend dic_path?
            sub_values = get_values(dic[key], type, dic_path)

        values.update(sub_values)

    return list(values)



def fct(dic, dic_path=[]):
    out_dic = {}

    for item in dic:
        print("item: {}".format(item))

        values = []

        #TODO: handle error cases
        if item[0] == "[" and item[-1] == "]":

            fields = item[1:-1].split(":")
            if len(fields) == 2:
                values = [ fields[1] ]
                type = fields[0]
            else:
                type = fields[0]
                values = get_values(dic[item], type, dic_path)
                print("VALUES: {}".format(values))

        elif item[0] == "<" and item[-1] == ">":

            type = item
            values = get_tag_values(type, dic_path)
            print("tag_values: {}".format(values))

        else:
            values = [ item ]
            #type = item # or None?
            type = None


        #print("values, type: {}, {}".format(values, type))


        for value in values:
            out_dic[value] = { "type": type }

            #sub_dict = fct(dic[item])
            if type:
                sub_dict = fct(dic[item], dic_path + [ (type, value) ])
            else:
                sub_dict = fct(dic[item], dic_path)
            #print("sub_dict: {}".format(sub_dict))

            out_dic[value]["children"] = sub_dict


    #print("out_dic: {}".format(out_dic))
    return out_dic



dicc = fct(d)

with open('output.json', 'w') as json_file:
    json.dump(dicc, json_file, indent=4)
