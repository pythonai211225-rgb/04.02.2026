# input rating
# rating == 5 rating == 4  print('VERY GOOD')
# rating == 3 print('GOOD')
# rating == 2 print('NEEDS IMPROVEMENT')
# rating == 1 print('REALLY NEEDS IMPROVEMENT')
# else print('NOT IN RANGE')

rating = int(input('rating?'))

match rating:
    case 1:
        print('REALLY NEEDS IMPROVEMENT')
    case 2:
        print('NEEDS IMPROVEMENT')
    case 3:
        print('GOOD')
    case 4 | 5:
        print('VERY GOOD')
    case _:
        print('NOT IN RANGE')


# rating == 5 rating == 4  print('VERY GOOD')
# rating == 3
# rating == 2
# rating == 1

x = 1
if x > 80:
    print('high')
elif x > 60:
    print('medium')
elif x > 40:
    print('medium-high')
else:
    print('low')

match True:
    case _ if x > 80:
        print('high')
    case _ if x > 60:
        print('high')
    case _ if x > 40:
        print('medium-high')
    case _:
        print('low')

x = 3
y = 1
match True:
    case _ if x == y:
        print('equal')
    case _:
        print('different')


