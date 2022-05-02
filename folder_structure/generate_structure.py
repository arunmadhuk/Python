import openpyxl
from openpyxl.utils import column_index_from_string
import re


# Working class to contain an "item" (value, column)
class Item:
    def __init__(self, value, col):
        self.value = value
        self.col = col


# Example Excel reader class
class ExcelReader:
    def __init__(self, excel_file="template.xlsx"):
        # This should of course be read from the file
        work_book = openpyxl.load_workbook(excel_file)

        main_sheet = work_book['MAIN']
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
                    print("Item col --- {} value -- {}".format(col, value))
                    self.values.append(Item(value, col))

        print(len(self.values))

        # self.values = [
        #     Item("root", 0),
        #     Item("data", 1),
        #     Item("assets", 2),
        #     Item("char", 3),
        #     Item("prop", 3),
        #     Item("env", 3),
        #     Item("shots", 2),
        #     Item("prod", 1)
        # ]
        # print(self.values)
        self.counter = 0

    def get_next(self):
        item = None
        if self.counter < len(self.values):
            item = self.values[self.counter]
            self.counter += 1

        return item

    def reset(self):
        self.counter = 0


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
            prev = next
            next = excel_reader.get_next()

    return None


# Usage example
d = {}

excel_reader = ExcelReader()
root = excel_reader.get_next()

generate_dictionary(d, root)
print("d: {}".format(d))
