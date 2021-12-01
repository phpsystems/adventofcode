#!/bin/env python3

'''
Pull information from a url, read in line by line, compare to previous.
'''
import requests

'''url="https://adventofcode.com/2021/day/1/input" '''
previous=0
total=0

''' r = requests.get(url, stream=True) '''
r = open("day1-input.txt","r")

for line in r.readlines():
    if line: print(f'Line: {line}')
    current=line.strip()
    print(f'{previous} < {current}')
    if previous == 0:
        print("skip")
    elif (int(previous) < int(current) ):
        print("Increase")
        total=total+1
    previous=current

print(f'Total: {total}') 
