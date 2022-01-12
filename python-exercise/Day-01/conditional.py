userInput = input('Enter your favorit Number: ')
userInput = int(userInput)

# if userInput % 2 == 0:
#     print('The number is even')
# if userInput % 2 == 1:
#     print('The number is odd')

# if userInput % 2 == 0:
#     print('The number is even')
# else:
#     print('The number is odd')


#Multi conditional

# if userInput >=1 and userInput<= 10:
#     print('Too low')
# elif userInput >= 11 and userInput <= 20:
#     print('medium')
# elif userInput >= 21 and userInput <= 30:
#     print('large')
# else:
#     print('too large')

#Nested if

if userInput > 10:
    print('Above ten')
    if userInput > 20:
        print('and also above 20!')
    else:
        print('but not above 20.')