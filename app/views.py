from flasgger import swag_from
from flask import Flask, jsonify, Blueprint
from flask_restful import reqparse
from app.models import Ride

app = Flask(__name__)
rides = Blueprint('rides', __name__)


@rides.route('/api/v1/rides', methods=['GET'])
def returnAll():
    rides = Ride.returnAll()
    return jsonify({"rides": rides})
@rides.route('/api/v1/rides/<int:ride_id>', methods=['GET'])
def returnOne(ride_id):
    ride = Ride.returnOne(ride_id)
    return jsonify({"ride": ride})
@rides.route('/api/v1/rides/<int:ride_id>', methods=['POST'])
def requestone(ride_id):
    ride = Ride.ride_request(ride_id)
    return jsonify({"ride": ride})
@rides.route('/api/v1/rides/create', methods=['POST'])
def addOne():
    parser = reqparse.RequestParser()
    parser.add_argument("start_address")
    parser.add_argument("destination")


    arguments = parser.parse_args()

    ride = Ride(arguments["start_address"], arguments["destination"])
    new_ride = Ride.addOne(ride)
    return jsonify({"ride": new_ride})
@rides.route('/api/v1/rides/delete/<int:ride_id>', methods=['DELETE'])
def removeOne(ride_id):
    remaining_rides = Ride.removeOne(ride_id)
    return jsonify({'remaining_rides': remaining_rides})

@rides.route('/api/v1/rides/request', methods=['POST'])
def getride():
    parser = reqparse.RequestParser()
    parser.add_argument("start_address")
    parser.add_argument("destination")

    arguments = parser.parse_args()

    ride = Ride(arguments["start_address"], arguments["destination"])
    new_ride = Ride.getride(ride)
    return jsonify({"ride": new_ride})
    
