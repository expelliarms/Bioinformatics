from __future__ import division
with open('rosalind_gc.txt') as f:
    content = f.readlines()
# print content
maxp = 0
name = ""
maxname =""
tot = 0
countgc = 0	
perc = 0	
for x in content:
	if x[0] == '>':
		if perc > maxp:
			maxp = perc
			maxname = name
		name = x[1:len(x)-1]
		tot = 0
		countgc = 0		
	else:
		countgc += x.count('G')
		countgc += x.count('C')
		tot = tot + x.count('A') + x.count('T') + x.count('G') + x.count('C') 
		perc = (countgc/tot)*100
if perc > maxp:
	maxp = perc
	maxname = name	
print maxname
print maxp