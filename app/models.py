# app/models.py

from flask import abort


class Rides(object):
    """This class represents the rides db."""
    def __init__(self,  start_address, destination):
        """intiate class db variables"""
        self.id = 0
        self.start_address = start_address
        self.destination = destination
        self.rides = []    
        