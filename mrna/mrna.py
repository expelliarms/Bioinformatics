str1 = raw_input()
corr = {'F':2, 'L':6, 'I':3, 'M':1, 'V':4, 'S':6, 'P':4, 'T':4, 'A':4, 'Y':2, 'stop':3, 'H': 2, 'Q':2, 'N':2, 'K':2, 'D':2, 'E':2, 'C':2, 'W':1, 'R':6,'G':4}
ans = 3
for x in str1:
	ans = ans*corr[x]%1000000
print ans