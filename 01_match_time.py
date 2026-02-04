import random

computer_score = 0
player_score = 0

while True:
    # '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'
    #  2    3   ..                             10    11  12   13   14
    computer_card_number = random.randint(2, 14)
    computer_card_suit = random.choice(["❤️", "♦️", "♣️", "♠️"])

    print('COMPUTER: ', end="")

    match computer_card_number:
        case 14:
            # if computer_card_number == 14
            display_number = 'A'
        case 13:
            # elif computer_card_number == 13 ...
            display_number = 'K'
        case 12:
            display_number = 'Q'
        case 11:
            display_number = 'J'
        case _:  # else
            display_number = computer_card_number

    print(display_number, computer_card_suit)

    # input rating
    # rating == 5 rating == 4  print('VERY GOOD')
    # rating == 3 print('GOOD')
    # rating == 2 print('NEEDS IMPROVEMENT')
    # rating == 1 print('REALLY NEEDS IMPROVEMENT')
    # else print('NOT IN RANGE')


    player_card_number = random.randint(2, 14)
    player_card_suit = random.choice(["❤️", "♦️", "♣️", "♠️"])

    print('PLAYER: ', end="")

    match player_card_number:
        case 14:
            display_number = 'A'
        case 13:
            display_number = 'K'
        case 12:
            display_number = 'Q'
        case 11:
            display_number = 'J'
        case _:
            display_number = player_card_number

    print(display_number, player_card_suit)

    if player_card_number > computer_card_number:
        player_score += 1
        print('PLAYER WON!')
    elif player_card_number < computer_card_number:
        computer_score +=1
        print('COMPUTER WON!')
    else:
        print('DRAW')

    print('SCORE:')
    print('PLAYER', player_score, 'COMPUTER', computer_score)
    print('*' * 40)

    if computer_score >= 10 or player_score >= 10:
        break