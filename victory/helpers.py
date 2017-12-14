#!/usr/bin/env python3
"""
These are helpers for Herr Viktor to fix problems and solve the task
Say hello to Mr. Viktor!!!
"""
import re
from sys import argv
def sqtuple():
    return [(t,int(t)**2) for t in range(1,21)]

def up(string):
    former=0
    bigger=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for strer in string:
        for i in bigger:
            if strer==i:
                former+=1
    return former

def low(string):
    former=0
    smaller=list('abcdefghijklmnopqrstuvwxyz')
    for strer in string:
        for i in smaller:
            if strer==i:
                former+=1
    return former

def even(x):
    if x%2 !=0:
        return x

def gen(n):
    yield from range(0,n,7)

def diglet(string):
	reg=re.compile('\d+')
	reger=list(reg.findall(string)); lister=list(reger)
	for nums in reger:
		print('DIGITS',len(list(nums)))

	regex=re.compile('[A-Za-z]')
	print('LETTERS',len(regex.findall(string)))


if __name__=='__main__':

    if len(argv)==2 and argv[1]=='--help':
        print(__doc__)
