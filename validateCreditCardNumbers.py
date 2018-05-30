def validate_num(ccnum):
    """
    Apply the Luhn Algorithm against a card number to verify its validity
    Returns True or False
    """
    ccnum = str(ccnum)

    # split the cc number into 2 strings
    ccnum_double = ccnum[-2::-2]
    ccnum_single = ccnum[-1::-2]

    # multiply each digit in double string by 2 and join them together in a single string
    ccnum_double = "".join([str(int(x) * 2) for x in ccnum_double])

    # add all the digits together
    mysum = sum(map(int, ccnum_double)) + sum(map(int, ccnum_single))

    # check that sum is evenly divisible by 10
    if mysum % 10 == 0:
        return True
    else:
        return False


def get_valid_cards():
    """
    specify the valid parameters for each card type
    Returns a Dictionary of Dictionaries sorted by card-number length,
    card type, card-validation parameters
    """
    valid_cards = {'fifteen':
                       {'American Express':
                            {'valid_prefixes': list(map(str,[34,37])),
                             'start' : 0,
                             'end' : 2
                            }
                       }, # fifteen
                  'sixteen':
                       {'Discover':
                            {'valid_prefixes': list(map(str,[6011])),
                             'start' : 0,
                             'end' : 4
                            },
                        'Master Card':
                            {'valid_prefixes': list(map(str,range(51,56))),
                             'start' : 0,
                             'end' : 2
                            },
                        'Visa':
                            {'valid_prefixes': list(map(str,[4])),
                             'start' : 0,
                             'end' : 1
                            }
                       } # sixteen
                  }
    return valid_cards


def validate_length(ccnum):
    """
    validate that the card number is a valid length
    """
    ccnum_str = str(ccnum)
    if len(str(ccnum_str)) == 15:
        return 'fifteen'

    elif len(str(ccnum_str)) == 16:
        return 'sixteen'

    else:
        return None


def validate_card(ccnum):
    """
    check a credit card number and return the type of card if the number is valid
    """
    ccnum_str = str(ccnum)

    # get valid card data
    valid_cards = get_valid_cards()

    # set default return value
    result = "Invalid Number"

    # check for valid length
    length = validate_length(ccnum)

    # if length is valid, loop through cards of that length
    if length:
        for card in valid_cards[length]:
            # set start and end parameters to be searched
            start = valid_cards[length][card]['start']
            end = valid_cards[length][card]['end']

            # check for card type
            if ccnum_str[start:end] in valid_cards[length][card]['valid_prefixes']:

                # validate card number
                if validate_num(ccnum):
                    result = card

    return result


#Enter your card numbers here
ccnums = ['<card1>',
          '<card2>',
          '<card3>',
          'etc'
         ]

# loop through card numbers and validate
for ccnum in ccnums:
    print("{:<16}\t{}".format(ccnum, validate_card(ccnum)))



