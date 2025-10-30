import openrouteservice
from config import ORS_API_KEY

client = openrouteservice.Client(key=ORS_API_KEY)

def get_distance(punto_a, punto_b):
    coords = [[punto_a['lng'], punto_a['lat']], [punto_b['lng'], punto_b['lat']]]
    routes = client.directions(coords, profile='driving-car', format='json')
    distance_meters = routes['routes'][0]['summary']['distance']
    return distance_meters / 1000  # Convertir a km
