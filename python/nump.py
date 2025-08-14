
import numpy as np
# print(np.__version__)
# a = np.array([1,2,3,4])
# print(type(a))
# b = np.array((1, 2, 3, 4))
# print("Array:", b)
# print("Type:", type(b))
# a = [1,2,3,4,5]
# print (a)
# print(type(a))
# c = np.array(4)
# print(c)
# d = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
# print(d)
# d1 = np.array([[[1,2,3],[3,4,5]],[[5,6,7],[7,8,9]]])
# print(d1)

# # 1 dimensional array --vector
# a1 = np.array([1,2,3,4])
# print(type(a1))
# print(a1)
# #2 dimensional array --matrix
# a2 = np.array([[1,2,3,4],[5,6,7,8]])
# print(type(a2))
# print(a2)
# # 3 dimentional array -- Tensor array
# a3 = np.array ([[[1,2,3],[3,4,5]],[[5,6,7],[7,8,9]]])
# print(type(a3))
# print(a3)
# 4 dimention array
#a4 = np.array([[[[1,2,3],[3,4,5]],[[5,6,7],[7,8,9]]],[[[0,1,2],[3,4,5]],[[6,7,8],[8,9,1]]]])
#print(a4.shape)

#array properties
#1 shape
# e = np.array([[10,20,30],[40,50,60]])
# print(e.shape)
# d = np.array([[[1,2,3],[3,4,5]],[[5,6,7],[7,8,9]]])
# print(d.shape)
d1 = np.array([[[1,2,3],[3,4,5]],[[5,6,7],[7,8,9]],[[9,0,1],[2,3,4]]])
# print(d1.shape)
d2 = np.array([[[[1,2,3],[3,4,5]],[[5,6,7],[7,8,9]],[[9,0,1],[2,3,4]]]])
# print(d2.shape)
d3 = np.array([[[[1,2,3],[3,4,5]],[[5,6,7],[7,8,9]]],[[[9,0,1],[2,3,4]],[[10,20,30],[40,50,60]]]])
# print(d3.shape)

#2size -no of elements
# print(d3.size)
# print(d2.size)
# print(d1.size)

#3 datatype
# print(d3.dtype)
# f = np.array([1.0,5,6.7])
# print(f.dtype)

#4 Transpose swap rows and column
#a6 = np.array([1,2,3,4])
# print(a6.T)
# print(d3.T)

#5 data memory location of the array
# print(id(a6))
# print(a6.data)

#indexing
# j = [1,2,3,4,[5,6],5,[9,10],10]
# print(j[6][1])
# j = np.array([1,2,3,4])
# print(j[3])
# print(j[-4])
# k = np.array([[1,2,3,5],[5,6,7,8]])
# print(k[1,2])
# print(k[-2,-2])
#3 dimentional indexing
# d = np.array([[[1,2,3],[3,4,5]],[[5,6,7],[7,8,9]]])
# print(d[0])
# print(d[0,1])
# print(d[0,1,2])
# print(d[-1,-2,-3])

#4 dimention sample
# d4 = np.array([[[[1,2,3],[3,4,5]],[[5,6,7],[7,8,9]],[[0,1,2],[0,1,4]]]])
# print(d4[0,1])
# print(d4[0,1,1])
# print(d4[0,1,1,2])
# print(d4[0,-3,-2,-1])

# d3 = np.array([[[[1,2,3],[3,4,5]],[[5,6,7],[7,8,9]]],[[[9,0,1],[2,3,4]],[[10,20,30],[40,50,60]]]])
# print(d3[1])
# print(d3[1,0,1,2])
# print(d3[-1,-2,-1,-2])

# m = np.array([[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,23,15],[17,19,20]],[[100,230,150],[170,190,200]]]])
# print(m[0,3,1,2])
# print(m[0,1,1])
# print(m[-1,-3,-1,-2])


#5 D
# m = np.array([[[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,23,15],[17,19,20]],[[100,230,150],[170,190,200]],[[3,4,2],[1,6,5]]]]])
# print(type(m))
# print(m[0,0,1,1,2])
#d3 = np.array([[[[[1,2,3],[3,4,5]],[[5,6,7],[7,8,9]]],[[[9,0,1],[2,3,4]],[[10,20,30],[40,50,60]]],[[[1,2,3],[3,4,5]],[[5,6,7],[7,8,9]]],[[[9,0,1],[2,3,4]],[[10,20,30],[40,50,60]]]]])
#print(m[0,3,1,2])

