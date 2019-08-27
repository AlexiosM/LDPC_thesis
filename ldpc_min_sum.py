import numpy as np

# y = [y1,y2,....,yN)]
def initializiePriorProb_BN(y):
	LQnm = 2*y/variance # LQnm^0 = LPn^0

def initializeMsg_CN_BN(m,n):

def updateMsg_CN_BN(m,n):
	LRmn = np.prod(np.sign(a[np.multiply(H(m,:),LQnm) != 0])) * np.amin(ns.abs(a[np.multiply(H(m,:),LQnm) != 0]))

def updatePosteriorProb_BN():

def updateMsg_BN_CN(n,m):
	LQnm = LPn - LRmn

def hardDecoding():
	return c


def main():

	initializiePriorProb_BN()
	initializeMsg_CN_BN()

        for i in range(MAX_ITERATIONS):

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


