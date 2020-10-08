amount=int(input('Enter amount '))
if amount> 2000:
    discount = amount*0.20
    amount= amount-discount
elif amount > 1000:
    discount= amount*0.10
    amount= amount- discount
else:
    discount= amount*0.05
    amount=amount-discount
print (amount)
