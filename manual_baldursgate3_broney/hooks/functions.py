import os
import pkgutil
import csv
import re

from io import StringIO

# we have to get the raw data from our CSV files to pass to a parser, so had to copy our own version of this method
# this gets the contents of the file from pkgutil and passes it back as a "file" for csv parsing later
def get_csv_file(*args) -> dict:
    fname = os.path.join("data", *args)
    package_base_name = re.sub(r'\.hooks\.\w+$', '.Data', __name__)
    try:
        filedata = pkgutil.get_data(package_base_name, fname).decode()
    except:
        filedata = ""
    return StringIO(filedata)

def get_rare_items() -> list:
    pack_data_file = 'rareitems.csv' # has the list of available packs
    rows = []
    with get_csv_file(pack_data_file) as opened_file:
        reader = csv.DictReader(opened_file)
        for row in reader:
            rows.append(row)
    return rows

def get_quest_locations(include_missable: bool) -> list:
    pack_data_file = 'templocations.csv' # has the list of available packs
    rows = []
    with get_csv_file(pack_data_file) as opened_file:
        reader = csv.DictReader(opened_file)
        for row in reader:
            if include_missable or row['ProgAllowed'] == 'TRUE':
                rows.append(row)
    return rows