monthely_income = int(input("Enter your monthly income: "))
monthely_expenses= int(input("Enter your monthly expenses: "))
monthely_saving = monthely_income - monthely_expenses
project_saving = monthely_saving*12+(monthely_saving*12*0.05)

print("Your monthly saving are $", monthely_saving)
print("Projection savings after one year, with interest, is: $", project_saving)