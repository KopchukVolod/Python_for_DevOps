import random

from datetime import datetime

import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_logger = logging.StreamHandler(sys.stdout)
file_logger1 = logging.FileHandler("formatted.log")

formatter1 = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_logger.setFormatter(formatter1)
file_logger1.setFormatter(formatter1)

logger.addHandler(file_logger)
logger.addHandler(file_logger1)

class BankAccount:
  def __init__(self):
    self.balance=100
    logger.info("Hello! Welcome to the ATM Depot!")
        
  def authenticate(self):
    while True:
      pin = int(input("Enter account pin: "))
      logger.info("Entering the account pincode")
      if pin != 1234:
        logger.error("Error! Invalid pin. Try again.")
      else:
        return None
 
  def deposit(self):
    try:
      amount=float(input("Enter amount to be deposited: "))
      logger.info("Entering the account amount deposited")
      if amount < 0:
        logger.warning("Warning! You entered a negative number to deposit.")
      self.balance += amount
      logger.info("Amount Deposited: ${amount}".format(amount=amount))
      logger.info("Transaction Info:")
      logger.info("Status: Successful")
      logger.info("Transaction #{number}".format(number=random.randint(10000, 1000000)))
      logger.info("Timestamp: {timestamp}".format(timestamp=datetime.now()))
    except ValueError:
      logger.error("Error! You entered a non-number value to deposit.")
      logger.info("Transaction Info:")
      logger.info("Status: Failed")
      logger.info("Transaction #{number}".format(number=random.randint(10000, 1000000)))
      logger.info("Timestamp: {timestamp}".format(timestamp=datetime.now()))
 
  def withdraw(self):
    try:
      amount = float(input("Enter amount to be withdrawn: "))
      logger.info("Entering amount to be withdrawn")
      if self.balance >= amount:
        self.balance -= amount
        logger.info("You withdrew: ${amount}".format( amount=amount))
        logger.info("Transaction Info:")
        logger.info("Status: Successful")
        logger.info("Transaction #{number}".format(number=random.randint(10000, 1000000)))
      else:
        logger.error("Error! Insufficient balance to complete withdraw.")
        logger.info("Transaction Info:")
        logger.info("Status: Failed")
        logger.info("Transaction #{number}".format(number=random.randint(10000, 1000000)))
    except ValueError:
      logger.error("Error! You entered a non-number value to withdraw.")
      logger.info("Transaction Info:")
      logger.info("Status: Failed")
      logger.info("Transaction #{number}".format(number=random.randint(10000, 1000000)))
      logger.info("Timestamp: {timestamp}".format(timestamp=datetime.now()))
 
  def display(self):
    logger.info("Available Balance = ${balance}".format(balance=self.balance))
 
acct = BankAccount()
acct.authenticate()
acct.deposit()
acct.withdraw()
acct.display()
