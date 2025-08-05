import os
import json
from qb import run_qb

shots = 4096
circuits_dir = './circuits'
results_folder = './results'
scenarios = ["scenario1.json", "scenario2.json", "scenario3.json"]
providers = [["local_aer", []]]
backends = [["local_aer", "fake_torino"], ["local_aer", "fake_kyiv"], ["local_aer", "fake_sherbrooke"], ["local_aer", "fake_fez"], ["local_aer", "fake_marrakesh"]]
execute_flag = False
nonlinear_iterations = 40
nonlinear_annealings = 10

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


for alg,size,qasm, circuit_name in data:
    for scenario in scenarios:
        scenario_name = scenario[:-5]  # Remove .json extension
        for optimizer in ["linear", "nonlinear"]:

            settings = {
                "providers": providers,
                "backends": backends,
                "execute_flag": execute_flag,
                "qasm": qasm,
                "results_folder": results_folder,
                "optimizer": optimizer,
                "algorithm": alg,
                "size": size,
                "circuit_name": circuit_name,
                "shots": shots
            }

            if optimizer == "linear":
               filename = f"{results_folder}/{scenario_name}{circuit_name}_{optimizer}.json"
            elif optimizer == "nonlinear":
                filename = f"{results_folder}/{scenario_name}{circuit_name}_{optimizer}_{nonlinear_annealings}_{nonlinear_iterations}.json"
                settings["nonlinear_iterations"] = nonlinear_iterations
                settings["nonlinear_annealings"] = nonlinear_annealings
            
            if os.path.exists(filename):
                print(f"******Skipping {filename} as it already exists ******")
                continue

            run_qb(settings, scenario)
