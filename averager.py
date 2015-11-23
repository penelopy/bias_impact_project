class Averager:

	def __init__(self):
		self.numbers = []
		self.total = 0

	def add(self, n):
		"""add number to numbers list"""
		self.total += n
		# self.numbers.append(n)

	def get_total(self):
		"""sum numbers list"""
		return self.total

	def get_average(self):
		"""get average of numbers list"""
		return self.total / float(len(self.numbers))
