from random import randint

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


def Check_base_change(n:int) :
	"""
	>>>Check_base_change(456)
	True
	>>>Check_base_change(1464)
	True
	>>>Check_base_change(9854641)
	True
	>>>Check_base_change(4611315)
	True
	"""
	p = randint(1, n)
	base = randint(2, 36)
	ret = int(int_to_string_base(p, base), base)
	if (ret != p):
		return (False)
	return (True)

def bin_add(a:int, b:int) :
	bin_a = int_to_string_base(a, 2)
	bin_b = int_to_string_base(b, 2)
	res = a + b
	bin_res = int_to_string_base(res, 2)
	l_a = len(bin_a)
	l_res = len(bin_res)
	l_b = len(bin_b)
	print(" " * (2 + l_res - l_a) + bin_a + "  :", a, "\n+" + " " * (1 + l_res - l_b) + bin_b + "  :", b, "\n" + "-" * (l_res + 2) + "\n" + "  " + bin_res + "  :", res)

a = randint(1, 100)
b = randint(1, 100)
bin_add(a, b)
