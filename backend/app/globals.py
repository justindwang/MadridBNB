def initialize():
    global parsed_data
    parsed_data = []
    global line_count
    line_count = 0

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