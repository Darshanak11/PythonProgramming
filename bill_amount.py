bill=float(input("enter the total bill amount:$"))

if bill>200:
 discount=0.15
else:
 discount=0.05

discount_amount=bill*discount
final_bill=bill-discount_amount

print(f"discount applied:${discount_amount:2f}")
print(f"final bill amount:${final_bill:2f}")
