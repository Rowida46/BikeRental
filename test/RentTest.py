import unittest
from datetime import datetime, timedelta
import sys
from BikeRental.rent import BikeRental

class BikeRentalTest(unittest.TestCase):

	def test_Bike_Rental_diplays_correct_stock(self):
		shop1 = BikeRental()
		shop2 = BikeRental(10)
		self.assertEqual(shop1.stock, 0)
		self.assertEqual(shop2.stock, 10)

	def test_rentBikeOnHourlyBasis_for_negative_number_of_bikes(self):
		shop1 = BikeRental(10)
		shop2 = BikeRental(20)
		self.assertEqual(shop1.rentBikeOnHourlyBasis(-10), None)
		self.assertEqual(shop2.rentBikeOnHourlyBasis(0), None)

	def test_out_of_stock_number_of_bikes(self):
		shop1 = BikeRental(10)
		shop2 = BikeRental(2)
		self.assertEqual(shop1.rentBikeOnHourlyBasis(20), None)
		self.assertEqual(shop2.rentBikeOnHourlyBasis(7), None)

tst = BikeRentalTest()
tst.test_rentBikeOnHourlyBasis_for_negative_number_of_bikes()

tst.test_out_of_stock_number_of_bikes()