# BikeRental
_A simple fledged bike rental system._ 

## Customers can
- See available bikes on the shop
- Rent bikes on hourly basis $5 per hour.
- Rent bikes on daily basis $20 per day.
- Rent bikes on weekly basis $60 per week.
- Family Rental, a promotion that can include from 3 to 5 Rentals (of any type) with a discount of 30% of the total price.

## Rental Shop Can
- Issue a bill when customer decides to return the bike.
- Display available inventory
- Take requests on hourly, daily and weekly basis by cross verifying stock.

# Applied Concepts

- Delegation 
- Encapsulation
- Enum
- Decorators

## Unit-Test
Unit test module is written alongside the main program to rigorously test the classes and methods for errors. Most errors occur in Null values, negative values and non-integer inputs. Most of them have been taken care of.

## Project Structure 
```bash
BikeRental/
|-- BikeRental/
|   |-- Customer.py
|   |-- RentStore.py
|
|-- test/
|   |-- CustomerTest
|   |-- RentTest.py
|
|-- README
```

### Initial Setup:
* Clone the repository
* Run the command `python3 main.py`