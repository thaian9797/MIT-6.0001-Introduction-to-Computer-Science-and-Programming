# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
annual_salary= float(input('Enter your annual salary: '))
portion_saved= float(input('Enter the percnet of your salary to save, as a decimal: '))
total_cost= float(input('Enter the cost of your dream home: '))
semi_annual_raise= float(input('Enter the semi-annual raise, as a decimal: '))

portion_down_payment =0.25
annual_return= 0.04
monthly_salary =annual_salary/12
current_savings=0

down_payment=portion_down_payment*total_cost
month =0

while current_savings<down_payment:
    current_savings+=current_savings*annual_return/12+monthly_salary*portion_saved
    if month>0 and month%6==0:
        annual_salary *= (1+semi_annual_raise)
        monthly_salary = annual_salary/12
    month+=1
   
    
    
print('Number of month:',month)
