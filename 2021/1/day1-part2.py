#!/bin/env python3

'''
Pull information from a file, read in line by line, compare to previous.
'''

'''url="https://adventofcode.com/2021/day/1/input" '''
previousa=0
previousb=0
previousc=0
total=0

''' r = requests.get(url, stream=True) '''
r = open("day1-input.txt","r")

for line in r.readlines():
    if line: print(f'Line: {line}')
    current=line.strip()

    prevtotal=int(previousa)+int(previousb)+int(previousc)
    currtotal=int(previousb)+int(previousc)+int(current)

    print(f'{prevtotal} < {currtotal}')
    if previousa == 0 or previousb == 0 or previousc==0:
        print("skip")
    elif (int(prevtotal) < int(currtotal) ):
        print("Increase")
        total=total+1
    previousa=previousb
    previousb=previousc
    previousc=current

print(f'Total: {total}') 
