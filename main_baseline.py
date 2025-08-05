from evaluator_sim import Evaluator
import os, json


shots = 4096
circuits_dir = './circuits'
results_folder = './results'
scenarios = ["scenario1.json", "scenario2.json", "scenario3.json"]
providers = [["local_aer", []]]
backends = [["local_aer", "fake_torino"], ["local_aer", "fake_kyiv"], ["local_aer", "fake_sherbrooke"], ["local_aer", "fake_fez"], ["local_aer", "fake_marrakesh"]]


data = []
for filename in os.listdir(circuits_dir):
    if filename.endswith('.json'):
        filepath = os.path.join(circuits_dir, filename)
        with open(filepath, 'r') as f:
            try:
                content = json.load(f)
                data.append((content.get('algorithm'), content.get('size'), content.get('qasm'), filename[:-5]))
            except Exception as e:
                print(f"Error reading {filename}: {e}")