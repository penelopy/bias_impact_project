class Averager:

	def __init__(self):
		self.numbers = []

	def add(self, n):
		"""add number to numbers list"""
		self.numbers.append(n)

	def get_total(self):
		"""sum numbers list"""
		return sum(self.numbers)

	def get_average(self):
		"""get average of numbers list"""
		return sum(self.numbers) / float(len(self.numbers))

	def get_median(self):
		"""get median of numbers list"""
		self.numbers.sort()

		num_len = len(self.numbers)
		if num_len == 0:
			return 0
		elif num_len == 1:
			return self.numbers[0]
		elif num_len % 2 == 0:
			return (self.numbers[num_len / 2 - 1] + self.numbers[num_len / 2]) / 2.0
		else:
			return self.numbers[num_len / 2]
