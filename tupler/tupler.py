#!/usr/bin/env python3
"""
Now Herr Viktor walked over the forest, and came across a board, with the next note: 'If you solve the task, your way will be free of traps'
Mr Viktor began thinking about solving this task:
'We have a next task:
     We have a tuple
 ('a','b','c','d','e','f')
We must create a list, with these kind of tuples
 [('a','b'),('c','d'),('e','f')]
Mmm, and our code have to be simple and useful, the code must have maximum 3 or 4 lines'
Please help Herr Viktor to solve this :)
"""
import sys

# Tupling the string 'abcdef' to obtain the ('a','b','c','d','e','f') tuple
tupler=tuple('abcdef')

# Creating a array, or list, which we put the result within it
array=[(i,j) for i,j in zip(tupler[::2],tupler[1::2])]

if __name__=='__main__':

    # Just type ./tupler.py --help to see what you have to do, to help Mr. Viktor
     if len(sys.argv)==2 and sys.argv[1]=='--help':
        print(__doc__)

    # Printing the result
     print('Here is the result!!!')
     print(array)
