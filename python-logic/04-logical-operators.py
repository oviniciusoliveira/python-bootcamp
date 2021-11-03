print('*-----Logical Operator (and)-----*')
high_income = True
good_credit = False

if high_income and good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

print('\n*-----Logical Operator (or)-----*')
high_income = True
good_credit = False

if high_income or good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

print('\n*-----Logical Operator (or)-----*')
student = True

print('\n*-----Logical Operator (not)-----*')
if not student:
    print("Eligible for loan")
else:
    print("Not eligible for loan")
