import numpy as np
from numpy import random
import sys
import bsuite
from bsuite.logging.csv_logging import wrap_environment
from bsuite.experiments.deep_sea import deep_sea
from bsuite.baselines.boot_dqn import boot_dqn


total_steps = 50000 + 10000
n_size = 20
LAST = 2
SAVE_PATH_RAND = 'results/deepsea/BDQNL20-LONG'
env = deep_sea.DeepSea(n_size,seed=int(sys.argv[1]))
agent = boot_dqn.default_agent( obs_spec=env.observation_spec(),action_spec=env.action_spec())
logname = 'deep_sea/'+sys.argv[1]
env = wrap_environment(env,logname,SAVE_PATH_RAND,overwrite=True)


cond = True
counter = 0
timestep = env.reset()

while cond:
	# Generate an action from the agent's policy.
	action = agent.policy(timestep)

	# Step the environment.
	new_timestep = env.step(action)
	counter+=1

	# Tell the agent about what just happened.
	agent.update(timestep, action, new_timestep)

	# Book-keeping.
	timestep = new_timestep
#	print("counter is ",counter)

	if counter>=total_steps: ##200 episodes = 2000 steps in L=10, 6000 steps in L=30
		cond = False
