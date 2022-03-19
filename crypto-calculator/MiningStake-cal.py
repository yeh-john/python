
# note
########################################################
# まだ文章にcakeが入っているなので取り除く必要ある
#なので仮想通貨を聞くinput必要
#質問の順番を考える必要性あり
########################################################




# This is mining calculator

coin = input('What is your mining coin? :')

target = input('How much do you want to get?('+coin+") :")

apr = input("Enter staking APR 'EX:53%=0.53'  :")

mining_profit = input('How much can payout with mining system?('+coin+') :')

days = input('How many days you need mining can payout? :')
day=days


staking_amount = input('Enter first staking amount (mining profit):')




keep = input('Are you continue this calculate?(y/n) :')
if keep=='y':
    days=int(days)+int(day)
    print('--------')
    print(str(days)+' days')
    print('')

    stake_profit=float(staking_amount)*float(apr)/365*int(day)
    print('You get '+str(stake_profit)+coin+' staking profit')
    print('')

    staking_amount=float(staking_amount)+float(mining_profit)+float(stake_profit)
    print('Start staking '+str(staking_amount)+coin)
    print('--------')


while float(staking_amount)<float(target):
    days=int(days)+int(day)
    print(str(days)+' days')
    print('')

    stake_profit=float(staking_amount)*float(apr)/365*float(day)
    print('You get '+str(stake_profit)+coin+'staking profit')
    print('')

    staking_amount=float(staking_amount)+float(mining_profit)+float(stake_profit)
    print('Start staking '+str(staking_amount)+coin)
    print('--------')


#  result

print('')
print('')
print('')
print(str(days)+'days')
print('Get: '+str(staking_amount)+coin)
print('')


day_profit=float(staking_amount)/days
print('1DAY: '+str(day_profit)+coin)
print('')


