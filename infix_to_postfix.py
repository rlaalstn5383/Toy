from __future__ import division
import random

NUMBERS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
OPS = ('+', '-', '/', '*')

def infix_to_postfix(infix_expr):
	try:
		result = eval(infix_expr)
	except SyntaxError:
		return "Syntax Error: %s" %infix_expr
	try:
		float(result)
	except ValueError:
		return "Cannot parse: %s" %infix_expr

	_infix_expr = infix_expr.replace('(', '').replace(')', '')

	if len(_infix_expr) % 2 == 0:
		return "Syntax Error"

	_ops = []
	_numbers = []
	for s in _infix_expr:
		if s in NUMBERS:
			_numbers.append(s)
		elif s in OPS:
			_ops.append(s)
		else:
			return "Invalid character: " %s


	def eval_postfix(numbers, ops):
		_ops = ops[:]
		_numbers = numbers[:]
		_ops.reverse()

		ret = float(_numbers.pop())
		while _numbers:
			ret = eval("%f%s%s" %(ret, _ops.pop(), _numbers.pop()))

		return ret

	while abs(eval_postfix(_numbers, _ops) - result) > 0.001:
		random.shuffle(_numbers)
		random.shuffle(_ops)

	return ''.join(_numbers) + ''.join(_ops)

if __name__ == '__main__':
	print '1+(2*3)/5/3', infix_to_postfix('1+(2*3)/5/3')