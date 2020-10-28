import os
import csv

class listings:
  id = 0
  neighborhood = ""
  room_type = ""
  price = 0

parsed_data = []

id_counter = 0

line_count = 0


# Opening file and setting up parser for read mode
with open('listings.csv', 'r') as csv_listings:
  parser = csv.reader(csv_listings)
  for row in parser:
      if line_count == 0:
#          print('ID, Neighborhood, Room Type, Price')
          line_count += 1
      else:
          x = listings()
#          print('ID:', row[0],'\tNeighborhood:', row[4], '\tRoom Type:', row[8], '\tPrice:', row[9])
          x.id = row[0]
          x.neighborhood = row[4]
          x.room_type = row[8]
          x.price = row[9]
#          print("ID:", x.id, "Neighborhood:", x.neighborhood, "Room Type:", x.room_type, "Price:", x.price)
          line_count += 1
          parsed_data.append(x)
#  count = 0
#  for i in parsed_data:
#    count += 1
#    print("ID:", parsed_data[count-1].id, "Neighborhood:", parsed_data[count-1].neighborhood, "Room Type:", parsed_data[count-1].room_type, "Price:", parsed_data[count-1].price)
#  print('Finished. Line count = ', line_count)




def search_listings(n, r, ceiling, floor):
  x = 0
  list = []
  for i in parsed_data:
    if n == parsed_data[x].neighborhood or n == None:
      if r == parsed_data[x].room_type or r == None:
        if parsed_data[x].price >= floor and parsed_data[x].price <= ceiling:
          list.append(parsed_data[x])
          x += 1
  return list


def add_listing(neighborhood, room_type, price):
  id_counter += 1
  x = listings()
  x.id = id_counter
  x.neighborhood = neighborhood
  x.room_type = room_type
  x.price = price
  parsed_data.append(x)
  new_listing = [x.id, '1', '2', '3', '4', neighborhood, '6', '7', room_type, price, '10', '11', '12', '13', '14', '15']
  with open('listings.csv', 'a') as csv_listings:
    writer = csv.writer(csv_listings)
    writer.writerow(new_listing)
  return x


def edit_listing(id, neighborhood, room_type, price):
  x = 0
  for i in parsed_data:
    if id == parsed_data[x].id:
      parsed_data[x].neighborhood = neighborhood
      parsed_data[x].room_type = room_type
      parsed_data[x].price = price
      return parsed_data[x]
    else:
      x += 1
  with open('listings.csv', 'w') as csv_listings:
    parser = csv.writer(csv_listings)
    for row in parser:
      if row[0] == id:
        new_listing = [id, row[1], row[2], row[3], row[4], neighborhood, row[6], row[7], room_type, price, row[10], row[11], row[12], row[13], row[14], row[15]]
        parser.writerow(new_listing)





def delete_listing(id):
  x = 0
  for i in parsed_data:
    if id == parsed_data[x].id:
      parsed_data.pop(x)
    else:
      x += 1
  with open('listings.csv', 'w') as csv_listings:
    parser = csv.writer(csv_listings)
    for row in parser:
      if row[0] == id:
        new_listing = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        parser.writerow(new_listing)

      






















