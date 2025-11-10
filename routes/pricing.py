from flask import Blueprint, request, jsonify
from services.ors_service import get_distance
from utils.tab import get_km
from utils.google_maps import get_lat_long_from_maps_url

pricing_bp = Blueprint('cotizacion', __name__)

@pricing_bp.route('/cotizar', methods=['POST'])
def cotizar():
    data = request.get_json()
    punto_a = data.get('puntoA')
    punto_b = data.get('puntoB')

    if not punto_a or not punto_b:
        return jsonify({'error': 'Error, verificar URLs'}), 400
    
    lat_a, lng_a = get_lat_long_from_maps_url(punto_a)
    lat_b, lng_b = get_lat_long_from_maps_url(punto_b)

    if None in [lat_a, lng_a, lat_b, lng_b]:
        return jsonify({'error': 'No se pudieron extraer coordenadas válidas'}), 400

    punto_a = {'lat': lat_a, 'lng': lng_a}
    punto_b = {'lat': lat_b, 'lng': lng_b}

    try:
        distancia_km = get_distance(punto_a, punto_b)
        monto = get_km(distancia_km)

        return jsonify({
            'distancia_km': f'{round(distancia_km, 2)}km',
            'monto': f'${monto}',
            'puntoA': punto_a,
            'puntoB': punto_b
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

