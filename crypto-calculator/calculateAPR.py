
# This is APR calculator.
# This calculator can calculate APR using input_days and input_reward.


coin = input('What is your mining coin? :')

stake_amount = input('Enter saking amount :')

days = input('How many days staking '+coin+' :')

reward = input('Enter '+days+'days reward :')



keep = input('Are you continue this calculate?(y/n) :')
if keep=='y':
    day_profit = float(reward)/int(days)
    year_profit = float(day_profit)*365
    apr = float(year_profit)/float(stake_amount)
    print('APR: '+str(apr*100)+'%')


    # Calculate input_days
    
    keep2 = input('Do you want to calculate input_days profit?(y/n) :')
    if keep2=='y':
        stake_days = input('Enter staking days :')
        stake_reward = float(stake_amount)*int(apr)/365*int(stake_days)
        print('You get '+str(stake_reward)+coin+' in '+stake_days+'days')
