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
annealings_max = 50
annealings_step = 5
iterations_max = 50
iterations_step = 5

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


def series_from_1_by_5(max_value):
    yield 1
    i = 5
    while i <= max_value:
        yield i
        i += 5

for alg,size,qasm, circuit_name in data:
    for scenario in scenarios:
        scenario_name = scenario[:-5]  # Remove .json extension
        for nonlinear_annealings in series_from_1_by_5(annealings_max):
            for nonlinear_iterations in series_from_1_by_5(iterations_max):
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

                filename = f"{results_folder}/{scenario_name}_{circuit_name}_{optimizer}_{nonlinear_annealings}_{nonlinear_iterations}.json"
                
                if os.path.exists(filename):
                    print(f"******Skipping {filename} as it already exists ******")
                    continue
                print(f"Running {filename}")
                run_qb(settings, scenario)