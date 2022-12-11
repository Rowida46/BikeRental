
import sys

sys.path.append("..")

from BikeRental.rent import BikeRental
from BikeRental.Customer import Customer

def main():
    shop = BikeRental()
    customer = Customer()


if __name__ == '__main__':
    main()