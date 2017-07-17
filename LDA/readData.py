# !/usr/bin/python
# -*- coding:utf-8 -*-

with open('corpus.txt') as f,open('utf8_corpus.txt','w') as w:
    for line in f:
        line = line.decode('utf8').encode('utf8')
        w.write(line)