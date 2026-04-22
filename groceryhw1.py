rice_price = 45
sugar_price = 40
oil_price = 130

rice_qty = 3
sugar_qty = 2.5
oil_qty = 1.8

rice_total = rice_price * rice_qty
sugar_total = sugar_price * sugar_qty
oil_total = oil_price * oil_qty

print("Rice total=", rice_total)
print("Sugar total=", sugar_total)
print("Oil total=", oil_total)

final_total = rice_total + sugar_total + oil_total

final_total_str = str(final_total)

final_total_int = int(final_total)

print("Final Total (float):", final_total)
print("Final Total (integer):", final_total_int)
print("Final Total (string):", final_total_str)

import random
delivery_charge = random.randrange(5, 10)

final_bill = final_total + delivery_charge

print("Final Bill (with delivery):", final_bill)