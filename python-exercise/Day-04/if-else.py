n = int(input('Enter your Number: '))

if n%2:
    print('Weird')
elif n % 2 and (n>= 2 and n <6):
    print('Not Weird')
elif n % 2 and (n>= 6 and n <20):
    print('Weird')
else:
    print('Not Weird')