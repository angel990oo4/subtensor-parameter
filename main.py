import bittensor
from flask import Flask, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app, supports_credentials=True)
histories = []
sub = bittensor.subtensor()

def run_bittensor():
    print("Run started")
    current_block = 0
    while True:
        print("Histories:", histories)
        current_block = sub.get_current_block() #we need all blocks !!!
        metagraph = bittensor.metagraph( subtensor = sub )
        metagraph.sync()
        histories.append([metagraph.block.item(), metagraph])
        time.sleep( bittensor.__blocktime__ )
        if len(histories) > 2:
            break


@app.route('/')
def hello_world():
    return 'Bittensor Cli Bot'
@app.route('/bot')
def bit_bot():
    return jsonify({"block": f"{str(sub.block)}", "difficulty": f"{str(sub.difficulty)}", "totalIssuance": f"{str(sub.total_issuance)}" })
@app.route('/neurons')
def bit_neruons():
    neurons = bittensor.metagraph().retrieve_cached_neurons()
    # return jsonify({"neurons": f"{(sub.neurons())}" })
    # print('neurons', neurons)
    return jsonify({"neurons":neurons})

@app.route("/stake")
def stake_api():
    # run_bittensor()
    print("Calling Stake ...")
    stake_dict = {n.uid:n.stake for n in histories[-1][1]}
    return stake_dict
