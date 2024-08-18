import requests
from .config import Config

def fetch_numbers(url):
    try:
        response = requests.get(url, timeout=Config.REQUEST_TIMEOUT)
        response.raise_for_status()
        data = response.json()
        if "numbers" not in data:
            raise ValueError("Invalid response format")
        return data["numbers"]
    except (requests.RequestException, ValueError) as e:
        raise ValueError("Failed to fetch numbers") from e

def calculate_average(numbers):
    if not numbers:
        return 0
    return round(sum(numbers) / len(numbers), 2)
