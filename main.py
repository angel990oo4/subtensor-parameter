import bittensor
from flask import Flask, jsonify, request
import json
from flask_cors import CORS
import rich, subtensorapi

app = Flask(__name__)
CORS(app, supports_credentials=True)
sub = bittensor.subtensor()
fastsync = subtensorapi.FastSync("wss://archivelb.nakamoto.opentensor.ai:9943")

@app.route('/')
def hello_world():
    return 'Bittensor Cli Bot'

@app.route('/bot')
def bit_bot():
    return jsonify({"block": f"{str(sub.block)}", "difficulty": f"{str(sub.difficulty)}", "totalIssuance": f"{str(sub.total_issuance)}" })

@app.route("/subtensorapi")
def bit_subtensorapi():
    uid = request.get_json()['uid']
    days = int(request.get_json()['range'])
    blocks = list(range(sub.block - (7200 * days), sub.block, 7200))
    fastsync.sync_and_save_historical(blocks, [uid], "FILENAMETHATYOUCANACCESS")
    historical_data = fastsync.load_historical_neurons("FILENAMETHATYOUCANACCESS")
    return json.dumps(historical_data, default=lambda x: x.__dict__)

if __name__ == '__main__':
   app.run(debug=True)
