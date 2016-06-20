def sortLetters(s):
	st =[]
	for c in s:
		st.append(c)
	start = 0
	end = len(s) - 1
	while start <= end:
		while start <= end and not st[start].isupper():
			start += 1
		while start <= end and st[end].isupper():
			end -= 1
		if start <= end:
			st[start], st[end] = st[end], st[start]

	return "".join(st)

print sortLetters("aBcDeFg")