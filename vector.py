class Viktor:

	def __init__(self,x):
		self.x=x

	def __str__(self,other):
		self.x=self.x+other.x
		return 'Viktor walked %r m road' % (self.x)

	def __bool__(self):
		return bool(abs(self.x))

	def plus3r(self,other,third):
		return self.x+other.x+third.x

	def __abs__(self):
		return abs(self.x)

	def __add__(self,other):
		# self.x+other.x
		return self.__str__(other)

	def __len__(self):
		return len(self.__str__())

if __name__ == '__main__':
	firstday=Viktor(329) # He walked 329 m first day
	secondday=Viktor(500) # He walked over 500 m on second day
	# print(firstday)
	# print(secondday)
	thirdday=Viktor(129) # He walked 129 m on the third day
	fourthday=Viktor(1182) # On the fourth day, he walked over 1182 m
	# print(thirdday+fourthday)
	print(fourthday+thirdday)