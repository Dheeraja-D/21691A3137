from flask import Blueprint, jsonify, request
import requests
from .config import Config
from .utils import fetch_numbers, calculate_average

bp = Blueprint('routes', __name__)

# Dictionary to maintain the state of numbers
window_numbers = []

@bp.route('/numbers/<string:number_id>', methods=['POST'])
def get_numbers(number_id):
    if number_id not in Config.API_URLS:
        return jsonify({"error": "Invalid number ID"}), 400

    url = Config.API_URLS[number_id]
    
    try:
        numbers = fetch_numbers(url)
    except (requests.RequestException, ValueError) as e:
        return jsonify({"error": str(e)}), 500

    # Maintain unique numbers and handle window size
    global window_numbers
    current_window = list(set(window_numbers + numbers))[-Config.WINDOW_SIZE:]
    
    response = {
        "numbers": numbers,
        "windowPrevState": window_numbers,
        "windowCurrState": current_window,
        "avg": calculate_average(current_window)
    }

    window_numbers = current_window

    return jsonify(response)
