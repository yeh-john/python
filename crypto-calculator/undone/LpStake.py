
# This calculator is to calculate how many day you need to stake LP token can get profit.

# Token names
coin1 = input('Enter first coin :')
coin2 = input('Enter second coin :')
LP_token = coin1+'-'+coin2

# Needed fees
EnableStake_fee = input('Enter enable staking fee :')
AddLiquidity_fee = input('Entet add liquidity fee :') # Create liquidity fee
# Start staking fee
# End staking fee ?????
# Remove LP token fee

# Token volume
CreateLpVolume1 = input('Enter create LPtoken using '+coin1+' token volume :')
CreateLpVolume2 = input('Enter create LPtoken using '+coin2+' token volume :')
LP_Balance = input('Enter '+LP_token+' LPtoken balance :')

# Staking info
apr = input("Enter staking APR 'EX:53%=0.53'  :")




# If in the namal calculator to calculate 1 day profit

# 1coin to twd     EX: 100000shib = 100twd
# 100twd X 2 = 200     Because LP token is 50% 50%
# 200twd X APR = YearProfit    EX: 200X20% = 40
# 40/365 = DayProfit    EX: 40/365 = 0.1 twd
# So that day profit is 0.1 twd

# If you want to calculate how many days you need to stake can get plus profit.

# NeedFees / DayProfit = NeedDays
# EX: 500/0.1=5000 
# So that you need to stake 5000days 
