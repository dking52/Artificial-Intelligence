# Hidden Markov Model
# Calculate probable path given path weights
# Using dictionary to assign values to string states
# and tuples for obs and states to ensure not changed

import random

#Create states and observationservations
model_States = ('Dead', 'Alive')
model_Obs = ('breathing', 'cold', 'warm')
 
 #Create random starting probabilities
initial_Prob = {
    'Dead': round(random.uniform(0.0, 1.0), 3), 
    'Alive': round(random.uniform(0.0, 1.0), 3)
}
 
#Create random transition probabilities
trans_Prob = {
   'Dead' : {'Dead': round(random.uniform(0.0, 1.0), 3), 'Alive': round(random.uniform(0.0, 1.0), 3)},
   'Alive' :   {'Dead': round(random.uniform(0.0, 1.0), 3), 'Alive': round(random.uniform(0.0, 1.0), 3)},
}
 
#Create random emission probabilities
emiss_Prob = {
   'Dead' : {'breathing': round(random.uniform(0.0, 1.0), 3), 'cold': round(random.uniform(0.0, 1.0), 3), 'warm': round(random.uniform(0.0, 1.0), 3)},
   'Alive'   : {'breathing': round(random.uniform(0.0, 1.0), 3), 'cold': round(random.uniform(0.0, 1.0), 3), 'warm': round(random.uniform(0.0, 1.0), 3)},
}

#Print the generated probabilities
print ("\nRandom Emission Probabilities")
print(emiss_Prob)
print ("\nRandom Transition Probabilities")
print(trans_Prob)

#Calculate paths using viterbi algorithm
def viterbi_algor(observations, model_States, initial_Prob, trans_Prob, emiss_Prob):
	path = { i:[] for i in model_States}
	curr_pro = {}

	#Nested loop to iterate emiss_prob with observations to calculate new/highest probabilities
	for i in model_States:
		curr_pro[i] = initial_Prob[i] * emiss_Prob[i][observations[0]]
	for i in range(1, len(observations)):
		last_trans_Prob = curr_pro
		curr_pro = {}
		#Calculate probability, max is ideal
		for curr_state in model_States:
			ideal_prob, previous = max(((last_trans_Prob[last_state] * trans_Prob[last_state][curr_state] * emiss_Prob[curr_state][observations[i]], last_state) 
				                       for last_state in model_States))
			curr_pro[curr_state] = ideal_prob
			path[curr_state].append(previous)
	#Update path with each max prob
	ideal_prob = -1
	best = None
	for i in model_States:
		path[i].append(i)
		if curr_pro[i] > ideal_prob:
			best = path[i]
			ideal_prob = curr_pro[i]
        
		print (("\nPath probability: "),'%s: %s'%(curr_pro[i], path[i]))
               
	return best


if __name__ == '__main__':
	observations = ['breathing', 'cold', 'warm']
	print (("\nOptimal Path: "), (viterbi_algor(observations, model_States, initial_Prob, trans_Prob, emiss_Prob)))