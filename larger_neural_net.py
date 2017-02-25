import numpy as np
import random

def sigmasoid(x, deriv=False):
	if(deriv):
		return x*(1-x)
	return 1/(1+np.exp(-x))

# # input
# x = np.array([[0,0,1,1]])
# input_len = 4
# # output
# y = np.array([[ 0,0,1,1 ]])

# # seed PRNG
# np.random.seed(314159)


# num_neurons_per_layer = [4,5,2,4,4]
# layer_count = len(num_neurons_per_layer)

# weights = [2*np.random.random((input_len,num_neurons_per_layer[0])) - 1]
# for i in range(1, layer_count):
# 	weights += [2*np.random.random((num_neurons_per_layer[i-1],num_neurons_per_layer[i])) - 1]
# 	# print weights[i]


# layers = [None]*(layer_count+1)
# error = [None]*(layer_count)
# change = [None]*(layer_count)
# for i in range(0):

# 	# foreward!
# 	layers[0] = x
# 	for i in range(1, layer_count+1):
# 		layers[i] = sigmasoid(np.dot(layers[i-1], weights[i-1]))

# 	# calculate error
# 	error[-1] = y - layers[-1]
# 	change[-1] = error[-1] * sigmasoid(layers[-1], True)

# 	for j in range(layer_count-2, 0, -1):
# 		error[j] = change[j+1].dot(weights[j+1].T)
# 		change[j] = error[j] * sigmasoid(layers[j+1], True)

# 	for j in range(1, layer_count):
# 		# print layers[j]
# 		# print change[j]
# 		weights[j] += layers[j].T.dot(change[j])

# 	print layers[-1]


	


























class Neural_Network(object):
	"""docstring for Neural_Network"""
	def __init__(self, num_neurons_per_layer_, input_len_):
		super(Neural_Network, self).__init__()
		self.num_neurons_per_layer = num_neurons_per_layer_
		self.input_len = input_len_
		self.layer_count = len(self.num_neurons_per_layer)
		print self.layer_count

		# intialize weights
		self.weights = [2*np.random.random((self.input_len,self.num_neurons_per_layer[0])) - 1]
		for i in range(1, self.layer_count):
			self.weights += [2*np.random.random((self.num_neurons_per_layer[i-1],self.num_neurons_per_layer[i])) - 1]
			# print self.weights[i]


		self.layers = [None]*(self.layer_count+1)
		self.error = [None]*(self.layer_count)
		self.change = [None]*(self.layer_count)


	def train(self, x, y, num, printme=False):
		for i in range(num):
			# foreward!
			self.layers[0] = x
			for i in range(1, self.layer_count+1):
				self.layers[i] = sigmasoid(np.dot(self.layers[i-1], self.weights[i-1]))

			# calculate error
			self.error[-1] = y - self.layers[-1]
			self.change[-1] = self.error[-1] * sigmasoid(self.layers[-1], True)

			for j in range(self.layer_count-2, 0, -1):
				self.error[j] = self.change[j+1].dot(self.weights[j+1].T)
				self.change[j] = self.error[j] * sigmasoid(self.layers[j+1], True)

			for j in range(1, self.layer_count):
				# print layers[j]
				# print change[j]
				self.weights[j] += self.layers[j].T.dot(self.change[j])

			# randomly zero nodes
			# kinda like drinking a ton, fries some nerve cells but u feel better, and it helps the soul :)
			if(random.randrange(0, 1) == 2):
				zero = random.randrange(0, len(self.layers))
				self.layers[zero][random.randrange(0, len(self.layers[zero]))] = random.choice([-1,0,1])
			if(printme):
				print self.layers[-1]


def stringToArray(stra):
	#remove brackets
	result = []
	stra = stra.replace("[", "").replace("]", "")
	#go through the string
	for x in stra:
		if(x == "1"):
			result += [1]
		if(x == "0"):
			result += [0]
	return result


my_neural_net = Neural_Network([161,120,60,43], 161)

file = open("normalized data.txt", "r")
text = []
for line in file:
	text += [line]
file.close()
for i in range(0, 1000):
	for i in range(0, len(text)-1, 2):
		my_neural_net.train([stringToArray(text[i+1])],[stringToArray(text[i])], 1, True)
		print "---------"

my_neural_net.train([[ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],[stringToArray(text[i])], 1, True)


	
















