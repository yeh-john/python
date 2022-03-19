# This is total day profit calculator.
num = 1
ans = 0
keep = input('Do you want to continue the calculation? y/n:')
while keep =='y':
    apr = input('Enter '+str(num)+' APR(EX:15% = 0.15) :')
    amt = input('Enter '+str(num)+' amount :')
    cal = float(amt)*float(apr)
    ans = int(ans)+float(cal)/365
    num = int(num)+1
    print('')
    print('total: '+str(ans))
    keep = input('Do you want to continue the calculation? y/n:')
print(ans)
