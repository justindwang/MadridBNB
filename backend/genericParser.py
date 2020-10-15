import csv
def genericParser(filename):
  fields = []
  # Opening file and setting up parser for read mode
  with open(filename, 'r') as csv_file:
    parser = csv.reader(csv_file)
    # Getting column names
    for column in parser:
      fields[column] = next(parser)
    # Getting information in each column
    # This depends on the format of the individual csv file
    for x in fields:
