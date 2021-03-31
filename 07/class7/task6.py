def read_cards(filename):
    with open(filename) as fp:
        content = fp.read()
    return content
def can_be_card_number(user_input):
    if not len(user_input) in [13, 15, 16]:
        return False

    if not user_input.isdigit():
        return False

    return True

def is_visa(card_number):
    if card_number[0] == '4' and len(card_number) in [13, 16]:
        return True
    else:
        return False

def is_mastercard(card_number):
    # numbers 51 through 55 or with the numbers 2221 through 2720. All have 16 digits.
    if (51 <= int(card_number[0:2]) <= 55 or 2221 <= int(card_number[0:4]) <= 2720) and len(card_number) == 16:
        return True
    else:
        return False

def is_american_express(card_number):
    if card_number[0:2] in ['34', '37'] and len(card_number) == 15:
        return True
    else:
        return False

#main code


cards_list = read_cards("cards.txt")
for card in cards_list
if can_be_card_number(cards):

    if is_visa(cards):
        print('Visa card')
    elif is_mastercard(cards):
        print('MasterCard')
    elif is_american_express(cards):
        print('American Express')
    else:
        print('Inna karta')
else:
    print('This input is not a card number')