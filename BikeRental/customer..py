class Customer(object):
	"""Logging history for Customer"""
	def __init__(self, arg):
		self.bikes = 0
		self.rentalBasis = 0
		self.rentalTime = 0
		self.bill = 0
	
	def request_Bike(self):
		"""
        Takes a request from the customer for the number of bikes.
        """ 
		bikes = input("How many bikes would you like to rent?")
		# validate  input
		try:
			bikes = int(bikes)
		except ValueError:
			print("Not a positive integer!")
			return -1 
		