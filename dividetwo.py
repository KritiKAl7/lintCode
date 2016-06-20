def divide(dividend, divisor):
	if divisor == 0:
		return 2147483647
	if divisor == 1:
		return dividend

	c = 0
	
	while dividend > 0:
		dividend -= divisor
		c += 1
		print dividend, c

	
	if dividend < 0:
		c -= 1

	return c

print divide(10000000000000,1)