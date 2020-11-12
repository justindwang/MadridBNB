from flask import request, jsonify, make_response
from flask_restful import Resource
from .parser_listings import listings, search_listings, add_listing, edit_listing, remove_listing, get_average, get_cheap3, get_expensive3, get_popular_madrid, get_room_madrid, get_popular_neighborhood, get_room_pop_neighborhoods

class Listings(Resource):
    def post(self):
        if request.is_json:
            req = request.get_json()
            listings = search_listings(req.get('neighborhood'), req.get('roomType'), req.get('ceilprice'), req.get('floorprice'))
            #sets 'listings' variable to the the expected returned array of Listing objects that meet search criteria (search_listings())
            response = {
                "listings": [],
                "average_price": 0,
                "cheap_listings": [],
                "expensive_listings": []
            }
            # dictionary that holds an array of dictionaries, each containing data of a single listing
            # e.g. access listing data "id" of 1st entry - response["listings"][0]["id"]

            for x in listings:
                temp = {
                    "id": x.id,
                    "neighborhood": x.neighborhood,
                    "roomType": x.room_type,
                    "price": x.price
                    # Accessors for each variable stored in a Listing Object
                }
                response['listings'].append(temp)

            response['average_price'] = get_average(listings)

            cheap3 = get_cheap3(listings)
            for x in cheap3:
                temp1 = {
                    "id": x.id,
                    "neighborhood": x.neighborhood,
                    "roomType": x.room_type,
                    "price": x.price
                    # Accessors for each variable stored in a Listing Object
                }
                response['cheap_listings'].append(temp1)

            expensive3 = get_expensive3(listings)
            for x in expensive3:
                temp2 = {
                    "id": x.id,
                    "neighborhood": x.neighborhood,
                    "roomType": x.room_type,
                    "price": x.price
                    # Accessors for each variable stored in a Listing Object
                }
                response['expensive_listings'].append(temp2)
            
            res = make_response(jsonify(response), 200)
            res.headers.add('Access-Control-Allow-Origin', '*')
            return res
        else:
            return "No JSON received", 400

class AddListing(Resource):
    def post(self):
        if request.is_json:
            req = request.get_json()
            add_listing(req.get('neighborhood'), req.get('roomType'), req.get('price'))
            # expected add listing function that adds listing to csv file given passed neighborhood, roomType, and price parameters
            res = make_response(jsonify({}),200)
            res.headers.add('Access-Control-Allow-Origin', '*')
            return res
        else:
            return "No JSON received", 400

class RemoveListing(Resource):
    def post(self):
        if request.is_json:
            req = request.get_json()
            remove_listing(req.get('id'))
            # expected remove listing function that removes a listing from csv file given passed listing id
            res = make_response(jsonify({}), 200)
            res.headers.add('Access-Control-Allow-Origin', '*')
            return res
        else:
            return "No JSON received", 400

class EditListing(Resource):
    def post(self):
        if request.is_json:
            req = request.get_json()
            edit_listing(req.get('id'), req.get('neighborhood'), req.get('roomType'), req.get('price'))
            # expected edit listing function that edits a listing from csv file given passed parameters
            res = make_response(jsonify({}), 200)
            res.headers.add('Access-Control-Allow-Origin', '*')
            return res
        else:
            return "No JSON received", 400

