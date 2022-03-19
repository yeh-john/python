
# This is staking calculator. 
# This calculator can calculate how much you need to stake can get your goal at your input_days.


# Question time

coin = input('What coin do you want to stake? :')

goal = input('How many '+coin+' do you want to get? :')

input_day = input('How many days do you wnat to get '+goal+coin+'? :')

apr = input("Enter staking APR (EX:53%=0.53)  :")


# Start calculate

keep_calculate = input('Do you want to continue calculate?(y/n) :')
if keep_calculate=='y':
    u_need_stake = float(goal)/float(apr)*365/int(input_day)
    print('-----')
    print('You need to stake '+str(u_need_stake)+coin)
    print('-----')
else:
    print('')
    print('done...')



