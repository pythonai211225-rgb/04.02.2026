import random

computer_score = 0
player_score = 0

while True:
    # '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'
    #  2    3   ..                             10    11  12   13   14
    computer_card_number = random.randint(2, 14)
    computer_card_suit = random.choice(["❤️", "♦️", "♣️", "♠️"])

    print('COMPUTER: ', end="")
    if computer_card_number <= 10:
        display_number = computer_card_number
    elif computer_card_number == 11:
        display_number = 'J'
    elif computer_card_number == 12:
        display_number = 'Q'
    elif computer_card_number == 13:
        display_number = 'K'
    elif computer_card_number == 14:
        display_number = 'A'

    print(display_number, computer_card_suit)

    player_card_number = random.randint(2, 14)
    player_card_suit = random.choice(["❤️", "♦️", "♣️", "♠️"])

    print('PLAYER: ', end="")

    if player_card_number <= 10:
        display_number = player_card_number
    elif player_card_number == 11:
        display_number = 'J'
    elif player_card_number == 12:
        display_number = 'Q'
    elif player_card_number == 13:
        display_number = 'K'
    elif player_card_number == 14:
        display_number = 'A'

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