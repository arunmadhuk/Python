import os
import json

cwd = os.getcwd()

full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)

airticket_json_file = os.path.join(path,"airTicketListResponse.json")
# airport_v1_json_file = os.path.join(path,"airportv1_formatted.json")
# print(airport_json_file)
with open(airticket_json_file) as json_data:
    airportData = json.load(json_data)

# with open(airport_v1_json_file) as json_v1_data:
#     airportDatasv1 = json.load(json_v1_data)

# print(airportData)

with open('airTicketListResponse.json', 'w') as f:
    json.dump(airportData, f, indent=4, sort_keys=True)