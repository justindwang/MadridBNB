def initialize():
    global parsed_data
    parsed_data = []
    global line_count
    line_count = 0
    global total_price
    total_price = 0
    global num_listings
    num_listings = 0


    global avg_init
    avg_init = False
    global pop_listing_init
    pop_listing_init = False
    global pop_neighborhood_init
    pop_neighborhood_init = False
    global dist_init
    dist_init = False
    global madrid_dist_init
    madrid_dist_init = False

    global madrid_dist
    madrid_dist = None
    global room_distributions
    room_distributions = []
    global pop_listings
    pop_listings = []
    global pop_neighborhoods
    pop_neighborhoods = []

    global changed
    changed = False
    global pop_listing_changed
    pop_listing_changed = False

    # global delta_private
    # delta_private = 0
    # global delta_shared
    # delta_shared = 0
    # global delta_entire
    # delta_entire = 0
    # global delta_hotel
    # delta_hotel = 0