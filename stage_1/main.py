from http.client import responses

from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from functools import lru_cache

app = Flask(__name__)
CORS(app)

@lru_cache(maxsize=1024)
def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(abs(n) ** 0.5) + 1, 2):
        if abs(n) % i == 0:
            return False
    return True

@lru_cache(maxsize=1024)
def is_perfect(n):
    if n < 0:
        return False
    total  = sum(i for i in range(1, int(n / 2) + 1) if n % i == 0)
    return total == n

@lru_cache(maxsize=1024)
def is_armstrong(n):
    if n < 0:
        return False
    digits = list(map(int, str(abs(n))))
    power = len(digits)
    return sum(d ** power for d in digits) == abs(n)


def get_fun_fact(n):
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math", timeout=3)
        if response.status_code == 200:
            return response.text
    except requests.exceptions.RequestException:
        pass
    return f"{n} is an interesting number!"

@app.route('/classify-number', methods=['GET'])
def classify_number():
    num_str = request.args.get("number")

    try:
        num = int(num_str)
    except (TypeError, ValueError):
        return jsonify({"number": num_str, "error": True}), 400

    properties = []
    if is_armstrong(num):
        properties.append("armstrong")

    if num % 2 == 1:
        properties.append("odd")
    else:
        properties.append("even")

    digit_sum = sum(int(d) for d in str(abs(num)))

    response = {
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": is_perfect(num),
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": get_fun_fact(num)
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)