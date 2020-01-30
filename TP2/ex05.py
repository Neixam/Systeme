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

def bin_mul(a:int, b:int) :
    a_bin = int_to_string_base(a, 2)
    b_bin = int_to_string_base(b, 2)
    decal = 0
    res = []
    for char in b_bin[::-1] :
        if (char == '1') :
            elem = ""
            elem += a_bin
            elem += "." * decal
            res.append(elem)
        decal += 1
    res_bin = int_to_string_base(a * b, 2)
    res_len = len(res_bin)
    a_len = len(a_bin)
    b_len = len(b_bin)
    print(" " * (2 + res_len - a_len) + a_bin + " :", a)
    print("*" + " " * (1 + res_len - b_len) + b_bin + " :", b)
    print("-" * (2 + res_len))
    for step in res :
        print(" " * (2 + res_len - len(step)) + step)
    print("-" * (2 + res_len))
    print("  " + res_bin + " :", a * b)

a = randint(1, 100)
b = randint(1, 100)
bin_mul(a, b)
