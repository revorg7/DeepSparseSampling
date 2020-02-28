'''
Enconding (x,y) grid to a single number
'''


import numpy as np

class DeepSea_encoder:
	def __init__(self,size=10):
		self.size = size

	def encode(self,arr):
		if (np.argwhere(arr).size):
			index = np.argwhere(arr)[0]
		else:
			raise Exception("End state is passed")
		x = index[0]
		y = index[1]
		return y + x*self.size


#----------------------------------------------

