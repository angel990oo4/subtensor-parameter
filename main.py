# import bittensor
from flask import Flask, jsonify
from flask_cors import CORS
# from tqdm import tqdm
# from concurrent.futures import ThreadPoolExecutor, as_completed
import rich, subtensorapi

app = Flask(__name__)
CORS(app, supports_credentials=True)
# sub = bittensor.subtensor()

# @app.route('/')
# def hello_world():
#     return 'Bittensor Cli Bot'
# @app.route('/bot')
# def bit_bot():
#     return jsonify({"block": f"{str(sub.block)}", "difficulty": f"{str(sub.difficulty)}", "totalIssuance": f"{str(sub.total_issuance)}" })

# @app.route("/stake")
# def bit_stake():
#     print("Calling Stake ...")
#     subHistory = bittensor.subtensor( chain_endpoint = "ws://134.122.126.212:9944" )
#     stakeHisotry =[subHistory.neuron_for_uid( uid = 50, block = subHistory.block - (7200 * i) ).stake for i in tqdm(range(5))]
#     return jsonify({"stakes":stakeHisotry})
    
# @app.route("/neuronHistory")
# def bit_neuron_history():
#     print("Calling Stake ...")
#     subHistory = bittensor.subtensor( chain_endpoint = "ws://134.122.126.212:9944" )
#     stakeHisotry =[subHistory.neuron_for_uid( uid = 50, block = subHistory.block - (7200 * i) ).stake for i in tqdm(range(30))]
#     return jsonify({"stakes":stakeHisotry})

# @app.route("/stakerange")
# def bit_stake_range():
#     uid = 50
#     days = 30
#     print('days', days)
#     sub = bittensor.subtensor( chain_endpoint = "ws://134.122.126.212:9944" )
#     blocks = list(range(sub.block - (7200 * days), sub.block, 7200))

#     def stake_for_block(block):
#         sub = bittensor.subtensor( chain_endpoint = "ws://134.122.126.212:9944" )
#         return (block, sub.neuron_for_uid( uid = uid, block = block ).stake)

#     stake_range = []
#     with tqdm(total=len(blocks)) as pbar:
#         with ThreadPoolExecutor(max_workers=10) as ex:
#                 futures = [ex.submit(stake_for_block, block) for block in blocks]
#                 for future in as_completed(futures):
#                     stake_range.append(future.result())
#                     pbar.update(1)
#     return jsonify({"stake_range":stake_range})

@app.route("/subtensorapi")
def bit_subtensorapi():
    fastsync = subtensorapi.FastSync("wss://archivelb.nakamoto.opentensor.ai:9943")
    fastsync.sync_and_save_historical(rich.console.Console(), ["2663133", "2663132", "2663131"], [1, 2], "FILENAMETHATYOUCANACCESS")
    historical_data = fastsync.load_historical_neurons("FILENAMETHATYOUCANACCESS")
    print('historical_data',historical_data)
if __name__ == '__main__':
   app.run(debug=True)