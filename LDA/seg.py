# !/usr/bin/python
# -*- coding:utf-8 -*-

import jieba

with open('utf8_corpus.txt','r') as f, open('seg_corpus.txt','w') as w:
    for line in f:
        lines = line.strip().split('\t')
        seg_list = jieba.cut(lines[1])
        row = ''
        for word in seg_list:
            row += word.encode('utf8') + ' '
        w.write(row.strip() + '\n')
