# from flask import Flask, render_template, redirect, url_for, flash, request, jsonify, make_response
# from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from .search import Listings, Reviews, Neighborhoods, AddListing, RemoveListing, EditListing, AddReview, RemoveReview, EditReview, Analytics

def initialize_routes(api):
    api.add_resource(Listings, "/listings")
    api.add_resource(AddListing, "/listings/add")
    api.add_resource(RemoveListing, "/listings/remove")
    api.add_resource(EditListing, "/listings/edit")

    api.add_resource(Analytics, "/analytics")

    api.add_resource(Reviews, "/reviews")
    api.add_resource(AddReview, "/reviews/add")
    api.add_resource(RemoveReview, "/reviews/remove")
    api.add_resource(EditReview, "/reviews/edit")
    

    api.add_resource(Neighborhoods, "/neighborhoods")





