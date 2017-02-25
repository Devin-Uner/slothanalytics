import numpy as np

def sigmasoid(x, deriv=False):
	if(deriv):
		return x*(1-x)
	return 1/(1+np.exp(-x))

# input
x = np.array([[0,0,1,1]])
input_len = 4
# output
y = np.array([[ 0,0,1,1 ]])

# seed PRNG
np.random.seed(314159)


num_neurons_per_layer = [2,5,3,4]
layer_count = len(num_neurons_per_layer)

weights = [2*np.random.random((input_len,num_neurons_per_layer[0])) - 1]
for i in range(1, layer_count):
	weights += [2*np.random.random((num_neurons_per_layer[i-1],num_neurons_per_layer[i])) - 1]
	# print weights[i]


layers = [None]*(layer_count+1)
error = [None]*(layer_count)
change = [None]*(layer_count)
for i in range(1000000):

	# foreward!
	layers[0] = x
	for i in range(1, layer_count+1):
		layers[i] = sigmasoid(np.dot(layers[i-1], weights[i-1]))

	# calculate error
	error[-1] = y - layers[-1]
	change[-1] = error[-1] * sigmasoid(layers[-1], True)

	for j in range(layer_count-2, 0, -1):
		error[j] = change[j+1].dot(weights[j+1].T)
		change[j] = error[j] * sigmasoid(layers[j+1], True)

	for j in range(1, layer_count):
		# print layers[j]
		# print change[j]
		weights[j] += layers[j].T.dot(change[j])

	print layers[-1]


	







