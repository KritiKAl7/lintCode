#https://leetcode.com/discuss/72701/here-10-line-template-that-can-solve-most-substring-problems

from collections import counter
def minWindowSub(source, target):
	if not source or not target:
		return ""
	s = counter()
	t = counter()
	for i in source:
		s[i] += 1
	for j in target:
		t[j] += 1

	start = 0
	end = 0
	while start < len(source):
		for i in range(len(target)):