# -*- coding: utf-8 -*-
__author__ = 'Matrix'
# 2015/01/17
# Script passed in py2 & py3 with Ubuntu 14.04 env.
# Prerequirement: pip install nltk

from libs.nlpLib import nltkL

nltk =nltkL("libs/nltk_data/")  # folder "nltk_data" location, if default, just give it an empty string.

k ="""Computational Science seeks to explain the complex world we live in using technological simulations."""
stopword =["to", "the", "in", "we"]           # stopword is an option condition that you can choice.

print("Unigram------------------------")
result =nltk.string2ngram(string =k, n =1)                          # n =n_gram
print(result)                                                       # return list objects with list inside(depend on ngram).

print("Unigram Without stopword-------")
result =[i for i in result if i not in stopword]
print(result)

print("Bigram------------------------")
result =nltk.string2ngram(string =k, n =2)                          # n =n_gram
print(result)                                                       # return list objects with list inside(depend on ngram).
print()

print("Trigram------------------------")
result =nltk.string2ngram(string =k, n =3)                          # n =n_gram
print(result)                                                       # return list objects with list inside(depend on ngram).

'''

Console Print:::

Unigram------------------------
[['Computational'], ['Science'], ['seeks'], ['to'], ['explain'], ['the'], ['complex'], ['world'], ['we'], ['live'],
['in'], ['using'], ['technological']]
Bigram------------------------
[['Computational', 'Science'], ['Science', 'seeks'], ['seeks', 'to'], ['to', 'explain'], ['explain', 'the'],
['the', 'complex'], ['complex', 'world'], ['world', 'we'], ['we', 'live'], ['live', 'in'], ['in', 'using'],
['using', 'technological']]
Trigram------------------------
[['Computational', 'Science', 'seeks'], ['Science', 'seeks', 'to'], ['seeks', 'to', 'explain'],
['to', 'explain', 'the'], ['explain', 'the', 'complex'], ['the', 'complex', 'world'], ['complex', 'world', 'we'],
['world', 'we', 'live'], ['we', 'live', 'in'], ['live', 'in', 'using'], ['in', 'using', 'technological']]


'''