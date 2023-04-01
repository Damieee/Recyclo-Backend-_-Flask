import requests
import geocoder
import jsonify

# Define some sample recycling bins
bins = [
    {
        'id': 1,
        'name': 'Green Bin',
        'address': '123 Main St.',
        'lat': 37.7749,
        'lon': -122.4194
    },
    {
        'id': 2,
        'name': 'Blue Bin',
        'address': '456 Elm St.',
        'lat': 37.7833,
    
        'lon': -122.4167
    },
    {
        'id': 3,
        'name': 'Yellow Bin',
        'address': '789 Oak St.',
        'lat': 37.7767,
        'lon': -122.3942
    }
]

class Gps:

    @staticmethod
    def gps_location():

        # Get the user's IP address
        ip = requests.get('https://api.ipify.org').text

        # Use the IP address to get the location information
        g = geocoder.ip(ip)

        # Get the latitude and longitude from the location information
        latitude, longitude = g.latlng

        return ({"Latitude": latitude, "Longitude": longitude})
