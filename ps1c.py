annual_salary  = float(input('Enter the starting salary: '))
total_cost = 1000000.0

semi_annual_raise = .0700
current_savings = 0
r = .0400
months = 36
steps = 0
low = 0.0
high = 1000.0
guess_rate = (low+high)/2.000
portion_down_payment = total_cost*0.25
monthly_salary = annual_salary/12
while abs(current_savings - portion_down_payment) >= 100:
    current_savings = 0
    rate = guess_rate/10000
    for month in range(36):
      if months % 6 == 0 and months > 0:
        annual_salary += annual_salary*semi_annual_raise
        monthly_salary = annual_salary/12
        current_savings += monthly_salary*rate+current_savings*r/12
      if current_savings < portion_down_payment:
         low = guess_rate
      else:
        high = guess_rate
    guess_rate = (high + low)//2
    steps += 1
    if current_savings > portion_down_payment:
        break
    if current_savings > portion_down_payment:
     print('It is not possible to pay the down payment in three years.')
    else:
     print('Best savings rate:', rate)
     print('Steps in bisection search:', steps)
