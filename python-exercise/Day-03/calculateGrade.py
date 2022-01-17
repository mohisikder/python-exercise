from audioop import avg


print('Enter your marks:')
sub1 = int(input('Enter your Math mark: '))
sub2 = int(input('Enter your Bangla mark: '))
sub3 = int(input('Enter your English mark: '))
sub4 = int(input('Enter your Islam mark: '))
sub5 = int(input('Enter your Others mark: '))

avg = (sub1 + sub2 + sub3 + sub4 + sub5)/5

if avg >= 90:
    print('Grade: A')
elif avg >= 80:
    print('Grade: B')
elif avg >= 70:
    print('Grade: C')
elif avg >= 60:
    print('Grade: D')
else:
    print('Grade: F')
