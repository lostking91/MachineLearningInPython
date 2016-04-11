#coding=utf-8
# ��������	��������Lost
'''
Read File on 2016.4.4
file2mat -> savemat (-> readmat)
file2mat
Input: file and a num<=1
Output: if num=1,return mat and label
if num<1,return a random [trainMat,trainLabel,testMat,testLabel]
savemat
save matrix as txt
readmat
load matrix

PengKun
'''
from numpy import *
import operator
from os import listdir
import random
import linecache
print "���سɹ�"

# savetxt��loadtxt�ʺ϶�д1ά�Ͷ�ά����
# ��������,��%g�ĸ�ʽ���棬���ڻ�û�н�����������
def savemat(filename,mat):
    "{:<10}".format(mat)
    savetxt(filename,mat,fmt="%g")

# ��ȡ����
def readmat(filename):
    return loadtxt(filename)

# ���ѡ��
# ������ĩλ��ǩ
def rand2mat(alldata,randpart):
    m,n=alldata.shape
#    n=n-1	#ȥ����ǩ
    randNumber=[i for i in range(m)]
    random.shuffle(randNumber)
    partition=int(randpart*m)
#   print alldata,randNumber,partition
    trainPart=randNumber[:partition]
    testPart=randNumber[partition:]
    testMat= zeros((len(testPart),n))
    trainMat=zeros((len(trainPart),n))
    for i,x in enumerate(trainPart):
        trainMat[i,]=alldata[x, ]
    for j,y in enumerate(testPart):
        testMat[j,:]=alldata[y, ]
    return trainMat,testMat

# ��ȡ����
def file2mat(filename,randpart):      
    fr = open(filename)
    numberOfLines = len(fr.readlines())         #get the number of lines in the file
    fr = open(filename)
    FeatureOfLines = len(fr.readline().strip().split(',')) # get the feature and label,feature=FeatureOfLines-1
    # FeatureOfLines = linecache.getlines(filename,1).count('\t') # same as FeatureOfLines
    returnMat = zeros((numberOfLines,FeatureOfLines))        #prepare matrix to return
#    print returnMat
    classLabelVector = []                       #prepare labels return
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split(',')
        for i, item in enumerate(listFromLine):
            if item=='?': item='99'
            listFromLine[i] = eval(item)
 #       print listFromLine[30]
        returnMat[index,] = listFromLine
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
#    print returnMat
    if randpart!=1:
        trainMat,testMat=rand2mat(returnMat,randpart)
        return trainMat,testMat
    else:
        return returnMat[:,:-1],classLabelVector