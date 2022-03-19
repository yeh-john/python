# This calculator is to calculate how much can get profit in exchage market. EX: dex, bitoex , bybit


# Coin info
coin = input('What coin do you buy :')
bought_price = input('Enter bought '+coin+' price :')
current_price = input('Enter current '+coin+' price :')

# Calculate change percentage
start_cal_per = input('Do you want to continue calculate?(y/n) :')
if start_cal_per=='y':
    change_amt = float(current_price)-float(bought_price)
    change_per = float(change_amt)/float(bought_price)
    percent = float(change_per)*100
    print(coin+' price change '+str(percent)+'%')

# Calculate profit
start_cal = input('Do you want to continue calculate?(y/n) :')
if start_cal=='y':
    market_coin = input('What currency do you want to use in Exchange market :')
    invest_amount = input('How much do you plan to invest :')
    profit_amt = float(invest_amount)*float(change_per)
    profit = float(invest_amount)+float(profit_amt)
    print('----')
    print('Your '+coin+' profit is '+str(profit_amt)+market_coin)
    print(str(invest_amount)+market_coin+' > '+str(profit)+market_coin)
