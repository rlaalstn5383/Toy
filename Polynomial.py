class Polynomial:
	def __init__(self, expr):
		self._expr_list = []

		if isinstance(expr, list):
			self._expr_list = expr
			return

		assert isinstance(expr, str)

		try:
			expr_tuple = eval("(%s)" %expr)
		except:
			raise SyntaxError("%s is not polynomial tuple" %expr)
		for _expr in expr_tuple:
			if not isinstance(_expr, tuple):
				raise SyntaxError("%s is not tuple" %str(_expr))
			if len(_expr) != 2:
				raise SyntaxError("%s is not double" %str(_expr))
			if not(isinstance(_expr[0], int) and isinstance(_expr[1], int)):
				raise SyntaxError("%s does not contain integers" %str(_expr))
			while len(self._expr_list) <= _expr[1]:
				self._expr_list.append(0)
			if self._expr_list[_expr[1]] != 0:
				raise SyntaxError("%s already exists" %str(_expr))
			self._expr_list[_expr[1]] = _expr[0]

	def __str__(self):
		_str_list = []
		for index in range(len(self._expr_list)):
			if self._expr_list[index] != 0:
				_str_list.append("%dx**%d" %(self._expr_list[index], index))
		return " + ".join(_str_list)

	def __len__(self):
		return len(self._expr_list)

	def __getitem__(self, index):
		return self._expr_list[index]

	def __add__(self, rhs):
		return self.add(rhs)

	def __sub__(self, rhs):
		return self.sub(rhs)

	def __mul__(self, rhs):
		return self.mul(rhs)

	def add(self, rhs):
		assert isinstance(rhs, Polynomial)

		ret = [0] * max(len(self), len(rhs))

		for i in range(max(len(self), len(rhs))):
			try:
				self_val = self[i]
			except IndexError:
				self_val = 0
			try:
				rhs_val = rhs[i]
			except IndexError:
				rhs_val = 0
			ret[i] = self_val + rhs_val
		return Polynomial(ret)

	def negate(self):
		return Polynomial(list(map(lambda x: -x, self._expr_list[:])))

	def sub(self, rhs):
		assert isinstance(rhs, Polynomial)

		return self.add(rhs.negate())

	def mul_x(self):
		return Polynomial([0] + self._expr_list[:])

	def mul_number(self, n):
		return Polynomial(list(map(lambda x: n * x, self._expr_list[:])))

	def mul(self, rhs):
		ret = Polynomial([])
		cur = self.mul_number(1)

		for i in rhs._expr_list:
			ret += cur.mul_number(i)
			cur = cur.mul_x()

		return ret

if __name__ == "__main__":
	lhs = Polynomial("(1,1),(3,5),(4,2)")
	rhs = Polynomial("(2,0),(3,2)")
	print "%s + %s = %s" %(lhs, rhs, lhs + rhs)
	print "%s - %s = %s" %(lhs, rhs, lhs - rhs)
	print "%s * %s = %s" %(lhs, rhs, lhs * rhs)