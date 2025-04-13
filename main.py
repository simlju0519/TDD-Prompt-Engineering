"""
Concert Itinerary Builder

This module provides functionality to build an itinerary of upcoming concerts.
"""

import math

class Concert:
    """
    Represents a concert event.
    
    Attributes:
        artist (str): The name of the artist performing.
        date (str): The date of the concert in 'YYYY-MM-DD' format.
        location (str): The location where the concert will take place.
        latitude (float): Latitude coordinate of the concert location.
        longitude (float): Longitude coordinate of the concert location.
    """
    
    def __init__(self, artist, date, location, latitude, longitude):
        self.artist = artist
        self.date = date
        self.location = location
        self.latitude = latitude
        self.longitude = longitude

class ItineraryBuilder:
    """
    A class to build concert itineraries. 
    """

    concerts = []
    artists = []
    
    def _get_artists_without_concert(self):
        concerts = self.concerts.copy()
        aritsts = self.artists.copy()

        for concert in concerts:
            concert: Concert
            if concert.artist in aritsts:
                aritsts.remove(concert.artist)
        
        return []


    def build_itinerary(self, concerts, artists=None):
        self.concerts = concerts
        self.artists = artists


        return {
            "artists_without_concert": self._get_artists_without_concert()
        }


if __name__ == "__main__":
    from concerts_data import get_all_concerts
    
    all_concerts = get_all_concerts()