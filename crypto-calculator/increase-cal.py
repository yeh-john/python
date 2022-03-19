
# This is calculator about crypto or stock.
# This calculator can calculate how many times the crypto price incrase.


original_price = input('Enter original price :')
current_price = input('Enter current price :')


keep_cal = input('Do you want to continue to calculate?(y/n) :')

if keep_cal=='y':
    times=float(current_price)/float(original_price)
    print('----')
    print('It incrased '+str(times)+'times')
    print('----')