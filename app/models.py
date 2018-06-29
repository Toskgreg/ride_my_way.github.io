# app/models.py

# variable that holds all the journeys and their details
rides = []
requestr = []


class Ride:

    def __init__(self, destination, start_address):

        # initialising class attributes
        self.ride_id = self.auto_id(rides)
        self.start_address = start_address
        self.destination = destination

    def addOne(self):

        # creating a dictionary from an object and returning it

        ride = {
            "Id": self.ride_id,
            "start_address": self.start_address,
            "destination": self.destination,

        }
        rides.append(ride)

        return ride

    @staticmethod
    def auto_id(ride_ids):
        # methods aids auto generation of ride_ids
        if ride_ids:
            return ride_ids[-1].get("Id") + 1
        return 1

    @staticmethod
    def returnAll():
        # This method retrieves or returns all rides in the dictionary

        if rides:
            return rides
        return "No existing Ride offer"

    @staticmethod
    def returnOne(ride_id):
        # method returns a single ride
        for ride in rides:
            if ride.get('Id') == ride_id:
                return ride
            continue

        return "Ride not Found"

    @staticmethod
    def ride_request(ride_id):
        # method returns a single ride
        for ride in rides:
            if ride.get('Id') == ride_id:
                return ride
            continue

        return "Ride not Found"

    @staticmethod
    def getride(ride_id):
        # method returns a single ride
        for ride in rides:
            if ride.get('Id') == ride_id:
                return ride
            continue

        return "Ride not Found"

    @staticmethod
    def removeOne(ride_id):
        # method deletes a specified ride
        for count, ride in enumerate(rides):
            if ride.get("Id") == ride_id:
                rides.pop(count)
                return rides
        return "Ride not Found"
