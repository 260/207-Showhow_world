#!/usr/bin/python3

# This problem is http://yukicoder.me/problems/560

first_line = input()

begin_end_numbers = list(map(int, first_line.split(' ')))

"""
for i in range(begin_end_numbers[0], begin_end_numbers[1]):
    if i % 3 == 0 or '3' in str(i):
        print(i)
"""

for i in range(begin_end_numbers[0], begin_end_numbers[1]+1):
    if i % 3 == 0:
        print(i)
    elif '3' in str(i):
        print(i)
# print(begin_end_numbers)
