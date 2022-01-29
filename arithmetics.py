import math, re

class ArithmeticOperators:
	def add(arg1, arg2):
		if "." in arg1 or "." in arg2:
			return str(float(arg1) + float(arg2))
		else:
			return str(int(arg1) + int(arg2))

	def sub(arg1, arg2):
		if "." in arg1 or "." in arg2:
			return str(float(arg1) - float(arg2))
		else:
			return str(int(arg1) - int(arg2))

	def mul(arg1, arg2):
		if "." in arg1 or "." in arg2:
			return str(float(arg1) * float(arg2))
		else:
			return str(int(arg1) * int(arg2))

	def div(arg1, arg2):
		if "." in arg1 or "." in arg2:
			return str(float(arg1) / float(arg2))
		else:
			return str(int(arg1) / int(arg2))

	def square(arg1):
		if "." in arg1:
			result = float(arg1)**2
			return str(result)
		else:
			result = int(arg1)**2
			return str(result)

	def cube(arg1):
		if "." in arg1:
			result = float(arg1)**3
			return str(result)
		else:
			result = int(arg1)**3
			return str(result)

	def squareRoot(arg1, arg2):
		if arg1 == '':
			arg1 = "1"

		result = float(arg1) * math.sqrt(float(arg2))
		return str(result)

	def cubeRoot(arg1, arg2 = 1):
		if arg1 == '':
			arg1 = "1"

		result = float(arg1) * (float(arg2) ** (1. / 3))
		return str(result)

class Evaluate:
	def evaluate(equation):
		while "³" in equation:
			regex = re.search(r"(-?\d+\.?\d*)³", equation)
			if regex != None:
				result = ArithmeticOperators.cube(regex.group(1))
				equation = equation[0:regex.start()] + result + equation[regex.end():]
		while "²" in equation:
			regex = re.search(r"(-?\d+\.?\d*)²", equation)
			if regex != None:
				result = ArithmeticOperators.square(regex.group(1))
				equation = equation[0:regex.start()] + result + equation[regex.end():]
		while "∛" in equation:
			regex = re.search(r"(-?\d*\.?\d*)∛(-?\d+\.?\d*)", equation)
			if regex != None:
				result = ArithmeticOperators.cubeRoot(regex.group(1), regex.group(2))
				equation = equation[0:regex.start()] + result + equation[regex.end():]
		while "√" in equation:
			regex = re.search(r"(-?\d*\.?\d*)√(-?\d+\.?\d*)", equation)
			if regex != None:
				result = ArithmeticOperators.squareRoot(regex.group(1), regex.group(2))
				equation = equation[0:regex.start()] + result + equation[regex.end():]
		while "*" in equation:
			regex = re.search(r"(-?\d*\.?\d*)\*(-?\d+\.?\d*)", equation)
			if regex != None:
				result = ArithmeticOperators.mul(regex.group(1), regex.group(2))
				equation = equation[0:regex.start()] + result + equation[regex.end():]
		while "/" in equation:
			regex = re.search(r"(-?\d*\.?\d*)/(-?\d+\.?\d*)", equation)
			if regex != None:
				result = ArithmeticOperators.div(regex.group(1), regex.group(2))
				equation = equation[0:regex.start()] + result + equation[regex.end():]
		while "+" in equation:
			regex = re.search(r"(-?\d+\.?\d*)\+(-?\d+\.?\d*)", equation)
			if regex != None:
				result = ArithmeticOperators.add(regex.group(1), regex.group(2))
				if result == "0":
					result = "+" + result
				equation = equation[0:regex.start()] + result + equation[regex.end():]
		while "-" in equation:
			if equation[0] == "-":
				if equation.count("-") == 1:
					break
			else:
				regex = re.search(r"(-?\d+\.?\d*)-(-?\d+\.?\d*)", equation)
				if regex != None:
					if regex.group(2)[0] == "-":
						result = ArithmeticOperators.sub(regex.group(1), regex.group(2))
					else:
						result = ArithmeticOperators.sub(regex.group(1), regex.group(2))
					equation = equation[0:regex.start()] + result + equation[regex.end():]

		return equation