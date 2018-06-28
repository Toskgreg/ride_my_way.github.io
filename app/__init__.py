# app/__init__.py


from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy

# local import
from instance.config import app_config

# initialize sql-alchemy


# existing import remains

from app.models import Rides
from flask import request, jsonify, abort

def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    
    

    #####################
    # existing code remains #
    #####################
    @app.route('/api/v1/ride/', methods=['POST', 'GET'])
    def rides():
        if request.method == "POST":
            start_address = str(request.data.get('Start Address', ''))
            destination = str(request.data.get('Destination', ''))
            if start_address and destination:
                ride = Rides(start_address,destination,)
                
                
                response = jsonify({
                    'id': ride.id,
                    'start_address': ride.start_address,
                    'destination': ride.destination,
                    
                })
                response.status_code = 201
                return response
        else:
            # GET
            
            results = []


            for ride in ride:
                obj = {
                    'id': ride.id,
                    'start_address': ride.start_address,
                    'destination': ride.destination,
                   
                }
                results.append(obj)
            response = jsonify(results)
            response.status_code = 200
            return response

    
    @app.route('/api/v1/ride/<int:id>', methods=['GET', 'PUT', 'DELETE'])
    def ride_list_manipulation(id, **kwargs):
     # retrieve a ride using it's ID
        ride = Rides(id,destination="mutungo")
        if not ride:
            # Raise an HTTPException with a 404 not found status code
            abort(404)

        if request.method == 'DELETE':
            
            return {
            "message": "ride {} deleted successfully".format(ride.id) 
         }, 200

        elif request.method == 'PUT':
            
            start_address = str(request.data.get('Start Address', ''))
            destination = str(request.data.get('Destination', ''))
            ride.start_address = start_address
            ride.destination =destination
            
            response = jsonify({
                'id': ride.id,
                'start_address': ride.start_address,
                'destination': ride.destination,
                
            })
            response.status_code = 200
            return response
        else:
            # GET
            response = jsonify({
                'id': ride.id,
                'start_address': ride.start_address,
                'destination': ride.destination,
               
            })
            response.status_code = 200
            return response

    return app