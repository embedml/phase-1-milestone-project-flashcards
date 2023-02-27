'''
This will test your DeckReader class, once you have passed
all of these tests, you can start making your control flow
to make the flashcards useable! 
'''

from flash_cards import *

from io import StringIO

def test_reader_init():
    test_reader = DeckReader()
    assert test_reader.loaded_decks == {}


def test_reader_load_deck():
    test_reader = DeckReader()
    test_reader.load_deck("test_deck.csv")
    test_deck = Deck("test_deck.csv")
    assert test_reader.loaded_decks["test_deck"].name == "test_deck"
    pass

    
def test_reader_print_menu(capsys):
    test_reader = DeckReader()
    test_reader.load_deck("test_deck.csv")
    test_reader.print_menu()
    captured_stdout, _ = capsys.readouterr()
    output_text = captured_stdout.split("\n")
    output_text[0] == "*******************"
    output_text[2] == "test_deck"
    output_text[3] == "******************"

def test_reader_play_front_first(monkeypatch, capsys):
    # Using forloop to make sure the tests are printed somewhere. 
    test_reader = DeckReader()
    test_reader.load_deck("test_deck.csv")
    inputs = ["f\n" "\n", "\n", "\n", "\n"] # We actually want these inputs for this one
    inputs_str = StringIO(''.join(inputs))
    monkeypatch.setattr('sys.stdin', inputs_str)


    test_reader.play_front_first("test_deck")
    captured_stdout, _ = capsys.readouterr()
    output_text = captured_stdout.split("\n")
    # Search through all substrings to see if 
    # test_deck contents are being printed
    # There is probably a better way to do this but this makes the most sense in my head
    is_test1_in_text = False
    is_test2_in_text = False
    is_test3_in_text = False
    is_test4_in_text = False
    for text in output_text:
        if text.find("test1") != -1:
            test_1_index = text.find("test1")
            is_test1_in_text = True
        if text.find("test2") != -1:
            test_2_index = text.find("test2")
            is_test2_in_text = True
        if text.find("test3") != -1:
            is_test3_in_text = True
        if text.find("test4") != -1:
            is_test4_in_text = True
    assert is_test1_in_text == True, "test1 not found in print out"
    assert is_test2_in_text == True, "test2 not found in print out"
    assert is_test3_in_text == True, "test3 not found in print out"
    assert is_test4_in_text == True, "test4 not found in print out"
    # Checking order of tests, this could be merged into the above code, but I am lazy
    for index, text in enumerate(output_text): # Based on how user prints front and back, test1 and test2 may be in seperate elements or in the same element
        if text.find("test1") != -1:
            test_1_index = index
        if text.find("test2") != -1:
            test_2_index = index
    # if in seperate elements
    if test_1_index != test_2_index:
        assert test_1_index < test_2_index, "When printing your deck, your back card was seen before your front card"
        pass
    else: # They are in the same string
        index_1 = output_text[test_1_index].find("1")
        index_2 = output_text[test_1_index].find("2")
        assert index_1 < index_2, "When printing deck front first, your back card was seen before your front card"

        

def test_reader_play_back_first(monkeypatch, capsys):
    test_reader = DeckReader()
    test_reader.load_deck("test_deck.csv")
    inputs = ["f\n" "\n", "\n", "\n", "\n"] # We actually want these inputs for this one
    inputs_str = StringIO(''.join(inputs))
    monkeypatch.setattr('sys.stdin', inputs_str)
    test_reader.play_back_first("test_deck")
    captured_stdout, _ = capsys.readouterr()
    output_text = captured_stdout.split("\n")
    # Search through all substrings to see if 
    # test_deck contents are being printed
    # There is probably a better way to do this but this makes the most sense in my head
    # This could later be imporved by specifiying order of these finds
    is_test1_in_text = False
    is_test2_in_text = False
    is_test3_in_text = False
    is_test4_in_text = False
    for text in output_text:
        if text.find("test1") != -1:
            is_test1_in_text = True
        if text.find("test2") != -1:
            is_test2_in_text = True
        if text.find("test3") != -1:
            is_test3_in_text = True
        if text.find("test4") != -1:
            is_test4_in_text = True
    assert is_test1_in_text == True, "test1 not found in print out"
    assert is_test2_in_text == True, "test2 not found in print out"
    assert is_test3_in_text == True, "test3 not found in print out"
    assert is_test4_in_text == True, "test4 not found in print out"
    # Checking order of tests, this could be merged into the above code, but I am lazy
    for index, text in enumerate(output_text): # Based on how user prints front and back, test1 and test2 may be in seperate elements or in the same element
        if text.find("test1") != -1:
            test_1_index = index
        if text.find("test2") != -1:
            test_2_index = index
    # if in seperate elements
    if test_1_index != test_2_index:
        assert test_1_index > test_2_index, "When printing your deck, your back card was seen before your front card"
        pass
    else: # They are in the same string
        index_1 = output_text[test_1_index].find("1")
        index_2 = output_text[test_1_index].find("2")
        assert index_1 > index_2, "When printing deck front first, your back card was seen before your front card"


def test_reader_does_deck_exist():
    test_reader = DeckReader()
    test_reader.load_deck("test_deck.csv")
    assert test_reader.does_deck_exist("test_deck") == True, 'test_deck is loaded in but you said it is not'
    assert test_reader.does_deck_exist("adaksdjf") == False, 'Deck "adaksdjf" does not exits but you indicated it does'
    