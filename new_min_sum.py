import numpy as np
import os


# Read matrix H from H.txt file
H_positions = []

num_of_lines = int(os.popen('cat H.txt | wc -l').read())
print num_of_lines

# find max element number in H.txt which will be the one distance of the H
max_val = 0
for line in open('H.txt','r').readlines():
	print line.split(',')[:-1]
	tmp_max = max(map(int,(line.split(',')[:-1])))
	if  tmp_max > max_val :
		print str(tmp_max)+' greater than '+str(max_val)
		max_val = tmp_max
	print max_val

print max_val
print num_of_lines

M = num_of_lines
N = max_val

H = np.zeros((M,N))
for line,line_num in zip(open('H.txt','r').readlines(),range(M)):
	for elem in map(int,line.split(',')[:-1]):
		H[line_num-1,elem-1] = 1

print H
H.shape

ran = 300
print 'Each CN is connected to '+ str(np.sum(H[ran,:])) + ' BNs'
print 'Each BN is connected to '+ str(np.sum(H[:,ran])) + ' CNs'



# LDPC Min Sum
MAX_ITERATIONS = 100
variance = 1
# construction of the incoming signal vector
#M = np.shape(H)[0]
#N = np.shape(H)[1]
awgn = np.random.normal(0,variance,N)
signal = np.random.choice([-1,1],N) # random vector of +1 -1

y = signal + awgn
print y

fake_encoded_y = np.zeros(N)
fake_encoded_y[1] = 1
print fake_encoded_y
y=fake_encoded_y




LPn0 = 2*y/variance # vector 1xN
iteration = 0
while (iteration < MAX_ITERATIONS):
	# update message to be send from each CN to each BN
	for n in range(N):
		for m in range(M):
			H_row = H[m,:] # take all BNs connected to the specific CN
			H_row[n] = 0 # except the specific BN for which the message is to be sent
			LRmn[m,n] = np.prod(np.sign([np.multiply(H_row,LQnm) != 0])) * np.amin(np.abs([np.multiply(H_row,LQnm) != 0]))

	for n in range(N): # adding vectors, element by element, aims to update the state of each BN
		H_col = H[:,n] # LP, which is the new state of a specific BN is the initial (prior probability of that BN) and the messages received from all the attached CNs to it
		LP[n] = LPn0[n] +  np.sum(np.multiply(LRnm[:,n],H_col)) 

	# update messages from each BN to each CN attached to it
	if iteration == 0:
		tmp_val = np.repeat(LPn0,M).reshape(N,M).T # columns fulfilled with the initial (a prior) BN probabilities  
		LQ = np.multiply(tmp_val,H) # Hadamard product with H, so that we get LQ with messages only in the attach CN of each BN 
	else:
		for m in range(M):
			LQ[:,m] = (LP - LRmn).T # the subtraction can be done with calculations on N-size vectors so each LQnm column is calculated directly

	# hard decoding
	for n in range(N):
		if LP[n] < 0:
			C[n] = 1
		else:
			C[n] = 0

	# Check residue
	if False not in  residue == 0:
		print "result is:"
		print C
	        exit(0)	
	else:
		iteration += 1
		continue
print "Decoding failed" 
