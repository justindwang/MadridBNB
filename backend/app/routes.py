# from flask import Flask, render_template, redirect, url_for, flash, request, jsonify, make_response
# from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from .search import Listings, Reviews, Neighborhoods

def initialize_routes(api):
    api.add_resource(Listings, "/listings")
    api.add_resource(Reviews, "/reviews")
    api.add_resource(Neighborhoods, "/neighborhoods")