class Analytics(Resource):
    def post(self):
        # if request.is_json:
        #     req = request.get_json()
        pop_listings = get_popular_madrid()
        madrid_dist = get_room_madrid()
        pop_neighborhoods = get_popular_neighborhood()
        neighborhood_room_dist = get_room_pop_neighborhoods(pop_neighborhoods)
        # 1 dictionary with 3 keys to 3 lists of room dist objects
        # expected add listing function that adds listing to csv file given passed neighborhood, roomType, and price parameters
        response = {
            "top_neighborhoods": [],
            "top_listings": [],
            "room_dist_data": []
        }
        for x in pop_listings:
            temp = {
                "id": x.id,
                "neighborhood": x.neighborhood,
                "roomType": x.room_type,
                "price": x.price,
                "reviews": x.reviews
                # Accessors for each variable stored in a Listing Object
            }
            response['top_listings'].append(temp)

        for y in pop_neighborhoods:
            temp2 = {
                "neighborhood": y.neighborhood,
                "reviews": y.reviews,
                # Accessors for each variable stored in a Rooms Object
            }
            response['top_neighborhoods'].append(temp2)

        # response['room_dist_data'].append({"Madrid": []})
        temp3 = {
                "neighborhood": madrid_dist.neighborhood,
                "shared_count": madrid_dist.shared_count,
                "private_count": madrid_dist.private_count,
                "entire_count": madrid_dist.entire_count,
                "hotel_count": madrid_dist.hotel_count
                # Accessors for each variable stored in a room_dist Object
            }
        response['room_dist_data'].append(temp3)
        for z in neighborhood_room_dist:
            temp4 = {
                "neighborhood": z.neighborhood,
                "shared_count": z.shared_count,
                "private_count": z.private_count,
                "entire_count": z.entire_count,
                "hotel_count": z.hotel_count
                # Accessors for each variable stored in a Listing Object
            }
            response['room_dist_data'].append(temp4)
        
        res = make_response(jsonify(response), 200)
        res.headers.add('Access-Control-Allow-Origin', '*')
        return res
        # else:
        #     return "No JSON received", 400

class Reviews(Resource):
    def post(self):
        if request.is_json:
            req = request.get_json()
            #reviews = <PARSER>.search_reviews(req.get(listing_id))
            #sets 'reviews' variable to the the expected returned array of Review objects that meet search criteria (search_reviews())
            response = {
                "reviews": []
            }
            # dictionary that holds an array of dictionaries, each containing data of a single review
            # e.g. access review data "id" of 1st entry - response["reviews"][0]["id"]

            # for x in reviews:
            #     temp = {
                    # "listing_id": x.get_listing_id(),
                    # "id": x.get_id(),  
                    # "date": x.get_date(),
                    # "reviewerName": x.get_reviewer_name(),
                    # "comments": x.get_comments()
                    # Accessors for each variable stored in a Review Object
            #     }
            #     response['reviews'].append(temp)
            res = make_response(jsonify(response), 200)
            return res
        else:
            return "No JSON received", 400

class AddReview(Resource):
    def post(self):
        if request.is_json:
            req = request.get_json()
            # add_review(req.get('listing_id'), req.get('comment'))
            # expected add review function that adds review to csv file given passed listing id and comment parameters
            res = make_response(200)
            res.headers.add('Access-Control-Allow-Origin', '*')
            return res
        else:
            return "No JSON received", 400

class RemoveReview(Resource):
    def post(self):
        if request.is_json:
            req = request.get_json()
            # remove_listing(req.get('listing_id'))
            # expected remove review function that removes a review from csv file given passed listing id
            res = make_response(200)
            res.headers.add('Access-Control-Allow-Origin', '*')
            return res
        else:
            return "No JSON received", 400

class EditReview(Resource):
    def post(self):
        if request.is_json:
            req = request.get_json()
            # edit_listing(req.get('listing_id'), req.get('listing_id'), req.get('comment'))
            # expected edit review function that edits a review from csv file given passed parameters
            res = make_response(200)
            res.headers.add('Access-Control-Allow-Origin', '*')
            return res
        else:
            return "No JSON received", 400

class Neighborhoods(Resource):
    def post(self):
        if request.is_json:
            req = request.get_json()
            #neighborhoods = <PARSER>.search_neighborhoods(req.get(neighborhoodName), req.get(neighborhoodGroup))
            
            response = {
                "neighborhoods": []
            }
            # dictionary that holds an array of dictionaries, each containing data of a single neighborhood
            # e.g. access neighborhood data "neighborhoodGroup" of 1st entry - response["neighborhoods"][0]["neighborhoodGroup"]

            # for x in neighborhoods:
            #     temp = {
                    # "neighborhoodGroup": x.get_neighborhood_group(),
                    # "neighborhood": x.get_neighborhood()
                    # Accessors for each variable stored in a Neighborhood Object
            #     }
            #     response['neighborhoods'].append(temp)
            res = make_response(jsonify(response), 200)
            return res
        else:
            return "No JSON received", 400