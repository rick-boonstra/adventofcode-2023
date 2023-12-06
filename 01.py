import aoc_modules as aoc
import re

DAY = '01'
TEST_FLAG = False

if TEST_FLAG:
    file_name = DAY + '-test.txt'
else:
    file_name = DAY + '.txt'

inputs = aoc.load_file(file_name)

def get_number(string):
    numbers_only = re.sub('\D','',line)
    first_digit = numbers_only[:1]
    last_digit = numbers_only[-1:]
    return int(first_digit + last_digit)

# PART ONE
running_sum = 0
for line in inputs:
    running_sum += get_number(line)
print(f'Part one answer: {running_sum}')

# PART TWO
if TEST_FLAG:
    file_name = DAY + '-test-pt2.txt'
    inputs = aoc.load_file(file_name)

running_sum = 0
for line in inputs:
    line = line.replace('one','one1one')
    line = line.replace('two','two2two')
    line = line.replace('three','three3three')
    line = line.replace('four','four4four')
    line = line.replace('five','five5five')
    line = line.replace('six','six6six')
    line = line.replace('seven','seven7seven')
    line = line.replace('eight','eight8eight')
    line = line.replace('nine','nine9nine')
    running_sum += get_number(line)
print(f'Part two answer: {running_sum}')
