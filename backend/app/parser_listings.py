import os
import csv
import io
import re
import codecs
from app import globals

class listings:
  id = 0
  neighborhood = ""
  room_type = ""
  price = 0

# parsed_data = []


# line_count = 0


# Opening file and setting up parser for read mode
def run_parser():
  with codecs.open("app/listings.csv", "r", encoding="utf-8", errors='ignore') as csv_listings:
    parser = csv.reader(csv_listings)
    for row in parser:
        if globals.line_count == 0:
            # print('ID, Neighborhood, Room Type, Price')
            globals.line_count += 1
        else:
          if row:
            x = listings()
            # print('ID:', row[0],'\tNeighborhood:', row[5], '\tRoom Type:', row[8], '\tPrice:', row[9])
            x.id = row[0]
            x.neighborhood = row[5]
            x.room_type = row[8]
            x.price = row[9]
  #          print("ID:", x.id, "Neighborhood:", x.neighborhood, "Room Type:", x.room_type, "Price:", x.price)
            globals.line_count += 1
            globals.parsed_data.append(x)
  # count = 0
  # for i in globals.parsed_data:
  #   count += 1
  #   print("ID:", globals.parsed_data[count-1].id, "Neighborhood:", globals.parsed_data[count-1].neighborhood, "Room Type:", globals.parsed_data[count-1].room_type, "Price:", globals.parsed_data[count-1].price)
  #   print('Finished. Line count = ', count)




def search_listings(n, r, ceiling, floor):
  x = 0
  myList = []
  if ceiling == None or floor == None:
    return myList
  for i in globals.parsed_data:
    if n == globals.parsed_data[x].neighborhood or n == None or n == "":
      if r == globals.parsed_data[x].room_type or r == None:
        if int(globals.parsed_data[x].price) >= floor and int(globals.parsed_data[x].price) <= ceiling:
          myList.append(globals.parsed_data[x])
    x += 1
  return myList

def add_listing(neighborhood, room_type, price):
  with codecs.open('app/id.txt', 'r', encoding="utf-8", errors='ignore') as f:
    id_counter = int(f.read())
  id_counter += 1
  with codecs.open('app/id.txt', 'w', encoding="utf-8", errors='ignore') as f:
    f.write(str(id_counter))
  x = listings()
  x.id = str(id_counter)
  x.neighborhood = neighborhood
  x.room_type = room_type
  x.price = price
  globals.parsed_data.append(x)
  new_listing = [x.id, '1', '2', '3', '4', x.neighborhood, '6', '7', x.room_type, x.price, '10', '11', '12', '13', '14', '15']
  with codecs.open("app/listings.csv", 'a', encoding="utf-8", errors='ignore') as csv_listings:
    writer = csv.writer(csv_listings)
    writer.writerow(new_listing)
  return x

def edit_listing(id, neighborhood, room_type, price):
  x = 0
  for i in globals.parsed_data:
    if id == int(globals.parsed_data[x].id):
      globals.parsed_data[x].neighborhood = neighborhood
      globals.parsed_data[x].room_type = room_type
      globals.parsed_data[x].price = price
    else:
      x += 1
  index_to_edit = 0
  with codecs.open("app/listings.csv", 'r', encoding="utf-8", errors='ignore') as csv_listings:
    parser = csv.reader(csv_listings)
    for row in parser:
      if row[0] and row[0].isdigit():
        if int(row[0]) == id:
          break
      index_to_edit += 1
    csv_listings.seek(0)
    contents = csv_listings.readlines()
    try:
      contents.pop(index_to_edit)
    except:
      print(index_to_edit)
      print(contents[index_to_edit-1])
    new_listing = str(id)+','+row[1]+','+row[2]+','+row[3]+','+row[4]+','+neighborhood+','+row[6]+','+row[7]+','+room_type+','+str(price)+','+row[10]+','+row[11]+','+row[12]+','+row[13]+','+row[14]+','+row[15]+'\n'
    contents.insert(index_to_edit, new_listing)
    contents = "".join(contents)
    with codecs.open("app/listings.csv", "w", encoding="utf-8", errors='ignore') as f:
      f.write(contents)
    # for row in parser:
    #   if row[0] == id:
    #     new_listing = [id, row[1], row[2], row[3], row[4], neighborhood, row[6], row[7], room_type, price, row[10], row[11], row[12], row[13], row[14], row[15]]
    #     parser.writerow(new_listing)

def remove_listing(id):
  x = 0
  for i in globals.parsed_data:
    if id == int(globals.parsed_data[x].id):
      globals.parsed_data.pop(x)
    else:
      x += 1
  index_to_remove = 0
  with codecs.open("app/listings.csv", "r", encoding="utf-8", errors='ignore') as csv_listings:
    parser = csv.reader(csv_listings)
    for row in parser:
      if row[0] and row[0].isdigit():
        if int(row[0]) == id:
          print(row[0])
          print(id)
          break
      index_to_remove += 1
    csv_listings.seek(0)
    contents = csv_listings.readlines()
    print(index_to_remove)
    contents.pop(index_to_remove)
    contents = "".join(contents)
    with codecs.open("app/listings.csv", "w", encoding="utf-8", errors='ignore') as f:
      f.write(contents)
  # with open("app/test.csv", 'w') as csv_listings:
  #   parser = csv.writer(csv_listings)
  #   for row in parser:
  #     if row[0] == id:
  #       new_listing = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
  #       parser.writerow(new_listing)


