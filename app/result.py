class Result:
	"""Result has two attrs, men and women. Each are an array of length levels
	where each elem is the count of gender at the indexed level"""

	def __init__(self, men, women):
		self.men = men
		self.women = women