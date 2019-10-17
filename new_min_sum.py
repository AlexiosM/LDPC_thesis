import matplotlib.pyplot as plt
import numpy as np
import os
import time


# Read matrix H from H.txt file
H_positions = []

num_of_lines = int(os.popen('cat H.txt | wc -l').read())
print 'num_of_lines : '
print num_of_lines

# find max element number in H.txt which will be the one distance of the H
max_val = 0
for line in open('H.txt','r').readlines():
	print 'line.split(',')[:-1] : '
	print line.split(',')[:-1]
	tmp_max = max(map(int,(line.split(',')[:-1])))
	if  tmp_max > max_val :
		print str(tmp_max)+' greater than '+str(max_val)
		max_val = tmp_max
	print max_val


M = num_of_lines
N = max_val+1
print 'M :'+str(M) 
print 'N :'+str(N) 

H = np.zeros((M,N))
for line,line_num in zip(open('H.txt','r').readlines(),range(M)):
	for elem in map(int,line.split(',')[:-1]):
		H[line_num-1,elem-1] = 1

print 'Tanner graph matrix\nH : '
print H
np.shape(H)

ran = 100
print 'Each CN is connected to '+ str(np.sum(H[ran,:])) + ' BNs'
print 'Each BN is connected to '+ str(np.sum(H[:,ran])) + ' CNs'


def create_Y(variance):
	fake_encoded_y = np.ones(N)
	awgn = np.random.normal(0,variance,N)
	#signal = np.random.choice([-1,1],N) # random vector of +1 -1
	#y = signal + awgn
	y = fake_encoded_y + awgn
	print 'Incoming message y :'
	print y
	return y



# LDPC Min Sum
MAX_ITERATIONS = 100
#variance = 0.33
# construction of the incoming signal vector
#M = np.shape(H)[0]
#N = np.shape(H)[1]

def LDPC_min_max(variance):
	LR = np.zeros((M,N))
	H_row = np.zeros(N)
	LP = np.zeros(N)
	C = np.zeros(N)
	t0 = time.time()
	y = create_Y(variance)
	LPn0 = 2*y/variance # vector 1xN
	print "Initial vector of LPn0 = prior probabilities of BNs :"
	print LPn0
	iteration = 0
	# begin Iterations for the specific input
	while (iteration < MAX_ITERATIONS):
		print '\nIteration : '+str(iteration+1)
		# initialize LQ
		if iteration == 0:
			tmp_val = np.repeat(LPn0,M).reshape(N,M).T # columns fulfilled with the initial (a prior) BN probabilities
			LQ = np.multiply(tmp_val,H).T 	# Hadamard product with H, so that we get LQ with messages only in the attach CN of each BN
			print 'LQ : '
			print LQ			# LQ will have NxM dimensions
		# update message to be send from each CN to each BN
		for n in range(N):
			for m in range(M):
				H_row = H[m,:].copy() # take all BNs connected to the specific CN
				H_row[n] = 0 # except the specific BN for which the message is to be sent
				LR[m,n] = np.prod(np.where(np.multiply(H_row,LQ[:,m].T) > 0,1,-1)) * np.amin(np.abs(np.multiply(H_row,LQ[:,m].T)))
		print 'Update messages from CNs to BNs\nLR in iter: '+str(iteration+1)+':'
		print LR

		for n in range(N): # adding vectors, element by element, aims to update the state of each BN
			H_col = H[:,n].copy() # LP, which is the new state of a specific BN is the initial (prior probability of that BN) and the messages received from all the attached CNs to it
			LP[n] = LPn0[n] +  np.sum(np.multiply(LR[:,n],H_col)) 
		print 'Posterior probabilities of BNs\nLP:'
		print LP

		# update messages from each BN to each CN attached to it
		if iteration > 0:
			for m in range(M):
				LQ[:,m] = (LP - LR[m,:]).T # the subtraction can be done with calculations on N-size vectors so each LQ column is calculated directly
		print 'Update messages from BNs to CNs\nLQ in iter: '+str(iteration+1)+':'
		print LQ

		# hard decoding
		for n in range(N):
			if LP[n] < 0:
				C[n] = 1
			else:
				C[n] = 0
		print 'After Hard Decoding\nC:'
		print C
		residue = H.reshape(N,M).T.dot(C) # multiplication vector*Matrix c*H
		print 'Residue with lengh('+ str(len(residue)) +') :'
		print residue
		if not np.any(residue) : # if all residue elements are zero
			print "Final result is:"
			print C
			print time.time() - t0
			return 0
		else:
			iteration += 1
			continue
	print "Decoding failed, returning BER"
	print time.time() - t0
	print C
	BER = list(C).count(1) # the number of ones inside the result is the number of total errors that have not been corrected
	return BER




ber=[]
snr=[]
for varian in np.arange (2, 0.001, -0.12):
	ber.append(LDPC_min_max(varian))
	snr.append(10*np.log10(1/varian))



print ber
print snr
#[612, 609, 521, 436, 325, 158, 43, 0]
#[-3.010299956639812, -2.4303804868629446, -1.7609125905568126, -0.969100130080564, 0.0, 1.2493873660829993, 3.010299956639812, 6.020599913279624]

plt.plot(snr,ber,'ro')
plt.xlabel('SNR')
plt.ylabel('BER')
plt.show()


