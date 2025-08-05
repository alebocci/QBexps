import os
import json
from qb import run_qb

shots = 4096
circuits_dir = './circuits'
results_folder = './results_nonlinear'
scenarios = ["scenario1.json", "scenario2.json", "scenario3.json"]
providers = [["local_aer", []]]
backends = [["local_aer", "fake_torino"], ["local_aer", "fake_kyiv"], ["local_aer", "fake_sherbrooke"], ["local_aer", "fake_fez"], ["local_aer", "fake_marrakesh"]]
execute_flag = False
optimizer = "nonlinear"
annealings_max = 100
iterations_max = 100

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
        for nonlinear_annealings in range(1, annealings_max + 1):
            for nonlinear_iterations in range(1, iterations_max + 1):
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
                    "shots": shots,
                    "nonlinear_iterations": nonlinear_iterations,
                    "nonlinear_annealings": nonlinear_annealings
                }

                filename = f"{results_folder}/{scenario_name}{circuit_name}_{optimizer}_{nonlinear_annealings}_{nonlinear_iterations}.json"
                
                if os.path.exists(filename):
                    print(f"******Skipping {filename} as it already exists ******")
                    continue

                run_qb(settings, scenario)
