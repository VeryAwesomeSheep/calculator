import unittest
import arithmetics

class TestArithmeticOperations(unittest.TestCase):
	def test_add(self):
		self.assert_(arithmetics.ArithmeticOperators.add("5", "13") == "18")
	
	def test_sub(self):
		self.assert_(arithmetics.ArithmeticOperators.sub("11", "13") == "-2")

	def test_mul(self):
		self.assert_(arithmetics.ArithmeticOperators.mul("12", "3") == "36")

	def test_div(self):
		self.assert_(arithmetics.ArithmeticOperators.div("12", "3") == "4.0")

	def test_square(self):
		self.assert_(arithmetics.ArithmeticOperators.square("5") == "25")

	def test_cube(self):
		self.assert_(arithmetics.ArithmeticOperators.cube("5") == "125")

	def test_squareRoot(self):
		self.assert_(arithmetics.ArithmeticOperators.squareRoot("5", "16") == "20.0")

	def test_cubeRoot(self):
		self.assert_(arithmetics.ArithmeticOperators.cubeRoot("2", "8") == "4.0")

	def test_evaluate(self):
		self.assert_(arithmetics.Evaluate.evaluate("2+3+8-44*16/4") == "-163.0")
		self.assert_(arithmetics.Evaluate.evaluate("1+2*3-6/2") == "4.0")

if __name__ == "__main__":
	unittest.main(verbosity=2)