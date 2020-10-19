from flask import request, jsonify, make_response
from flask_restful import Resource

class Listings(Resource):
    def post(self):
        if request.is_json:
            req = request.get_json()
            #listings = <PARSER>.search_listings(req.get(neighborhood), req.get(roomType), req.get(priceRange))
            #sets 'listings' variable to the the expected returned array of Listing objects that meet search criteria (search_listings())
            response = {
                "listings": []
            }
            # for x in listings:
            #     temp = {
                    # "id": x.get_id(),
                    # "neighborhood": x.get_neighborhood(),
                    # "roomType": x.get_roomType(),
                    # "price": x.get_price()
                    # Accessors for each variable stored in a Listing Object
            #     }
            #     response['Listings'].append(temp)

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
            # for x in reviews:
            #     temp = {
                    # "listing_id": x.get_listing_id(),
                    # "id": x.get_id(),  
                    # "date": x.get_date(),
                    # "reviewerName": x.get_reviewer_name(),
                    # "comments": x.get_comments()
                    # Accessors for each variable stored in a Review Object
            #     }
            #     response['Listings'].append(temp)
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
            # for x in neighborhoods:
            #     temp = {
                    # "neighborhoodGroup": x.get_neighborhood_group(),
                    # "neighborhood": x.get_neighborhood()
                    # Accessors for each variable stored in a Neighborhood Object
            #     }
            #     response['Listings'].append(temp)
            res = make_response(jsonify(response), 200)
            return res
        else:
            return "No JSON received", 400