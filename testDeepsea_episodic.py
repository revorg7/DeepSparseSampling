from numpy import random
import sys
import bsuite
from bsuite.logging.csv_logging import wrap_environment
from bsuite.experiments.deep_sea import deep_sea
from wrap2 import derived
from DeepseaEncoder import DeepSea_encoder

#Initializing params
total_steps = 1e5 / 2
n_size = 20
LAST = 2
SAVE_PATH_RAND = 'results/deepsea/TS20-LONG'
env = deep_sea.DeepSea(n_size,seed=int(sys.argv[1]))
logname = 'deep_sea/'+sys.argv[1]
env = wrap_environment(env,logname,SAVE_PATH_RAND,overwrite=True)

discount = 0.95
n_actions = 2
ql = derived(n_size*n_size,n_actions,discount,2,5,40) #cross-validated params: L20:(2,5,40) ; L10:(4,10,20)
encoder = DeepSea_encoder(n_size)


#Interacting with environment
num_trials = 1
counter = 0
episodic_reward = []
n_episodes = 0
for i in range(num_trials):
	total_reward = 0
	prev_act = 0
	prev_state = -1

	act = random.randint(n_actions)
	cond = True
	env.reset()
	ql.Reset(-1)
	ql.Act(0,0)
	while cond:

		#Acting
		vals = env.step(act)
		episodic_reward.append(vals.reward)
		counter+=1

		#Episode Chk
		if vals.step_type.value == LAST:
			observation = env.reset().observation
			print('episode no.',n_episodes,' episodic-reward',sum(episodic_reward))
			episodic_reward.clear()
			ql.Reset(-1)
			act = ql.Act(vals.reward,encoder.encode(observation))
			n_episodes+=1
		else:
			observation = vals.observation

		##Encoding state, registering belief and calling Act for next step
		curr_state = encoder.encode(observation)


		ql.Observe(prev_state,prev_act,vals.reward,curr_state,act)
		act = ql.getAction(curr_state)

		prev_state = curr_state
		prev_act = act
		#print("counter is ",counter)

		if counter>=total_steps: ##200 episodes = 2000 steps in L=10, 6000 steps in L=30
			cond = False


env.close()
