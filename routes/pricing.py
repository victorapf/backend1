from flask import Blueprint, request, jsonify
from services.ors_service import get_distance
from utils.tab import get_km

pricing_bp = Blueprint('cotizacion', __name__)

@pricing_bp.route('/cotizar', methods=['POST'])
def cotizar():
    data = request.get_json()
    punto_a = data.get('puntoA')
    punto_b = data.get('puntoB')

    if not punto_a or not punto_b:
        return jsonify({'error': 'Faltan coordenadas'}), 400

    try:
        distancia_km = get_distance(punto_a, punto_b)
        monto = get_km(distancia_km)

        return jsonify({
            'distancia_km': f'{round(distancia_km, 2)}km',
            'monto': f'${monto}'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

