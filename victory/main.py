#!/usr/bin/env python3
"""
Herr Viktor thought that he is now free, but he was wrong... 
When he walked over the forest again and again to find some hint, he saw a few boards. Now, he have to solve all the tasks to find a keys, and open locks for opening mystery door to the road full of cars and buses
There were next tasks
 1. Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included). 
 2. Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].
 3. Write a program that accepts a sentence and calculate the number of letters and digits.Suppose the following input is supplied to the program: hello world! 123. Then, the output should be:LETTERS 10, DIGITS 3
 4. Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.Suppose the following input is supplied to the program: 'Hello world!'.Then, the output should be:UPPER CASE 1,LOWER CASE 9
 5. Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
"""
import helpers
from sys import argv
if __name__=='__main__':

    # Checking...

    if len(argv)==2 and argv[1]=='--help':

        print(__doc__)
    print('=======================================================================')
    print('Here are the answers...')
    print('=======================================================================')
    print('The answer of 1st task is', helpers.sqtuple())

    print('The answer of 2nd task is',list(filter(helpers.even,range(1,11))))

    print('The answer of 3rd task is'),helpers.diglet('Hello World! 123')

    print('The answer of 4th task is: The uppercase characters:',helpers.up('Hello world'), ',and the lowercase characters:',helpers.low('Hello world'))

    print('The answer of 5th task is',list(helpers.gen(114)))