#slicing
# n = np.array([1,2,3,4,5,6,7])
# print(n[1:5])
# print(n[:4])
# print(n[3:])
# print(n[-4:-1])
# print(n[::2]) 
# print(n[::-1])  # Reverse the array
# 2D slicing
# O = np.array([[1,2,3,4],[5,6,7,8]])
# print(O[:2,:1])
# #3D slicing
# P = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# print(P[:1,:1,:2])



# iteration
# a=[1,2,3,4]
# for i in a:
# if i%2==0:
# print(i)

# q=np.array([1,2,3,4])
# for i in q:
# 	if i%2==0:
# 		print(i)

# r=np.array([[1,2,3,4],[5,6,7,8]])
# for i in r:
# 	for j in i:
# 		print(j)
		
# s=np.array([[[1,2,3,4],[5,6,7,8]],[[6,7,8,9],[4,5,6,7]]])
# for i in s:
# 	for j in i:
# 		for z in j:
# 			print(z)

# t=np.array([[[1,2,3,4],[5,6,7,8]],[[6,7,8,9],[4,5,6,7]]])
# for i in np.nditer(t):
#    print(i)

# for idx, i in np.ndenumerate(t):
#     print(idx,i)

# q=np.array([1,2,3,4])
# for idx, i in enumerate(q):
#    print(idx, i)

# # numpy joining
# u=np.array([1,2,3])
# v=np.array([4,5,6])
# print(np.concatenate((u,v)))

# u=np.array([[1,2,3],[2,3,4]])
# v=np.array([[4,5,6],[5,7,8]])
# print(np.concatenate((u,v)))

# u=np.array([[1,2,3],[2,3,4]])
# v=np.array([[4,5,6],[5,7,8]])
# #w=np.stack((u,v),axis=1)
# #print(w)
# print(np.stack((u,v)))

# # hstack()-- horizonal stack
# # vstack ()-- vertical stack

# a = np.array([1,2,3,4])
# b = np.array([2,4,5,6])
# c = np.hstack([a,b])
# print (c)
# d = np.vstack([a,b])
# print(d)

# split function

# x=np.array([1,2,3,4,5,6])
# y=np.array_split(x,2)
# print(y)

# z=np.array([[1,2,3],[4,5,6],[6,7,8],[9,10,11]])
# a=np.array_split(z,6)
# print(a)

# #hsplit
# b=np.hsplit(z,3)
# print(b)
# # vsplit
# c=np.vsplit(z,2)
# print(c)

# a=[3,1,2,3,4,5]
# a.sort(reverse=True)
# print(a)

# a=np.array([3,5,6,8,2,1])
# print(np.sort(a))

# a=np.array([3,5,6,8,2,1])
# b=np.argsort(a)[::-1]
# c=a[b]
# print(c)

# # filter method
# c=np.array([1,3,4,5,6])
# b=[True,False,True,True,False]
# print(c[b])

# c=np.array([1,3,4,5,6])
# d=c > 4
# print(c[d])

# array initialization method
# 1. zeros() method
# 2. ones() method
# 3. full() method
# 4. arange() method
# 5. linspace() method
# 6.eye() method

# a=np.zeros((2,3))
# print(a)

# a=np.ones((2,3))
# print(a)

# a=np.full((2,3),5)
# print(a)

# a=np.arange(1,10,2)
# print(a)

# c=np.linspace(0,20,num=15)
# print(c)

# d=np.eye(3)
# print(d)


# a=np.array([[1,2,3,4],[5,6,7,8]])
# a=np.array([[1,2,3,4],[5,6,7,8]])
# print(a+a)
# print(a+2)
# print(a*a)
# print(a.sum())
# print(a.min())
# print(a.max())


from numpy import random
x=random.rand()
print(x)
y=random.randint(100,size=(3,5))
print(y)
x=random.rand(2,5)
print(x)

z=random.choice([1,2,3,4,5,6],size=3)
print(z)

k=[1,2,3,4,5]
random.shuffle(k)
random.permutation(k)
print(k)
print(k)

# data distribution
# 1.normal distribution or guassion distribution

# loc==mean
# scale==standard deviation
# size ==size of the data

v=random.normal(loc=2,scale=4,size=(2,3))
print(v)

# binominal distribution
# n==number of trials
# p==probability of success
# size==size of the data

w=random.binomial(n=10,p=0.9,size=10)
print(w)

# multinominal distribution
# n==number of trials
# pvals==probability of success
# size==size of the data

w=random.multinomial(n=10,pvals=[1/6,1/3,1/6,1/6,1/6],size=10)
print(w)