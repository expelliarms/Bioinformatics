str1 = raw_input()
str2 = raw_input()
distance = 0
for i, c in enumerate(str1):
	if str2[i] != c:
		distance += 1
print distance