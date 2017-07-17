#D:\Python27
#-*- coding:utf-8 -*-
import jieba


def seg_words(sentence):
    seg_list = jieba.cut(sentence)  # 默认是精确模式
    return seg_list

def seg_txt():
    dic = {}
    n = 0
    with  open('corpus.txt') as f, open('seg_corpus.txt', 'w') as w:
        for line in f:
            lines = line.split('\t')
            label = lines[0]
            if label not in dic:
                dic[label] = n
                n += 1
            txt = lines[1].decode('utf8')
            li = seg_words(txt.strip())
            w.write(str(dic[label]) + '\t')
            for word in li:
                w.write(word.encode('utf8') + ' ')
            w.write('\n')

def square(x):
    return x * x

def compute_chi():
    cat_num = {}
    term_cat_num = {}
    terms = set()
    labels = set()
    term_chi = {}
    n = 0
    with open('seg_corpus.txt','r') as f:
        for line in f:
            line = line.decode('utf8')
            n += 1
            lines = line.strip().split('\t')
            label = lines[0]
            labels.add(label)
            if label in cat_num:
                cat_num[label] += 1
            else:
                cat_num[label] = 1

            txts = lines[1].strip().split(' ')
            for term in txts:
                terms.add(term)
                if term in term_cat_num:
                    if label in term_cat_num[term]:
                        term_cat_num[term][label] += 1
                    else:
                        term_cat_num[term][label] = 1
                else:
                    term_cat_num[term] = {}
                    term_cat_num[term][label] = 1
    out = open('chi_num.txt','w')
    for word in terms:
        for label in labels:
            aplusb = sum(term_cat_num[word].values())
            cplusd = n - aplusb
            a = 0
            if label in term_cat_num[word]:
                a = term_cat_num[word][label]
            else:
                continue
            b = aplusb - a
            c = cat_num[label] - a
            d = cplusd - c
            fenzi = (square(a * d - b* c) * 1.0)
            fenmu = (aplusb * cplusd)
            chi = fenzi/fenmu
            if word in term_chi:
                    if chi > term_chi[word]:
                        term_chi[word] = chi
            else:
                term_chi[word] = chi
            if float(chi) - 2544.94335907 < 1:
                out.write(word.encode('utf8') + '\t' + str(a) +'\t' + str(b) + '\t' +str(c) +'\t' + str(d) +  '\t'+  str(chi))
                out.write('\n')

    ana = open('chi_result.txt','w')
    res = sorted(term_chi.items(), key=lambda e:e[1], reverse=True)
    for key,value in res:
        ana.write(key.encode('utf8') + '\t' + str(value) + '\n')

compute_chi()


