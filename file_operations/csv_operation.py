# CSV -> Comma Separated Values
# CSV is a simple file format used to store tabular data, such as a spreadsheet or database. Files in the CSV format can be imported to and exported from programs that store data in tables, such as Microsoft Excel.
# import csv
# with open("test.csv", mode="w", newline="") as f:
#     writer = csv.writer(f, delimiter=",")
#     writer.writerow( ["Name", "City"] )
#     writer.writerow( ["Craig Lou", "Taiwan"] )

# The newline parameter controls how newlines are handled when opening files in text mode. For most text files, you can ignore it, but when working with structured formats like CSVs, using newline="" ensures proper formatting without unintended extra lines.

import csv

data = {
'name' : ['Dave', 'Dennis', 'Peter', 'Jess'],
'language': ['Python', 'C', 'Java', 'Python']
}

name_data = data['name']
language_data = data['language']

with open("test.csv", mode="w", newline="") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow( ["Name", "Language"] )
    for i in range(len(name_data)):
        writer.writerow( [name_data[i], language_data[i]] )