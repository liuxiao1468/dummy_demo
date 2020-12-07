import numpy as np
import scipy.io
import matplotlib.pyplot as plt

mat = scipy.io.loadmat('InsulinGlucoseData.mat')
# print(mat.keys())

strings = ['actBolusDelivered', 'dateMuBolus', 'dateNumber', 'numCGM']
x1 = np.flip(mat[strings[2]][0])
x2 = np.flip(mat[strings[1]][0])

gt = np.flip(mat[strings[0]][0])
input_data = np.flip(mat[strings[3]][0])
print(len(gt))
print(len(input_data))

print(input_data)
fig, axs = plt.subplots(2)
fig.suptitle('CGM - gt')
axs[0].plot(x1[:1000], input_data[:1000])
axs[1].plot(x2[:1000], gt[:1000])
plt.show()

# n = len(input_data)

# def init_input(input_data, n):
# 	x = [0,input_data[0],0,0,0.0068,0.0037,1.3,20]
# 	x = np.array(x,dtype = np.float64)

# 	y = 0

# 	u = np.random.normal(0., 1, 8)
# 	v = np.random.normal(0., 1, 8)
# 	return x, y

# def update_state(n)



