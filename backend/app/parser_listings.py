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
  reviews = 0

class rooms:
  name = ""
  tally = 0

class popular_n:
  neighborhood = ""
  tally = 0

# parsed_data = []


# line_count = 0


# Opening file and setting up parser for read mode
def run_parser():
  with codecs.open("app/listings.csv", "r", encoding="utf-8", errors='ignore') as csv_listings:
    parser = csv.reader(csv_listings)
    for row in parser:
        if globals.line_count == 0:
            globals.line_count += 1
        else:
          if row:
            x = listings()
            x.id = row[0]
            x.neighborhood = row[5]
            x.room_type = row[8]
            x.price = row[9]
            x.reviews = row[11]
            globals.line_count += 1
            globals.parsed_data.append(x)

def get_popular_neighborhood():
  counter1 = 0
  n_list = []

  for i in globals.parsed_data:
    counter2 = 0
    flag = 0
    if counter1 == 0:
      x = popular_n()
      x.neighborhood = globals.parsed_data[counter1].neigborhood
      x.tally += globals.parsed_data[counter1].reviews
      n_list.append(x)
    else:
      for j in n_list:
        if globals.parsed_data[counter1].neighborhood == n_list[counter2].neighborhood:
          n_list[counter2].tally += globals.parsed_data[counter1].reviews
          flag = 1
          break
        else:
          counter2 += 1
      if flag == 0:
        x = popular_n()
        x.neighborhood = globals.parsed_data[counter1].neigborhood
        x.tally += globals.parsed_data[counter1].reviews
        n_list.append(x)
    counter1 += 1     

  popular = [None, None, None]
  newlist = sorted(n_list, key=lambda x: int(x.tally), reverse=False)
  y = 0
  for i in newlist:
    if y == 3:
        break
    popular[y] = newlist[len(newlist)-(y+1)]
    y += 1
  return popular


def get_room_madrid():
  room_count = []
  a = rooms()
  a.name = "Private room"
  b = rooms()
  b.name = "Shared room"
  c = rooms()
  c.name = "Entire home/apt"
  d = rooms()
  d.name = "Hotel room"
  room_count.append(a)
  room_count.append(b)
  room_count.append(c)
  room_count.append(d)
  counter = 0

  for i in globals.parsed_data:
    if globals.parsed_data[counter].room_type == "Private room":
      room_count[0].tally += 1
    if globals.parsed_data[counter].room_type == "Shared room":
      room_count[1].tally += 1
    if globals.parsed_data[counter].room_type == "Entire home/apt":
      room_count[2].tally += 1
    if globals.parsed_data[counter].room_type == "Hotel room":
      room_count[3].tally += 1
    counter += 1

  return room_count


def get_popular_madrid():
  popular = [None, None, None]
  newlist = sorted(globals.parsed_data, key=lambda x: int(x.reviews), reverse=False)
  y = 0
  for i in newlist:
    if y == 3:
        break
    popular[y] = newlist[len(newlist)-(y+1)]
    y += 1
  return popular


def average_price(list):
  x = 0
  numerator = 0
  denominator = 0
  for i in list:
    numerator += list[x].price
    denominator += 1
    x += 1
  average = numerator / denominator
  return average

def get_expensive3(list):
  high = [None, None, None]
  newlist = sorted(list, key=lambda x: int(x.price), reverse=False)
  y = 0
  for i in newlist:
    if y == 3:
        break
    high[y] = newlist[len(newlist)-(y+1)]
    y += 1
  return high

def get_cheap3(list):
  low = [None, None, None]
  newlist = sorted(list, key=lambda x: int(x.price), reverse=False)
  y = 0
  for i in newlist:
    if y == 3:
      break
    low[y] = newlist[y]
    y += 1
  return low


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
      print("Stdexp error")
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
          break
      index_to_remove += 1
    csv_listings.seek(0)
    contents = csv_listings.readlines()
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


