\* General_Expr_Problem *\
Minimize
OBJ: max_aux_0
Subject To
constraint_0: fake_torino_shots >= 700
constraint_1: 0.215172234978 fake_fez_shots + 0.122734701186 fake_kyiv_shots
 + 0.117461894309 fake_marrakesh_shots + 0.0615541563615 fake_sherbrooke_shots
 + 0.211431409756 fake_torino_shots <= 1700
constraint_2: fake_fez_shots + fake_kyiv_shots + fake_marrakesh_shots
 + fake_sherbrooke_shots + fake_torino_shots = 4096
constraint_3: fake_fez_used + fake_kyiv_used + fake_marrakesh_used
 + fake_sherbrooke_used + fake_torino_used >= 1
link_shots_nonnegative_fake_fez: fake_fez_shots >= 0
link_shots_nonnegative_fake_kyiv: fake_kyiv_shots >= 0
link_shots_nonnegative_fake_marrakesh: fake_marrakesh_shots >= 0
link_shots_nonnegative_fake_sherbrooke: fake_sherbrooke_shots >= 0
link_shots_nonnegative_fake_torino: fake_torino_shots >= 0
link_shots_used_upper_fake_fez: fake_fez_shots - 4096 fake_fez_used <= 0
link_shots_used_upper_fake_kyiv: fake_kyiv_shots - 4096 fake_kyiv_used <= 0
link_shots_used_upper_fake_marrakesh: fake_marrakesh_shots
 - 4096 fake_marrakesh_used <= 0
link_shots_used_upper_fake_sherbrooke: fake_sherbrooke_shots
 - 4096 fake_sherbrooke_used <= 0
link_shots_used_upper_fake_torino: fake_torino_shots - 4096 fake_torino_used
 <= 0
max_aux_0_ge_fake_fez: - 0.32 fake_fez_shots - 30 fake_fez_used + max_aux_0
 >= 0
max_aux_0_ge_fake_kyiv: - 0.21 fake_kyiv_shots - 90 fake_kyiv_used + max_aux_0
 >= 0
max_aux_0_ge_fake_marrakesh: - 0.2 fake_marrakesh_shots
 - 85 fake_marrakesh_used + max_aux_0 >= 0
max_aux_0_ge_fake_sherbrooke: - 0.27 fake_sherbrooke_shots
 - 85 fake_sherbrooke_used + max_aux_0 >= 0
max_aux_0_ge_fake_torino: - 0.2 fake_torino_shots - 75 fake_torino_used
 + max_aux_0 >= 0
total_shots: fake_fez_shots + fake_kyiv_shots + fake_marrakesh_shots
 + fake_sherbrooke_shots + fake_torino_shots = 4096
Bounds
 0 <= fake_fez_shots
 0 <= fake_kyiv_shots
 0 <= fake_marrakesh_shots
 0 <= fake_sherbrooke_shots
 0 <= fake_torino_shots
 max_aux_0 free
Generals
fake_fez_shots
fake_kyiv_shots
fake_marrakesh_shots
fake_sherbrooke_shots
fake_torino_shots
Binaries
fake_fez_used
fake_kyiv_used
fake_marrakesh_used
fake_sherbrooke_used
fake_torino_used
End
