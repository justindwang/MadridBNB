from flask import request, jsonify, make_response
from flask_restful import Resource
from .parser_listings import listings, search_listings

class Listings(Resource):
    def post(self):
        if request.is_json:
            req = request.get_json()
            listings = search_listings(req.get('neighborhood'), req.get('roomType'), req.get('priceRangeHigh'), req.get('priceRangeLow'))
            #sets 'listings' variable to the the expected returned array of Listing objects that meet search criteria (search_listings())
            response = {
                "listings": []
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

            res = make_response(jsonify(response), 200)
            return res
        else:
            return "No JSON received", 400

class Reviews(Resource):
    def post(self):
        if request.is_json:
            req = request.get_json()
            #reviews = <PARSER>.search_reviews(req.get(dateRange), req.get(reviewerName))
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