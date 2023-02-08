'''
Make sure you pass all of these tests before you create 
the Deck and DeckReader classes.

'''

'''


DO NOT EDIT THIS FILE UNLESS TOLD TO DO SO


'''

import random

from flash_cards import *

def test_card_init():
    chars = ["abcdefgjhijklmnopqrstuvwxyz"]
    front_rand =  random.randint(0, len(chars)-1)
    back_rand = random.randint(0, len(chars)-1)
    card = Card(front=chars[front_rand], back=chars[back_rand])
    assert card.front == chars[front_rand]
    assert card.back == chars[back_rand]

