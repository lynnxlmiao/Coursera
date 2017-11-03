import re
data = open('regex_sum_46353.txt')
numlist = list()
for line in data:
    line = line.rstrip()
    integers = re.findall('[0-9]+', line)
    if len(integers) < 1: continue

    for i in range(len(integers)):
        num = float(integers[i])
        numlist.append(num)

num_sum = sum(numlist)
print (num_sum)
