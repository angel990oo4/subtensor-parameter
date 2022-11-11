import bittensor
from flask import Flask, jsonify
from flask_cors import CORS
from tqdm import tqdm

app = Flask(__name__)
CORS(app, supports_credentials=True)
sub = bittensor.subtensor()

@app.route('/')
def hello_world():
    return 'Bittensor Cli Bot'
@app.route('/bot')
def bit_bot():
    return jsonify({"block": f"{str(sub.block)}", "difficulty": f"{str(sub.difficulty)}", "totalIssuance": f"{str(sub.total_issuance)}" })

@app.route("/stake")
def bit_stake():
    print("Calling Stake ...")
    subHistory = bittensor.subtensor( chain_endpoint = "ws://134.122.126.212:9944" )
    stakeHisotry =[subHistory.neuron_for_uid( uid = 50, block = subHistory.block - (7200 * i) ).stake for i in tqdm(range(5))]
    return jsonify({"stakes":stakeHisotry})
