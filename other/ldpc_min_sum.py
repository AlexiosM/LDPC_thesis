import numpy as np

# y = [y1,y2,....,yN)]
def initializePriorProb_BN(y):
	LQnm0 = 2*y/variance # LQnm^0 = LPn^0 to apotelesma einai ena dianusma 1xN pou tha exei to 1o iteration
	LQ = np.repeat(LQnm0,m).reshape(n,m).T

def initializeMsg_CN_BN(m,n):

def updateMsg_CN_BN(m,n):  # 
	H_row = H[m,:]
	H_row[m,n] = 0
	LRmn = np.prod(np.sign(tmp[np.multiply(H_row,LQnm) != 0])) * np.amin(np.abs(tmp[np.multiply(H_row,LQnm) != 0]))

def updatePosteriorProb_BN(i,n):
	LPn = LQnm0 + 

def updateMsg_BN_CN(n,m,iteration,y):
		return LQnm = LQnm0 - LRmn

def hardDecoding():
	return c


def main():

	initializiePriorProb_BN()
	initializeMsg_CN_BN()

        for i in range(MAX_ITERATIONS):
		for i in range(M):
			updateMsg_CN_BN()
		updatePosteriorProb_BN()
		updateMsg_BN_CN()
		if hardDecoding() == 0:
			return c
		else continue

	print('Over Max iterations')
	return c


MAX_ITERATIONS = 100
variance = 5

#Parity-check matrix (non-systematic form)
H = np.array([[1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0], [1, 0, 0, 0, 1, 1], [0, 0, 1, 1, 0, 1]]) # non-systematic case
y = np.array([1.0, 3.0, 2.0])

# Received LLRs (the 1st bit is wrong - LDPC code should correct it):
r = np.array([-1.3863, 1.3863, -1.3863, 1.3863, -1.3863, -1.3863])
#r = np.array([-1.3863, 1.3863, -1.3863, -1.3863, 1.3863, -1.3863])
#r = np.array([-1.3863, 1.3863, -1.3863, 1.3863, 1.3863, 1.3863])


