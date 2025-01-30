from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def get_info():
    data = {
        "email": "sanzamcmillian@gmail.com",
        "current_datetime": datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
        "github_url": "https://github.com/sanzamcmillian/HNG12_Internship/tree/main/stage_0"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)