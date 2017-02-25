import numpy as np

def sigmasoid(x, deriv=False):
	if(deriv):
		return x*(1-x)
	return 1/(1+np.exp(-x))

# input
x = np.array([[0,0,1],
			  [0,1,1],
			  [1,0,1],
			  [1,1,1]])
# output
y = np.array([[0,0,1,1]]).T

# seed PRNG
np.random.seed(314159)

#initialize weights
syn0 = 2*np.random.random((3,4)) - 1
syn1 = 2*np.random.random((4,4)) - 1
syn2 = 2*np.random.random((4,1)) - 1

for i in range(0,100000):

	# foreward!
	layer0 = x
	layer1 = sigmasoid(np.dot(layer0, syn0))
	layer2 = sigmasoid(np.dot(layer1, syn1))
	layer3 = sigmasoid(np.dot(layer2, syn2))

	############ backpropigation ############

	# calculate the error
	layer3_error = y - layer3
	layer3_change = layer3_error * sigmasoid(layer3, True)

	layer2_error = layer3_change.dot(syn2.T)
	layer2_change = layer2_error * sigmasoid(layer2, True)

	layer1_error = layer2_change.dot(syn1.T)
	layer1_change = layer1_error * sigmasoid(layer1, True)

	# add to the weights
	syn2 += layer2.T.dot(layer3_change)
	syn1 += layer1.T.dot(layer2_change)
	syn0 += layer0.T.dot(layer1_change)
	


layer0 = np.array([[0,0,0]])
layer1 = sigmasoid(np.dot(layer0, syn0))
layer2 = sigmasoid(np.dot(layer1, syn1))
layer3 = sigmasoid(np.dot(layer2, syn2))

print layer3
































