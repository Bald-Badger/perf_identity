import numpy as np

if __name__ == '__main__':
	n = 30000
	a = np.random.rand(3000,n)
	b = np.random.rand(n,3000)
	c = np.matmul(a,b)
