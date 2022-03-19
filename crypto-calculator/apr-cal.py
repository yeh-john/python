# This is apr calculator. You can calculate your staking daily profit.

coin = input('What coin do you want to stake? :')

token_amount = input('How much do you want to stake?('+coin+') :')

apr = input("Enter staking APR 'EX 14%=0.14' :")

year_profit = float(token_amount)*float(apr)

daily_profit = float(year_profit)/365


print('----')
print('This is daily profit')
print(daily_profit)
print('----')

inputDay_calculate = input('Do you want to calculate input days profit?(y/n) :')


if inputDay_calculate=='y':
    day=input('How many days do you want to stake?('+coin+') :')
    input_day_profit=int(day)*float(daily_profit)
    print('')
    print('This is '+day+'days staking profit')
    print(input_day_profit)


print('')
wantProfit_calculate = input('Do you want to calculate how many days you need to stake get target profit?(y/n) :')



if wantProfit_calculate=='y':
    wantProfit=input('How much you want to get?('+coin+') :')
    need_days=float(wantProfit)/float(daily_profit)
    print('')
    print('You need to staking '+str(need_days)+'days')
