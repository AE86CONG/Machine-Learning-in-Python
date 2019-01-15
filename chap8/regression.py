#########learning---coca-----python


from numpy import *

import matplotlib.pyplot as plt

def loadDataSet(fileName):
	fr = open(fileName)

	numFeat = len(fr.readline().strip().split('\t')) -1
	dataMat = []; labelMat = []

	for line in fr.readlines():
		dataline = []
		curline = line.strip().split('\t')
		for i in range(numFeat):
			dataline.append(float(curline[i]))
		dataMat.append(dataline)
		labelMat.append(float(curline[-1]))
	return dataMat, labelMat

def plotdData():

	xArr, yArr = loadDataSet('ex0.txt')

	n = len(yArr)
	xcord = []; ycord = []

	for i in range(n):
		xcord.append(xArr[i][1])
		ycord.append(yArr[i])

	#fig = plt.figure()
	#ax = fig.add_subplot(111)
	plt.scatter(xcord, ycord, s =20, c = 'blue', alpha = .5)
	plt.title('data')
	plt.xlabel('x')
	plt.show()

def standRegres(xArr, yArr):
	xMat = mat(xArr); yMat = mat(yArr).T

	xTx = xMat.T*xMat
	if linalg.det(xTx) ==0:
		return

	ws = xTx.I *(xMat.T*yMat)

	return ws

def plotRegression():
	xArr, yArr = loadDataSet('ex0.txt')
	ws = standRegres(xArr,yArr)
	xMat = mat(xArr); yMat = mat(yArr)

	xCopy = xMat.copy()
	xCopy.sort(0)
	yHat = xCopy*ws

	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.plot(xCopy[:,1].flatten().A[0], yHat.flatten().A[0], c= 'red')
	ax.scatter(xMat[:,1].flatten().A[0],yMat.flatten().A[0], s = 20,c = 'blue', alpha =0.5)
	plt.title('regression')
	plt.xlabel('x')
	plt.show()



