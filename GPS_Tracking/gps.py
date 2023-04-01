from flask import Flask, jsonify, request
from geopy.distance import geodesic

app = Flask(__name__)

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

@app.route('/bins')
def get_bins():
    user_lat = float(request.args.get('lat'))
    user_lon = float(request.args.get('lon'))
    bins_with_distance = [
        {
            'id': bin['id'],
            'name': bin['name'],
            'address': bin['address'],
            'distance': geodesic((user_lat, user_lon), (bin['lat'], bin['lon'])).km
        }
        for bin in bins
    ]
    bins_sorted_by_distance = sorted(bins_with_distance, key=lambda bin: bin['distance'])
    return jsonify({'bins': bins_sorted_by_distance})
