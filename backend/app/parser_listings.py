import os
import csv
import io
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
  with open("app/listings.csv", "r", encoding="utf-8") as csv_listings:
    parser = csv.reader(csv_listings)
    for row in parser:
        if globals.line_count == 0:
            # print('ID, Neighborhood, Room Type, Price')
            globals.line_count += 1
        else:
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
    if n == globals.parsed_data[x].neighborhood or n == None:
      if r == globals.parsed_data[x].room_type or r == None:
        if int(globals.parsed_data[x].price) >= floor and int(globals.parsed_data[x].price) <= ceiling:
          myList.append(globals.parsed_data[x])
    x += 1
  return myList


