import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_logger = logging.FileHandler("cashier.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_logger.setFormatter(formatter)
logger.addHandler(file_logger)

print("Welcome to Food in a Jiffy!")

food_options = {
  "H": {
    "name": "Hamburger",
    "price": 2.49
    },
  "C": {
    "name": "Cheeseburger",
    "price": 4.99
    },
  "F": {
    "name": "Fries",
    "price": 2.50
    },
  "D": {
    "name": "Drink",
    "price": 1.99
    },
  "E": {
    "name": "End Order",
    "price": 0.00
    }
}

def menu():
  for food in food_options:
    print("[{key}] {food_name}: ${food_price}".format(key=food, food_name=food_options[food]["name"], food_price=food_options[food]["price"]))

menu()
cost = 0

choice = str(input("\nSelect a letter corresponding to the menu choice to order: ")).upper()
logger.info("Selected menu choice: %s", choice)

while choice != "E":
  for key in food_options:
    if choice == key:
      food = food_options[key]
      try:
        num = int(input("\nHow many of the " + food['name'] + " would the customer like to order? "))
        logger.info("Selected quantity for %s: %d", food['name'], num)
        if num <= 0:
          logger.warning("Negative or zero quantity entered for %s, Using quantity of 1.", food['name'])
          print("\nInvalid number entered. Using quantity of 1.")
          num = 1
      except ValueError:
        logger.warning("Invalid quantity entered for %s", food['name'])
        print("\nInvalid number entered. Using quantity of 1.")
        num = 1

      food_price = round(food['price'] * num, 2)
      cost += food_price
      print("\n" + food['name'] + "\t ${food_price}".format(food_price=food_price))
      break

  choice = str(input("\nSelect a letter corresponding to the menu choice to order: ")).upper()
  logger.info("Selected menu choice: %s", choice)

if choice == "E":
  print("\nThe total for the order is ${cost}".format(cost=round(cost, 2)))
  money = float(input("\nEnter the amount paid by the customer:"))
  logger.info("Amount paid by customer: %.2f", money)
  if money < cost:
    logger.warning("Insufficient payment. Amount paid: %.2f", money)
    money = float(input("\nThere is not enough money. Please re-enter the amount paid:"))
    logger.info("Amount paid by customer (second attempt): %.2f", money)

  change = money - cost
  logger.info("Change for the customer: %.2f", change)

  if change < 0:
    logger.warning("Negative change for the customer: %.2f", change)
  print("The customer's change is ${change}".format(change=round(change, 2)))
