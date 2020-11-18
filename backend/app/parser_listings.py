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

class room_distribution:
  neighborhood = ""
  shared_count = 0
  private_count = 0
  entire_count = 0
  hotel_count = 0

class popular_n:
  neighborhood = ""
  reviews = 0

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
            x.reviews = row[11]
  #          print("ID:", x.id, "Neighborhood:", x.neighborhood, "Room Type:", x.room_type, "Price:", x.price)
            globals.line_count += 1
            globals.parsed_data.append(x)
  # count = 0
  # for i in globals.parsed_data:
  #   count += 1
  #   print("ID:", globals.parsed_data[count-1].id, "Neighborhood:", globals.parsed_data[count-1].neighborhood, "Room Type:", globals.parsed_data[count-1].room_type, "Price:", globals.parsed_data[count-1].price)
  #   print('Finished. Line count = ', count)


def get_popular_neighborhood():
  if not globals.pop_neighborhood_init:
    globals.pop_neighborhood_init = True
    counter1 = 0
    n_list = []

    for i in globals.parsed_data:
      counter2 = 0
      flag = 0
      if counter1 == 0:
        x = popular_n()
        x.neighborhood = globals.parsed_data[counter1].neighborhood
        x.reviews += int(globals.parsed_data[counter1].reviews)
        n_list.append(x)
      else:
        for j in n_list:
          if globals.parsed_data[counter1].neighborhood == n_list[counter2].neighborhood:
            n_list[counter2].reviews += int(globals.parsed_data[counter1].reviews)
            flag = 1
            break
          else:
            counter2 += 1
        if flag == 0:
          x = popular_n()
          x.neighborhood = globals.parsed_data[counter1].neighborhood
          x.reviews += int(globals.parsed_data[counter1].reviews)
          n_list.append(x)
      counter1 += 1     


    popular = [None, None, None]
    newlist = sorted(n_list, key=lambda x: int(x.reviews), reverse=False)
    y = 0
    for i in newlist:
      if y == 3:
          break
      popular[y] = newlist[len(newlist)-(y+1)]
      y += 1
    globals.pop_neighborhoods = popular
    return globals.pop_neighborhoods
  else:
    return globals.pop_neighborhoods

def get_room_madrid():
  if not globals.madrid_dist_init:
    globals.madrid_dist_init = True
    counter = 0
    madrid_dist = room_distribution()
    madrid_dist.neighborhood = "Madrid"

    for i in globals.parsed_data:
      if globals.parsed_data[counter].room_type == "Private room":
        madrid_dist.private_count += 1
      if globals.parsed_data[counter].room_type == "Shared room":
        madrid_dist.shared_count += 1
      if globals.parsed_data[counter].room_type == "Entire home/apt":
        madrid_dist.entire_count += 1
      if globals.parsed_data[counter].room_type == "Hotel room":
        madrid_dist.hotel_count += 1
      counter += 1
    globals.madrid_dist = madrid_dist
    return globals.madrid_dist
  else:
    return globals.madrid_dist

def get_room_pop_neighborhoods(pop_neighborhoods):
  if not globals.pop_neighborhood_init: 
    globals.pop_neighborhood_init = True
    x = 0
    list_room_dists = []
    for i in pop_neighborhoods:
      counter = 0

      room_dist = room_distribution()
      room_dist.neighborhood = pop_neighborhoods[x].neighborhood

      for j in globals.parsed_data:
        if globals.parsed_data[counter].neighborhood == room_dist.neighborhood:
          if globals.parsed_data[counter].room_type == "Private room":
            room_dist.private_count += 1
          if globals.parsed_data[counter].room_type == "Shared room":
            room_dist.shared_count += 1
          if globals.parsed_data[counter].room_type == "Entire home/apt":
            room_dist.entire_count += 1
          if globals.parsed_data[counter].room_type == "Hotel room":
            room_dist.hotel_count += 1
        counter += 1
      list_room_dists.append(room_dist)
      x += 1
    globals.room_distributions = list_room_dists
    return globals.room_distributions
  else:
    return globals.room_distributions

def get_popular_madrid():
  if not globals.pop_listing_init: 
    globals.pop_listing_init = True
    popular = [None, None, None]
    newlist = sorted(globals.parsed_data, key=lambda x: int(x.reviews), reverse=False)
    y = 0
    for i in newlist:
      if y == 3:
          break
      popular[y] = newlist[len(newlist)-(y+1)]
      y += 1
    globals.pop_listings = popular
    return globals.pop_listings
  else:
    # if globals.changed:
      
    # else:
      return globals.pop_listings


def get_average(list):
  x = 0
  numerator = 0
  denominator = 0
  for i in list:
    numerator += int(list[x].price)
    denominator += 1
    x += 1
  average = numerator / denominator
  return round(average, 2)

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


