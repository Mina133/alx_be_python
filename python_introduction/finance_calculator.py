monthely_income = int(input("Enter your monthly income: "))
monthely_expenses= int(input("Enter your monthly expenses: "))
monthely_savings = monthely_income - monthely_expenses
project_saving = int(monthely_savings*12+(monthely_savings*12*0.05))

print("Your monthly saving are $", monthely_savings)
print("Projection savings after one year, with interest, is: $", project_saving)