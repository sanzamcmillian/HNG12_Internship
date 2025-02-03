from http.client import responses

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return sum(i for i in range(1, n) if n % i == 0) == n


def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n


def get_fun_fact(n):
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math", timeout=3)
        if response.status_code == 200:
            return response.text
    except requests.exceptions.RequestException:
        pass
    return f"{n} is an interesting number!"

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    num_str = request.args.get("number")

    if not num_str or not num_str.isdigit():
        return jsonify({"number": num_str, "error": True}), 400

    num = int(num_str)

    properties = []

    if num % 2 == 1:
        properties.append("odd")
    else:
        properties.append("even")

    if is_armstrong(num):
        properties.append("armstrong")

    response = {
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": is_perfect(num),
        "properties": properties,
        "digit_sum": sum(int(d) for d in str(num)),
        "fun_fact": get_fun_fact(num)
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)