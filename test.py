"""
Unit tests for the Concert Itinerary Builder.

This file contains unit tests for the ItineraryBuilder class in main.py.
Participants will implement tests based on the system specifications.
"""

import unittest
from main import Concert, ItineraryBuilder
from concerts_data import get_all_concerts

class ItineraryBuilderTest(unittest.TestCase):
    """Test cases for the ItineraryBuilder class."""
    
    def setUp(self):
        """Set up for the tests."""
        self.builder = ItineraryBuilder()

        self.all_concerts = get_all_concerts()
    
    # ----- Manual Test Cases -----
    # Participants will implement their manual test cases here. 
    
    def test_manual_1(self):
        """First manually written test case."""
        
        try:
            # Get all available artists clone.

            all_artists = [
                "Ed Sheeran",
                "Coldplay",
                "Billie Eilish",
                "Skibidi toilet",
                "Metallica",
                "Skrillex"
            ]

            # Build itinerary with new instance

            itineraryBuilder = ItineraryBuilder()
            json_data = itineraryBuilder.build_itinerary(
                concerts=self.all_concerts,
                artists=all_artists
            )

            # The same artists without a concert will be indicated by the itirnary.

            artist_without_concert = json_data["artists_without_concert"]

            self.assertEqual(
                    [
                    "Skibidi toilet",
                    "Skrillex"
                    ]
                , 
                artist_without_concert, 
                "Artists without concert not indicated correctly"
            )
        except Exception as e:
            print("could not run test 1:", e)
    
    def test_manual_2(self):
        try:
            concerts = [
                Concert("Taylor Swift", "2025-06-10", "Stockholm", 59.3293, 18.0686),
                Concert("Anton Johansson", "2025-07-15", "Copenhagen", 55.6761, 12.5683),
                Concert("Niklas Gustafsson", "2025-05-20", "Oslo", 59.9139, 10.7522),
                Concert("Ed Sheeran", "2025-06-05", "Gothenburg", 57.7089, 11.9746),
            ]
            itineraryBuilder = ItineraryBuilder()
            json_data = itineraryBuilder.build_itinerary(
                concerts=concerts
            )

            sorted_concert_list = json_data["upcoming_concerts"]

            self.assertEqual(
                [
                Concert("Niklas Gustafsson", "2025-05-20", "Oslo", 59.9139, 10.7522),
                Concert("Ed Sheeran", "2025-06-05", "Gothenburg", 57.7089, 11.9746),
                Concert("Taylor Swift", "2025-06-10", "Stockholm", 59.3293, 18.0686),
                Concert("Anton Johansson", "2025-07-15", "Copenhagen", 55.6761, 12.5683),
                ],
                sorted_concert_list,
                "concerts is not sorted by date"
            )

        except Exception as e:
            print("could not run test 2:", e)
    
    def test_manual_3(self):
        try:
            concerts = [
                Concert("Taylor Swift", "2025-09-10", "Stockholm", 59.3293, 18.0686),
                Concert("Anton Johansson", "2025-07-15", "Copenhagen", 55.6761, 12.5683),
                Concert("Niklas Gustafsson", "2025-05-20", "Oslo", 59.9139, 10.7522),
                Concert("Taylor Swift", "2025-06-10", "Stockholm", 59.3293, 18.0686),
                Concert("Ed Sheeran", "2025-06-05", "Gothenburg", 57.7089, 11.9746),
                Concert("Anton Johansson", "2025-08-15", "Copenhagen", 55.6761, 12.5683),
            ]
            itineraryBuilder = ItineraryBuilder()
            json_data = itineraryBuilder.build_itinerary(
                concerts=concerts
            )

            list_of_concerts = json_data["upcoming_concerts"]

            self.assertEqual(
                [
                Concert("Ed Sheeran", "2025-06-05", "Gothenburg", 57.7089, 11.9746),
                Concert("Taylor Swift", "2025-06-10", "Stockholm", 59.3293, 18.0686),
                Concert("Niklas Gustafsson", "2025-05-20", "Oslo", 59.9139, 10.7522),
                Concert("Anton Johansson", "2025-07-15", "Copenhagen", 55.6761, 12.5683),
                ],
                list_of_concerts,
            )

        except Exception as e:
            print("could not run test 3:", e)
    
    # ----- AI-Assisted Test Cases -----
    # Participants will implement their AI-assisted test cases here.
    # Please name your test in a way which indicates that these are AI-assisted test cases.


if __name__ == "__main__":
    unittest.main()