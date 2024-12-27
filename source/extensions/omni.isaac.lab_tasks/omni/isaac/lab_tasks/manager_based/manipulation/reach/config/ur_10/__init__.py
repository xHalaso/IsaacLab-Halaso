# Copyright (c) 2022-2024, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

import gymnasium as gym

from . import agents

##
# Register Gym environments.
##

gym.register(
    id="Isaac-Reach-UR10-v0",
    entry_point="omni.isaac.lab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.joint_pos_env_cfg:UR10ReachEnvCfg",
        "rl_games_cfg_entry_point": f"{agents.__name__}:rl_games_ppo_cfg.yaml",
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_ppo_cfg:UR10ReachPPORunnerCfg",
        "skrl_cfg_entry_point": f"{agents.__name__}:skrl_ppo_cfg.yaml",
        "sb3-ppo_cfg_entry_point": f"{agents.__name__}:sb3_ppo_cfg.yaml",
        "sb3-td3_cfg_entry_point": f"{agents.__name__}:sb3_td3_cfg.yaml",
        "sb3-sac_cfg_entry_point": f"{agents.__name__}:sb3_sac_cfg.yaml",
    },
)

gym.register(
    id="Isaac-Reach-UR10-Play-v0",
    entry_point="omni.isaac.lab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.joint_pos_env_cfg:UR10ReachEnvCfg_PLAY",
        "rl_games_cfg_entry_point": f"{agents.__name__}:rl_games_ppo_cfg.yaml",
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_ppo_cfg:UR10ReachPPORunnerCfg",
        "skrl_cfg_entry_point": f"{agents.__name__}:skrl_ppo_cfg.yaml",
        "sb3-ppo_cfg_entry_point": f"{agents.__name__}:sb3_ppo_cfg.yaml",
        "sb3-td3_cfg_entry_point": f"{agents.__name__}:sb3_td3_cfg.yaml",
        "sb3-sac_cfg_entry_point": f"{agents.__name__}:sb3_sac_cfg.yaml",
    },
)
