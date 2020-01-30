def int_to_symbol(a:int) :
	"""
	>>>int_to_symbol(0)
	'0'
	>>>int_to_symbol(35)
	'Z'
	>>>int_to_symbol(10)
	'A'
	>>>int_to_symbol(9)
	'9'
	"""
	if (a < 0 or a > 35) :
		return (None)
	if (a <= 9) :
		return (chr(ord('0') + a))
	return (chr(ord('A') + a - 10))

def int_to_string_base(n:int, base:int) :
	"""
	>>>int_to_string_base(15, 16)
	'F'
	>>>int_to_string_base(88, 8)
	'130'
	>>>int_to_string_base(17, 2)
	'10001'
	"""
	ret = ""
	while (n >= base) :
		tmp = n % base
		ret += int_to_symbol(tmp)
		n //= base
	ret += int_to_symbol(n)
	return (ret[::-1])

def factorial(n:int) :
	if (n < 1) :
		return (1)
	return (n * factorial(n - 1))

def conv_big_numb(n:int) :
	if (n < 1000) :
		return (int_to_string_base(n, 10))
	taille = 0
	while (n >= 1000) :
		n //= 1000
		taille += 1
	l = "KMGT"
	ret = int_to_string_base(n, 10)
	if (taille <= 4) :
		ret += l[taille - 1]
		return (ret)
	taille -= 5
	ret += str(chr(ord('a') + taille // 26) + chr(ord('a') + (taille % 26)))
	return (ret)

i = 0
while (i < 30) :
	print(conv_big_numb(factorial(i)))
	i += 1

