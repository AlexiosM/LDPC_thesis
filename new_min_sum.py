import numpy as np


M = np.shape(H)[0]
N = np.shape(H)[1]


LPn0 = 2*y/variance # vector 1xN


while (iteration < MAX_ITERATIONS):
	for m in range(M):
		H_row = H[m,:]
		H_row[m,n] = 0
		LRmn[m,n] = np.prod(np.sign(tmp[np.multiply(H_row,LQnm) != 0])) * np.amin(np.abs(tmp[np.multiply(H_row,LQnm) != 0]))

	for n in range(N): # adding vectors, element by element
		H_col = H[:,n]
		LP[n] = LPn0[n] +  np.sum(np.multiply(LRnm[:,n],H_col)) 

	if iteration = 0:
		LQmn = LPn0
	else:
		LQnm = LP - LRmn  # ????


	#hard decoding
	for n in range(N):
		if LP[n] < 0:
			C[n] = 1
		else
			C[n] = 0


	# Check residue

	if residue == 0:
		print "result is:"
		print c
		return
	else:
		iteration += 1
		continue
print "Decoding failed" 
