import unittest
from datetime import datetime, timedelta
import sys

sys.path.append("..")

from BikeRental.rent import BikeRental, RentalBasis
from BikeRental.Customer import Customer

class BikeRentalTest(unittest.TestCase):

	def test_Bike_Rental_diplays_correct_stock(self):
		shop1 = BikeRental()
		shop2 = BikeRental(10)
		self.assertEqual(shop1.stock, 0)
		self.assertEqual(shop2.stock, 10)

	def test_out_of_stock_number_of_bikes(self):
		shop1 = BikeRental(10)
		shop2 = BikeRental(2)
		self.assertEqual(shop1.rentBikeOnHourlyBasis(20), None)
		self.assertEqual(shop2.rentBikeOnHourlyBasis(7), None)

	def test_rentBikeOnHourlyBasis_for_valid_positive_number_of_bikes(self):
		shop1 = BikeRental(0)
		self.assertEqual(shop1.rentBikeOnHourlyBasis(20), None)
	
	def test_rentBikeOnHourlyBasis_for_negative_number_of_bikes(self):
		shop1 = BikeRental(10)
		shop2 = BikeRental(20)
		self.assertEqual(shop1.rentBikeOnHourlyBasis(-10), None)
		self.assertEqual(shop2.rentBikeOnHourlyBasis(0), None)

	def test_rentBikeOnHourly_or_WeeklyBasis_for_invalid_positive_number_of_bikes(self):
		shop1 = BikeRental(10)
		self.assertEqual(shop1.rentBikeOnDailyBasis(20,RentalBasis.daily),None )
		self.assertEqual(shop1.rentBikeOnDailyBasis(0,RentalBasis.daily),None )
		self.assertEqual(shop1.rentBikeOnDailyBasis(-20,RentalBasis.daily),None )
		self.assertEqual(shop1.rentBikeOnDailyBasis(20,RentalBasis.weekly),None )
		self.assertEqual(shop1.rentBikeOnDailyBasis(0,RentalBasis.weekly),None )
		self.assertEqual(shop1.rentBikeOnDailyBasis(-20,RentalBasis.weekly),None )

	def test_rentBikeOnWeekly_or_daily_Basis_for_valid_positive_number_of_bikes(self):
		shop = BikeRental(10)
		hour = datetime.now().hour
		self.assertEqual(shop.rentBikeOnDailyBasis(2, RentalBasis.weekly).hour, hour)
		self.assertEqual(shop.rentBikeOnDailyBasis(3, RentalBasis.daily).hour, hour)

	def test_returnBike_for_invalid_rentalTime(self):
		shop = BikeRental(20)
		customer = Customer()
		# let the customer not rent a bike a try to return one.
		request = customer.returnBike()
		self.assertIsNone(shop.returnBike(request))
		# manually check return function with error values
		self.assertIsNone(shop.returnBike((0,0,0)))

	def test_returnBike_for_invalid_rentalBasis(self):
		# create a shop and a customer
		shop = BikeRental(10)
		customer = Customer()
		# create valid rentalTime and bikes
		customer.rentalTime = datetime.now()
		customer.bikes = 3
		# create invalid rentalbasis
		customer.rentalBasis = ""
		request = customer.returnBike()
		self.assertEqual(shop.returnBike(request), None)
	
	def test_returnBike_for_invalid_numOfBikes(self):
		# create a shop and a customer
		shop = BikeRental(10)
		customer = Customer()
		# create valid rentalTime and bikes
		customer.rentalTime = datetime.now()
		# create invalid number of bikes
		customer.bikes = 0
		customer.rentalBasis = RentalBasis.weekly
		request = customer.returnBike()
		self.assertEqual(shop.returnBike(request), None)

	def test_returnBike_with_valid_credentials(self):
		shop = BikeRental(150)
		customer1 = Customer()
		customer2 = Customer()
		customer3 = Customer()
		customer4 = Customer()
		
		# create valid rentalBasis for each customer
		customer1.rentalBasis = RentalBasis.daily # hourly
		customer2.rentalBasis = RentalBasis.weekly
		customer3.rentalBasis = RentalBasis.hourly
		customer4.rentalBasis = RentalBasis.weekly

		# create a valid number of bikes for each customer
		customer1.bikes = 1
		customer2.bikes = 2 # for family discount 
		customer3.bikes = 7 
		customer4.bikes = 2

		# create a valid rentalTime for each customer
		customer1.rentalTime = datetime.now() + timedelta(days=-4)
		customer2.rentalTime = datetime.now() + timedelta(weeks=-2)
		customer3.rentalTime = datetime.now() + timedelta(hours=-23)
		customer4.rentalTime = datetime.now() + timedelta(weeks=-4)

        # get customers' requests
		request1 = customer1.returnBike()
		request2 = customer2.returnBike()
		request3 = customer3.returnBike()
		request4 = customer4.returnBike()

		# check if all of them get correct bill
		self.assertEqual(shop.returnBike(request1), 80)
		self.assertEqual(shop.returnBike(request2), 240)
		self.assertEqual(shop.returnBike(request3), 805)
		self.assertEqual(shop.returnBike(request4), 480)

tst = BikeRentalTest()
#tst.test_rentBikeOnHourlyBasis_for_negative_number_of_bikes()

tst.test_returnBike_with_valid_credentials()