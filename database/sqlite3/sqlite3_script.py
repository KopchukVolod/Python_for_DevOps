# Import module 
import sqlite3


#  Create connection object
con = sqlite3.connect("hotel_booking.db")

#  Create cursor object
cur = con.cursor()

#  View first row of booking_summary
result1 = cur.execute('''SELECT * FROM booking_summary''').fetchone()
#print(result1)

#  View first ten rows of booking_summary 
result2 = cur.execute('''SELECT * FROM booking_summary''').fetchmany(10)
#print(result2)

#  Create object bra and print first 5 rows to view data
bra = cur.execute('''SELECT * FROM booking_summary WHERE country = "BRA"; ''').fetchall()
# print(bra)


#  Create new table called bra_customers
cur.execute('''CREATE TABLE IF NOT EXISTS bra_customers (num INTEGER, 
hotel TEXT, 
is_cancelled INTEGER, 
lead_time INTEGER, 
arrival_date_year INTEGER, 
arrival_date_month TEXT, 
arrival_date_day_of_month INTEGER, 
adults INTEGER, 
children INTEGER, 
country TEXT, 
adr REAL, 
special_requests INTEGER)''')

#  Insert bject bra into the table bra_customers 
cur.executemany('''INSERT INTO bra_customers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', bra)

#  View the first 10 rows of bra_customers
bra_customers = cur.execute('''SELECT * FROM bra_customers''').fetchmany(10)
#print(bra_customers)

#  Retrieve lead_time rows where the bookings were canceled
lead_time_can = cur.execute('''SELECT lead_time FROM bra_customers WHERE is_cancelled = 1;''').fetchall()

#  Find average lead time for those who canceled and print results
sum = 0
len_ones = len(lead_time_can)
for num in lead_time_can:
    sum = sum + num[0]

average_value = sum / len_ones
print(average_value)

#  Retrieve lead_time rows where the bookings were not canceled
lead_time_is_not_cancelled = cur.execute('''SELECT lead_time FROM bra_customers WHERE is_cancelled = 0;''').fetchall()

#  Find average lead time for those who did not cancel and print results
sum1 = 0
len_ones1 = len(lead_time_is_not_cancelled)
for num1 in lead_time_is_not_cancelled:
    sum1 = sum1 + num1[0]
    average_value1 = sum1 / len_ones1
print(average_value1)

#  Retrieve special_requests rows where the bookings were canceled
special_requests_cancelled = cur.execute('''SELECT special_requests FROM bra_customers WHERE is_cancelled = 1;''').fetchall()
#print(special_requests_cancelled)

#  Find total speacial requests for those who canceled and print results
total_special_requests = 0
for request in special_requests_cancelled:
    total_special_requests += request[0]

print(total_special_requests)

#  Retrieve special_requests rows where the bookings were not canceled
special_requests_not_cancelled = cur.execute('''SELECT special_requests FROM bra_customers WHERE is_cancelled = 0;''').fetchall()

#  Find total speacial requests for those who did not cancel and print results
total_special_requests1 = 0
for request1 in special_requests_not_cancelled:
    total_special_requests1 += request1[0]

print(total_special_requests1)


#  Commit changes and close the connection
con.commit()

con.close()
