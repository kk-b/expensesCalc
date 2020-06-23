from collections import defaultdict
import re

months = defaultdict(int)
keys = {}
keyValues = defaultdict(int)
expenses = open('expenses/2020 Expenses.txt')
expenses = [i.rstrip('\n') for i in expenses.readlines()]
title = expenses[0].rstrip('\n')
month = None
schoolAmount = 0 

for i in expenses[3:expenses[3:].index('')+3]:
    yes = i.split()
    keys[yes[0]] = yes[-1]


for i in expenses[1:]:
    line = i.strip().lower()
    if re.search('^[a-z]+$', line):
        month = line
    else:
        lineBreak = [i.lower() for i in line.split()]
        if len(lineBreak) > 0 and (lineBreak[0] == '*' or lineBreak[0] == '•'):
            months[month] += float(lineBreak[1][1:]) 
            keyValues[lineBreak[-1]] += float(lineBreak[1][1:])
            if 'rent' in lineBreak or 'school' in lineBreak:
                schoolAmount += float(lineBreak[1][1:])  
                
total = sum(months.values())
    

print(f'\n{title}')
print('---------------------------\n')
for k, v in months.items():
    print(f'{k.title():15}${v:.2f}')
print('\n---------------------------') 
print('Categories\n')
for k, v in keyValues.items():
    print(f'{keys[k].title():14} - ${round(v, 2)}') 
print('\n---------------------------') 
print('%-14s $%.2f' % ('School Expenses:     ', schoolAmount))
print('%-14s $%.2f' % ('Total without School:', total - schoolAmount))
print('%-14s $%.2f' % ('Total:               ', total))

