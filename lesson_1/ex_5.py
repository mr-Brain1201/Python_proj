proceeds = float(input('Enter amount of proceeds: '))
expenses = float(input('Enter amount of expenses: '))
if proceeds < expenses:
    print(f'Your amount of loss: {(expenses - proceeds) :.2f}')
elif proceeds == expenses:
    print('Work to zero')
else:
    print(f'Your profitability: {(proceeds / expenses) :.2f}')
if proceeds > expenses:
    num_of_employees = int(input('Enter the number of employees: '))
    print(f'Profit per employee: {((proceeds - expenses) / num_of_employees) :.2f}')
