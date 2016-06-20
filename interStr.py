def isInterleave(s1, s2, s3):
	if len(s1) + len(s2) != len(s3):
		return False
	if not s1 and not s2 and not s3:
		return True
	dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]

	dp[0][0] = True
	for i in xrange(1, len(s1) + 1):
		if s1[i - 1] == s3[i - 1]:
			dp[i][0] = dp[i - 1][0]
	for i in xrange(1, len(s2) + 1):
		if s2[i - 1] == s3[i - 1]:
			dp[0][i] = dp[0][i - 1]

	for i in xrange(1, len(s1) + 1):
		for j in xrange(1, len(s2) + 1):
			if s3[i + j - 1] == s1[i - 1]:
				dp[i][j] = dp[i-1][j]
			elif s3[i + j - 1] == s2[j - 1]:
				dp[i][j] = dp[i][j-1]
			# for c in dp:
			# 	print c, i,s3[i+j-1],s1[i-1],s2[j-1], j
			# print ""
	return dp[-1][-1]

print isInterleave("sdfjas;dfjoisdufzjkndfasdkfja;sdfa;dfa;dfaskdjhfasdhjdfakhdgfkajdfasdjfgajksdfgaksdhfasdkbfjkdsfbajksdfhakjsdfbajkdfbakdjsfgaksdhgfjkdsghfkdsfgadsjfgkajsdgfkjasdfh", "dfnakdjnfjkzghdufguweygfasjkdfgb2gf8asf7tgbgasjkdfgasodf7asdgfajksdfguayfgaogfsdkagfsdhfajksdvfbgkadsghfakdsfgasduyfgajsdkfgajkdghfaksdgfuyadgfasjkdvfjsdkvfakfgauyksgfajkefgjkdasgfdjksfgadjkghfajksdfgaskdjfgasjkdgfuyaegfasdjkfgajkdfygadjskfgjkadfg", "sdfjas;dfjoisdfnakdjnfjkzghdufguwdufzjkeygfasjkdfgb2gf8asf7ndtgbgasjkdfgasodf7asdfgfajkasdksdfguayfgaogfsdkagfsfjadhfajksdvfbgkadsghfa;sdkdsfgasduyfgajsdkfgafajkdghfaksdgfuyadgfas;dfjkdvfjsdkvfakfgauyksa;dgfajkefgjkdasgfdjksffaskdjhfasdhjdfakhdgadjkghfajgfkajdfksdfgaskdjfgasjkdgfuasdjfgajksdfgaksdhfasdkbfjkdsfbajksdfyaegfasdjkfgajkdfygadjskfgjkadfghakjsdfbajkdfbakdjsfgaksdhgfjkdsghfkdsfgadsjfgkajsdgfkjasdfh")

	