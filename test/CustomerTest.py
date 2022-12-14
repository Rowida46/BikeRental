import sys
sys.path.append("..")

import unittest
from datetime import datetime, timedelta
from BikeRental.Customer import Customer
from BikeRental.rent import BikeRental, RentalBasis

class CustomerTest(unittest.TestCase):
	def test_return_Bike_with_valid_input(self):
		# create a customer
		customer = Customer()
		now = datetime.now()
		customer.rentalTime = now
		customer.rentalBasis = RentalBasis.daily
		customer.bikes = 4
		self.assertEqual(customer.returnBike(),(now,RentalBasis.daily, 4))

	def test_return_Bike_with_invalid_input(self):
 		# create a customer
		customer = Customer()

	    # create valid rentalBasis and bikes
		customer.rentalBasis = 1
		customer.bikes = 0
		# create invalid rentalTime
		customer.rentalTime =  0
		self.assertEqual(customer.returnBike(),(0,0,0))

test = CustomerTest()
test.test_return_Bike_with_invalid_input()