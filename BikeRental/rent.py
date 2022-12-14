from datetime import datetime, timedelta
from enum import Enum

class RentalBasis(Enum):
	"""
	This class is created to get rid of and ditch 
	this annoying string comparssion & provide 
	our provided Rental Basis.
	"""
	daily = "DailyBasis"
	weekly = "WeeklyBasis"
	hourly = "HourlyBasis"


class BikeRental():
	"""docstring for ClassName"""
	def __init__(self, stock = 0):
		self.__stock = stock

	@property
	def stock(self):
		"""
		Displays the bikes currently available for rent in the shop.
		"""
		print(f"We have currently {self.__stock} bikes available to rent")
		return self.__stock

	@stock.setter
	def stock(self, val):
		self.__stock = val

	def rentBikeOnHourlyBasis(self, n):
		"""
		Rents a bike on hourly basis to a customer.
		"""
		if self.__stock and self.__stock > n and n > 0:
			now = datetime.now()                      
			print("You have rented a {} bike(s) on hourly basis today at {} hours.".format(n,now.hour))
			print("You will be charged $5 for each hour per bike.")
			print("We hope that you enjoy our service.")
			self.stock -= n
			return now
		else :
			error_msg = f"Sorry! We have currently {self.stock} bikes available to rent." if self.__stock < n else "Number of bikes should be positive!"       
			print(error_msg)
			return None

	def rentBikeOnDailyBasis(self, n, perioed = RentalBasis.daily):
		"""
		Rents a bike on daily basis to a customer.
		"""
		if n < self.stock and n> 0:
			now, cost = datetime.now(), " $20 "  if perioed == RentalBasis.daily else " $60 "                    
			perioed = "daily" if perioed == RentalBasis.daily else "weekly"
			print("You have rented {} bike(s) on daily basis today at {} hours.".format(n, now.hour))
			print(f"You will be charged {cost} for each {perioed} per bike.")
			print("We hope that you enjoy our service.")
			self.stock -= n
			return now 
		else :
			# to validate it's not an out of stock order and a valid number or orders were given.
			error_msg = f"Sorry! We have currently {self.stock} bikes available to rent." if n > self.stock else "Number of bikes should be positive!"
			print(error_msg)
			return None

	def validate_bill(self, request):
		return all(request)  #  rentalTime and rentalBasis and numOfBikes
	
	def rent_back(self, numOfBikes, rentalTime):
		self.stock += numOfBikes # take back
		now = datetime.now()
		rentalPeriod = now - rentalTime # calc perioed
		return rentalPeriod

	def family_discount(self, bill):
		print("You are eligible for Family rental promotion of 30% discount")
		bill = bill * 0.7
		print("Thanks for returning your bike. Hope you enjoyed our service!")
		print("That would be ${}".format(bill))
		return bill

	def calc_bill(self, rentalBasis, rentalPeriod, numOfBikes):
		if rentalBasis == RentalBasis.hourly:
			# hourly bill calculation
			bill = round(rentalPeriod.seconds / 3600) * 5 * numOfBikes
		elif rentalBasis == RentalBasis.daily:
			# daily bill calculation
			bill = round(rentalPeriod.days) * 20 * numOfBikes
		elif rentalBasis == RentalBasis.weekly:
           	# weekly bill calculation
			bill = round(rentalPeriod.days / 7) * 60 * numOfBikes	
		return bill

	def returnBike(self, request):
		"""
		1. Accept a rented bike from a customer
		2. Replensihes the inventory
		3. Return a bill
		"""
		rentalTime, rentalBasis, numOfBikes = request
		# issue a bill only if all three parameters are not null!
		if self.validate_bill(request):
			print("A Valid Bill Request Provided!")
			rentalPeriod = self.rent_back(numOfBikes,rentalTime)
			bill = self.calc_bill(rentalBasis, rentalPeriod, numOfBikes)		
			# family discount calculation
			if numOfBikes in range(3,6):
				bill = self.family_discount(bill)
			return bill

		else :
			print("Are you sure you rented a bike with us?")
			return None


