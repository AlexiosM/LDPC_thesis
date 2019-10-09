import numpy as np

def sum_prod(r, H):
    stop = False
    Imax = 1000
    I = 0
    H_mirr = (H + np.ones(np.shape(H))) %2
    M = np.zeros(np.shape(H))
    E = np.zeros(np.shape(H))
    l = np.zeros(np.shape(r))
    while stop == False and I != Imax:
        if I == 0:
            for j in range(np.shape(H)[0]):
                M[j, :] = r*H[j, :]
        print('M:\n'+str(M))
        M = np.tanh(M / 2) + H_mirr
        for j in range(np.shape(H)[0]):
            for i in range(np.shape(H)[1]):
                if H[j,i] != 0:
                    E[j,i] = np.log(( 1 + np.prod(M[j,:]) \
                                     / M[j,i]) / ( 1 - np.prod(M[j,:]) / M[j,i]) )
                    
        print('E:\n'+str(E))
        l = r + np.sum(E, axis=0)
        print('l:\n'+str(l))
        for idx, l_j in enumerate(l):
            if l_j >= 0:
                l[idx] = 0
            else:
                l[idx] = 1
        s = np.dot(H, l) %2
        if np.prod(s == np.zeros(np.size(s))) == 1:
            stop = True
        else:
            I = I + 1
            for j in range(np.shape(H)[0]):
                for i in range(np.shape(H)[1]):
                    if H[j,i] != 0:
                        M[j,i] = np.sum(E[:, i]) - E[j,i] + r[j]
    return l

#Parity-check matrix (non-systematic form)
H = np.array([[1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0], [1, 0, 0, 0, 1, 1], [0, 0, 1, 1, 0, 1]]) # non-systematic case

# Received LLRs (the 1st bit is wrong - LDPC code should correct it):
r = np.array([-1.3863, 1.3863, -1.3863, 1.3863, -1.3863, -1.3863])
#r = np.array([-1.3863, 1.3863, -1.3863, -1.3863, 1.3863, -1.3863])
#r = np.array([-1.3863, 1.3863, -1.3863, 1.3863, 1.3863, 1.3863])

l = sum_prod(r, H)
print('Decoded message:\n'+str(l))
