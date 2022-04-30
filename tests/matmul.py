from xmlrpc.client import MAXINT
import numpy as np

if __name__ == '__main__':
	n = 30000
	a = np.random.randint(2**64-1,size=(n,n),dtype=np.uint64)
	b = np.random.randint(2**64-1,size=(n,n),dtype=np.uint64)
	c = np.matmul(a,b)
