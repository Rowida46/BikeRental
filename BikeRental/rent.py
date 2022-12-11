from datetime import datetime
from enum import Enum

class RentalBasis(Enum):
	"""
	This class is created to get rid of and ditch this annoying string comparssion.
	"""
	daily = "DailyBasis"
	weekly = "WeeklyBasis"
	hourly = "HourlyBasis"


class BikeRental(object):
	"""docstring for bike rental shop"""
	def __init__(self, stock = 0):
		self.stock = stock

	@property
	def stock(self):
		"""
        Displays the bikes currently available for rent in the shop.
        """
		return f"We have currently {self.stock} bikes available to rent"

	def rentBikeOnHourlyBasis(self, n):
		"""
        Rents a bike on hourly basis to a customer.
        """
		if self.stock:
			now = datetime.datetime.now()                      
			print("You have rented a {} bike(s) on hourly basis today at {} hours.".format(n,now.hour))
			print("You will be charged $5 for each hour per bike.")
			print("We hope that you enjoy our service.")
			self.stock -= n
			return now
		else :       
			error_msg = f"Sorry! We have currently {self.stock} bikes available to rent." if not self.stock else "" + \
			        	"\n Number of bikes should be positive!" if not n else ""
			return error_msg

	def rentBikeOnDailyBasis(self, n, perioed = RentalBasis.daily):
		"""
        Rents a bike on daily basis to a customer.
        """
		if n < self.stock:
			now, cost = datetime.now(), " $20 "  if perioed == RentalBasis.daily else " $60 "                    
			print("You have rented {} bike(s) on daily basis today at {} hours.".format(n, now.hour))
			print(f"You will be charged {cost} for each {perioed} per bike.")
			print("We hope that you enjoy our service.")
			self.stock -= n
			return now
		else :
			# to validate it's not an out of stock order and a valid number or orders were given.
			error_msg = f"Sorry! We have currently {self.stock} bikes available to rent." if n > self.stock else "Number of bikes should be positive!"
			return error_msg

	def validate_bill(self, request):
		return all(request) #  rentalTime and rentalBasis and numOfBikes
	
	def rent_back(self, numOfBikes, rentalTime):
		self.stock += numOfBikes # take back
		now = datetime.datetime.now()
		rentalPeriod = now - rentalTime # calc perioed
		return rentalPeriod
	
	def family_discount(self, bill):
		print("You are eligible for Family rental promotion of 30% discount")
		bill = bill * 0.7
		print("Thanks for returning your bike. Hope you enjoyed our service!")
		print("That would be ${}".format(bill))
		return bill

	def calc_bill(self, rentalBasis):
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
			rentalPeriod = self.rent_back(numOfBikes,rentalTime)
			bill = self.calc_bill(rentalBasis)			
			# family discount calculation
			if numOfBikes in range(3,6):
				bill = self.family_discount(self, bill)
				return bill
		else :
			return "Are you sure you rented a bike with us?"