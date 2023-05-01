names = ['Bubblegum', 'Toffee', 'Ice cream', 'Milk chocolate', 'Doughnut', 'Pancake']
profit = [202, 118, 2250, 1680, 1075, 80]
print('Earned amount:')
for i in range(6):
    print(names[i], '$' + str(profit[i]))
print()
print('Income: $' + str(sum(profit)))
staff = int(input('Staff expenses:'))
other = int(input('Other expenses:'))
print('Net income: $' + str(sum(profit) - staff - other))