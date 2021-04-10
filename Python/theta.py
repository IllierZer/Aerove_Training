import numpy as np 
x=np.random.normal(0,1,size=(20,20)) #a matrix having entries which lie along a gaussian distribution with center at 0 and standard deviation of 1
y=np.zeros([20],dtype='int32')
for i in range(20):
    y[i]=float(input("Element: "))

trans=np.transpose(x)
mul1=np.matmul(trans,x)
mul2=np.linalg.inv(mul1)
theta1=np.matmul(mul2,trans)
theta=np.matmul(theta1,y)
print(theta)




