str1 = raw_input()
str2 = raw_input()
L = len(str1)
i = 0
flag = 1
while (i < L and flag):
	idx = str1.find(str2, i)
	if idx == -1:
		flag = 0
		break
	print idx + 1,
	i = idx + 2