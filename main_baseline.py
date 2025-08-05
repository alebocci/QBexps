from evaluator_sim import Evaluator
from quantum_executor import VirtualProvider
import os, json


shots = 4096
circuits_dir = './circuits'
results_folder = './results_baseline'
scenarios = ["scenario1.json", "scenario2.json", "scenario3.json"]
providers = [["local_aer", []]]
backends = [("local_aer", "fake_torino"), ("local_aer", "fake_kyiv"), ("local_aer", "fake_sherbrooke"), ("local_aer", "fake_fez"), ("local_aer", "fake_marrakesh")]


virtual_provider = VirtualProvider({"local_aer": {}}, ["local_aer"])

if not os.path.exists(results_folder):
    os.makedirs(results_folder)

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


baselines = {"all_torino":[("fake_torino",shots)], 
            "all_kyiv":[("fake_kyiv",shots)], 
            "all_sherbrooke":[("fake_sherbrooke",shots)], 
            "all_fez":[("fake_fez",shots)], 
            "all_marrakesh":[("fake_marrakesh",shots)],
            "fair":[("fake_torino",shots//len(backends)),("fake_kyiv",shots//len(backends)),("fake_sherbrooke",shots//len(backends)),("fake_fez",shots//len(backends)),("fake_marrakesh",shots//len(backends))]}


def created_dispatch(backends, circuit, shot_vals):
    dispatch = {}
    for provider, backend in backends:
        if backend not in shot_vals or shot_vals[backend] == 0:
            continue
        if provider not in dispatch:
            dispatch[provider] = {}
        dispatch[provider][backend] = [{"circuit": circuit, "shots": int(shot_vals[backend])}]
    return dispatch


def scenario1(costs, times):
    cost_w = 0.5
    time_w = 0.5
    return cost_w * sum(costs) + time_w * max(times)

def scenario2(costs):
    return -sum(costs)

def scenario3(times):
    return max(times)

for alg, size, qasm, circuit_name in data:
    evaluator = Evaluator(qasm)
    for baseline_name, baseline in baselines.items():
        estimates = {}
        costs = []
        times = []
        fidelities = []
        shot_vals = {}
        for backend, shots in baseline:
            _backend = virtual_provider.get_backend("local_aer", backend)
            estimates[backend] = evaluator.evaluate_qpu(_backend, shots)
            cost = estimates[backend]["cost"]
            execution_time = estimates[backend]["execution_time"]
            waiting_time = estimates[backend]["waiting_time"]
            fidelity = estimates[backend]["fidelity"]

            time = execution_time + waiting_time
            costs.append(cost)
            times.append(time)
            fidelities.append(fidelity)
            shot_vals[backend] = shots
        scenario1_value = scenario1(costs, times)
        scenario2_value = scenario2(costs)
        scenario3_value = scenario3(times)
        total_cost = sum(costs)
        max_time = max(times)
        min_fidelity = min(fidelities)
        dispatch = created_dispatch(backends, qasm, shot_vals)
        to_dump = {
            "algorithm": alg,
            "size": size,
            "circuit_name": circuit_name,
            "baseline": baseline,
            "scenario1_value": scenario1_value,
            "scenario2_value": scenario2_value,
            "scenario3_value": scenario3_value,
            "total_cost": total_cost,
            "max_time": max_time,
            "min_fidelity": min_fidelity,
            "dispatch": dispatch
        }
        filename = f"{results_folder}/{circuit_name}_{baseline_name}.json"
        with open(filename, "w") as f:
            json.dump(to_dump, f, indent=4)

        
        



