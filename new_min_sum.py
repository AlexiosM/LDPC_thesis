import numpy as np


MAX_ITERATIONS = 100

# construction of the incoming signal vector
M = np.shape(H)[0]
N = np.shape(H)[1]
awgn = np.random.normal(0,variance,N)
signal = np.random.choice([-1,1],N) # random vector of +1 -1

y = signal + awgn
print y

variance = 1

LPn0 = 2*y/variance # vector 1xN

while (iteration < MAX_ITERATIONS):
	# update message to be send from each CN to each BN
	for n in range(N):
		for m in range(M):
			H_row = H[m,:] # take all BNs connected to the specific CN
			H_row[m,n] = 0 # except the specific BN for which the message is to be sent
			LRmn[m,n] = np.prod(np.sign(tmp[np.multiply(H_row,LQnm) != 0])) * np.amin(np.abs(tmp[np.multiply(H_row,LQnm) != 0]))

	for n in range(N): # adding vectors, element by element, aims to update the state of each BN
		H_col = H[:,n] # LP, which is the new state of a specific BN is the initial (prior probability of that BN) and the messages received from all the attached CNs to it
		LP[n] = LPn0[n] +  np.sum(np.multiply(LRnm[:,n],H_col)) 

	# update messages from each BN to each CN attached to it
	if iteration = 0:
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
		return
	else:
		iteration += 1
		continue
print "Decoding failed" 
