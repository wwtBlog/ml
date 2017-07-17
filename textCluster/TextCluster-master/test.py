# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import codecs
from sklearn.cluster import KMeans
def getFeatures():
    l = []
    n = 0
    with open('chi_result.txt') as f:
        for line in f:
            if n == 3000:
                break
            words = line.split('\t')
            l.append(words[0])
            n += 1
    return l
def getMatrix():
    l = getFeatures()
    k = 0
    with open('seg_corpus.txt') as f, open('matrix.txt', 'w') as w:
        for line in f:
            k += 1
            if k == 10000:
                break
            lines = line.split('\t')
            for word in l:
                if word in lines[1]:
                    w.write('1')
                else:
                    w.write('0')
                w.write('\t')
            w.write('\n')

def loadDataSet(fileName):      #general function to parse tab -delimited floats
    dataMat = []                #assume last column is target value
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = map(float,curLine) #map all elements to float()
        dataMat.append(fltLine)
    return dataMat

def kmeans():
    getMatrix()
    datamat =  loadDataSet('matrix.txt')
    #聚类分析
    km = KMeans(n_clusters = 5)
    km.fit(datamat)
    #中心点
    print(km.cluster_centers_)
    #每个样本所属的簇
    clusterRes = codecs.open('cluster.txt', 'w', 'utf-8')

    count = 1
    while count <= len(km.labels_):
        clusterRes.write(str(count) + '\t' + str(km.labels_[count-1]))
        clusterRes.write('\r\n')
        count = count + 1
    clusterRes.close()

def metric():
    corpus = {}
    num = 0
    with open('seg_corpus.txt','r') as f:

       for line in f:
           num += 1
           lines = line.split('\t')
           corpus[num] = lines[0]
    with open('cluster.txt') as c:
        all = 0
        tp = 0
        linenum = 0
        pre = 0
        right = 0
        for line2 in c:
            linenum += 1
            lines2 = line2.split('\t')
            label = lines2[1].strip()
            if label == '4' and corpus[linenum] == '4':
                tp+=1
            if label == '4':
                pre += 1
            if corpus[linenum] == '4':
                right += 1

        prec = float(tp)/pre
        print prec
        recall = float(tp)/right
        print recall

def cut():
    with open('seg_corpus.txt') as f, open('lda_corpus.txt','w') as w:
        num = 0
        for line in f:
            num += 1
            if num == 10000:
                break
            lines = line.split('\t')
            w.write(lines[1])

cut()