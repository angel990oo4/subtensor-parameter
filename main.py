import bittensor
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)
sub = bittensor.subtensor()
@app.route('/')
def hello_world():
    return 'Bittensor Cli Bot'
@app.route('/bot')
def bit_bot():
    return jsonify({"block": f"{str(sub.block)}", "difficulty": f"{str(sub.difficulty)}", "totalIssuance": f"{str(sub.total_issuance)}" })
