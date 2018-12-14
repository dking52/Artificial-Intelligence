# Single Layer Neural Network
# 4 input / 3 output, random weights
# iterate 100 test sets (new random values each iteration)

from numpy import exp, array, random, dot

random.seed()
testCount = 1

#Create input/output nodes
input_Nodes = array([[0, 0, 1, 1], [1, 1, 1, 1], [1, 0, 1, 1], [0, 1, 1, 1]])
output_Nodes = array([[0, 1, 1, 0]]).T

for iteration in range(100):
#Generate random weights for nodes
    node_Weights = 2 * random.random((4, 3)) - 1

#Iterate nodes and calculate weights using dot(matrix multiplication)
for iteration in range(100):
    output = 1 / (1 + exp(-(dot(input_Nodes, node_Weights))))
    node_Weights += dot(input_Nodes.T, (output_Nodes - output) * output * (1 - output))

#Calculate Activation function and print
    
    print (("Test"), testCount, (": Output for nodes 1, 2 and 3: "), 1 / (1 + exp(-(dot(array([1, 0, 0, 1]), node_Weights)))))
    testCount += 1