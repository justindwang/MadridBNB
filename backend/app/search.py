from flask import request, jsonify, make_response
from flask_restful import Resource
from .parser_listings import listings, search_listings, add_listing, edit_listing, remove_listing

class Listings(Resource):
    def post(self):
        if request.is_json:
            req = request.get_json()
            listings = search_listings(req.get('neighborhood'), req.get('roomType'), req.get('ceilprice'), req.get('floorprice'))
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