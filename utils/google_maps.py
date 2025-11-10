import requests
from urllib.parse import urlparse, parse_qs
#from utils.google_maps_utils import GoogleMapsUtils  # Asegúrate de tener este módulo con extract_places_coordinates()

def get_lat_long_from_maps_url(maps_url_str):
    maps_url = urlparse(maps_url_str)

    # Resolver redirecciones si es un acortador
    if maps_url.netloc in ["goo.gl", "maps.app.goo.gl"]:
        maps_url = urlparse(requests.get(maps_url_str).url)

    # Manejar redirección intermedia de Google
    if maps_url.path == "/sorry/index":
        query = parse_qs(maps_url.query)
        continue_param = query.get("continue", None)
        if continue_param:
            maps_url = urlparse(continue_param[0])

    # Caso: https://maps.google.com/?q=<lat>,<lon>
    if maps_url.netloc == "maps.google.com" and maps_url.path == "/":
        params = parse_qs(maps_url.query)
        if "q" in params:
            lat_long = params["q"][0].split(",")
            if len(lat_long) == 2:
                return float(lat_long[0]), float(lat_long[1])

    # Caso: www.google.co*/maps/*
    if maps_url.netloc.startswith("www.google.co") and maps_url.path.startswith("/maps"):
        params = parse_qs(maps_url.query)
        path = maps_url.path

        # /maps/place/<lat>,<lng>
        if maps_url.path.startswith("/maps/place"):
        # Extraer coordenadas directamente del path
            path = maps_url.path[12:].replace("+-", "-").replace("++", "+")
            lat_long = path.split(",")
            if len(lat_long) == 2:
                try:
                    return float(lat_long[0]), float(lat_long[1])
                except ValueError:
                    print("Coordenadas no numéricas en /maps/place/")


        # /maps/search/@<lat>,<lng>
        elif path.startswith("/maps/search"):
            if "@" in path:
                lat_long = path.split("@")[1].split(",")
                if len(lat_long) >= 2:
                    return float(lat_long[0]), float(lat_long[1])
            elif "query" in params:
                lat_long = params["query"][0].split(",")
                if len(lat_long) == 2:
                    return float(lat_long[0]), float(lat_long[1])
            else:
                path = path[13:].replace("+-", "-").replace("++", "+")
                lat_long = path.split(",")
                if len(lat_long) == 2:
                    return float(lat_long[0]), float(lat_long[1])

        # /maps/@<lat>,<lng>
        else:
            at_position = path.find("@")
            if at_position != -1:
                lat_long = path[at_position + 1:].split(",")
                if len(lat_long) >= 2:
                    return float(lat_long[0]), float(lat_long[1])

        # Parámetro q con coordenadas
        if "q" in params:
            q = params["q"][0]
            if q.startswith("@"):
                lat_long = q[1:].split(",")
            else:
                lat_long = q.split(",")
            if len(lat_long) == 2:
                return float(lat_long[0]), float(lat_long[1])

        # Dirección destino (daddr)
        elif "daddr" in params:
            destination = params["daddr"][0]
            if destination.startswith("@"):
                lat_long = destination[1:].split(",")
                if len(lat_long) == 2:
                    return float(lat_long[0]), float(lat_long[1])

    # maps.google.com/maps?q=<lat>,<lng>
    elif maps_url.netloc == "maps.google.com" and maps_url.path.startswith("/maps"):
        params = parse_qs(maps_url.query)
        if "q" in params:
            q = params["q"][0]
            if q.startswith("@"):
                lat_long = q[1:].split(",")
            else:
                lat_long = q.split(",")
            if len(lat_long) == 2:
                return float(lat_long[0]), float(lat_long[1])

    # Si no se pudo extraer
    print("No latitude and longitude found for URL:", maps_url_str)
    return None, None
