# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

semi_annual_raise =0.07
annual_return=0.04
total_cost=1000000
portion_down_payment=0.25
down_payment=portion_down_payment*total_cost
current_savings=0
annual_salary= float(input('Enter the starting salary: '))

low=0
high=10000
epsilon =100
guess=(low+high)/2
guess_rate=guess/10000
bisection_step=0

def savings(current_savings,annual_salary,guess_rate):
    month=0
    while month<36:
        current_savings+=current_savings*annual_return/12 +annual_salary/12*guess_rate
        if month>0 and month%6==0:
            annual_salary +=annual_salary*semi_annual_raise
        month +=1
    return current_savings

if savings(0,annual_salary,1)<down_payment:
    print('It is not possible to pay the down payment in three years')
else:
    current_savings=savings(0,annual_salary,guess_rate)
    while abs(current_savings-down_payment)>=epsilon and current_savings<1.5*down_payment:
        if current_savings<=down_payment:
            low=guess
            bisection_step +=1
        else:
            high=guess
            bisection_step +=1
        guess=(low+high)/2
        guess_rate=guess/10000
        current_savings=savings(0,annual_salary,guess_rate)
    print('Best saving rate:',guess_rate)
    print('Step in bisection',bisection_step)
            
    
    
