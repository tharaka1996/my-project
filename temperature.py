T=int(input('Enter temperature value: '))
S=input('Enter Scale C/F: ')
if S=="C":
    print("Temperature in Fahrenheit:",T*9/5+32,'F')
else:
    print("Temperature in Celsius:",(T-32)*5/9,'C')

