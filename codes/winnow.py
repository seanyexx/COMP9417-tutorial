import numpy as np
np.set_printoptions(precision=2)
x1_l=list("0101011011")
x2_l=list("1010101110")
x3_l=list("0001000010")
x4_l=list("1000111110")
x5_l=list("1010111101")
y1=1
y2=0
y3=1
y4=0
y5=0
x1=np.array([float(i) for i in x1_l])
x2=np.array([float(i) for i in x2_l])
x3=np.array([float(i) for i in x3_l])
x4=np.array([float(i) for i in x4_l])
x5=np.array([float(i) for i in x4_l])
w=np.array([float(i) for i in w])
def judge(x,w,th):
	if np.dot(x,w)-th>0:
		return np.dot(x,w)-th,1
	return np.dot(x,w)-th,0

def run_wim(data,y,th,a):
	w=np.ones((data.shape[1]))
	predicts=np.array([ judge(x,w,th)[1] for x in data])
	print("predict: ",predicts)
	print("Real: ",y)
	print("diffs: ",predicts-y)
	for k,x in enumerate(data):
		value,pred=judge(x,w,th)
		acu=y[k]
		print("w*x -th= ",value,"predict: ",pred,"Real: ",acu)
		if pred!=acu:
			for k1,v in enumerate(x):
				if v!=0:
					if y[k]==1:
						w[k1]=a*w[k1]
					else:
						w[k1]=w[k1]/a
		print("data: ",x)
		print("w: ",w)
	return w
x=np.array([x1,x2,x3,x4,x5])
y=np.array([y1,y2,y3,y4,y5])
w=run_wim(x,y,2,2)
for i in x:
	print(judge(i,w,2))