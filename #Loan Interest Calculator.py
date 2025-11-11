

print("Loan Interest Calculator ")

bill_amount = float(input('How much was loaned? '))

fam_input = input('Are you family? True/False ').strip().lower()
if fam_input == 'true':
    interest_percentage = 6
else:
    interest_percentage = 8

amount = (interest_percentage / 100) * bill_amount
total_amount = bill_amount + amount

print(f"They owe P{total_amount}")