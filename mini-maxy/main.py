#!/usr/bin/env python3
"""
Now, Mr. Viktor fell into a cave, did hurt himself.
He settled to find a way, but noticed something queer.
He had to fell down in the cave, he might fell.
There (in the cave) he saw much numbers written on the wall 
(more than 10 million random float numbers. He was excited.
==========================TASK=================================
Mr. Viktor must take only 2 numbers, minimum, and maximum
It's very hard task, please help to Herr Viktor
"""
from sys import argv
from mimax import stat
from random import random
from array import array

ar=array('d',(random() for i in range(10**7)))
result=stat(ar)

if __name__=='__main__':
    if len(argv)==2 and argv[1]=='--help':
        print(__doc__)
    print('Here is the result: \n', result)
