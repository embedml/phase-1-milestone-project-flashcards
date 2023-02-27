
from flash_cards import *
from io import StringIO

def test_io_first_deck_file(monkeypatch, capsys):
    inputs = ["python_vocab.csv\n", "n\n", "q\n"]  # Need all inputs to end of path so we dont have EOF error on stdout reading
    inputs_str = StringIO(''.join(inputs))
    monkeypatch.setattr('sys.stdin', inputs_str)
    main()
    captured_stdout, _ = capsys.readouterr()
    output_text = captured_stdout.split("\n")
    for line in output_text:
        print(line)
    assert output_text[0] == "Please specify the deck you would like to load by typing in the file name:", "Your output: " + output_text[0] + ' Expected: "Please specify the deck you would like to load by typing in the file name:" on line 0'

def test_io_loading_another_deck_no(monkeypatch, capsys):
    inputs = ["python_vocab.csv\n", "n\n", "q\n"]  # Need all inputs to end of path so we dont have EOF error on stdout reading
    inputs_str = StringIO(''.join(inputs))
    monkeypatch.setattr('sys.stdin', inputs_str)
    main()
    captured_stdout, _ = capsys.readouterr()
    output_text = captured_stdout.split("\n")
    for line in output_text:
        print(line)
    assert output_text[0] == "Please specify the deck you would like to load by typing in the file name:", "Your output: " + output_text[0] + ' Expected: "Please specify the deck you would like to load by typing in the file name:" on line 0'
    assert output_text[1] == "Would you like to load another deck? (y/n)", "Your output: " + output_text[1] + ' Expected: "Would you like to load another deck? (y/n)" on line 1'

def test_io_loading_another_deck_yes(monkeypatch, capsys):
    inputs = ["python_vocab.csv\n", "y\n", "test_deck.csv\n", "n\n", "q\n"]  # Need all inputs to end of path so we dont have EOF error on stdout reading
    inputs_str = StringIO(''.join(inputs))
    monkeypatch.setattr('sys.stdin', inputs_str)
    main()
    captured_stdout, _ = capsys.readouterr()
    output_text = captured_stdout.split("\n")
    for line in output_text:
        print(line)
    assert output_text[0] == "Please specify the deck you would like to load by typing in the file name:", "Your output: " + output_text[0] + ' Expected: "Please specify the deck you would like to load by typing in the file name:" on line 0'
    assert output_text[1] == "Would you like to load another deck? (y/n)", "Your output: " + output_text[1] + ' Expected: "Would you like to load another deck? (y/n)" on line 1'
    assert output_text[2] == "Please choose a deck to examine by typing in the deck name, or press 'q' to quit:", "Your output: " + output_text[2] + ' Expected: '+'"Please choose a deck to examine by typing in the deck name, or press '+"'q'"+' to quit: "'+'on line 2'


def test_io_quit(monkeypatch, capsys):
    inputs = ["python_vocab.csv\n", "n\n", "q\n"] # We actually want these inputs for this one
    inputs_str = StringIO(''.join(inputs))
    monkeypatch.setattr('sys.stdin', inputs_str)
    main()
    captured_stdout, _ = capsys.readouterr()
    output_text = captured_stdout.split("\n")
    for line in output_text:
        print(line)
    assert output_text[0] == "Please specify the deck you would like to load by typing in the file name:", "Your output: " + output_text[0] + ' Expected: "Please specify the deck you would like to load by typing in the file name:" on line 0'
    assert output_text[1] == "Would you like to load another deck? (y/n)", "Your output: " + output_text[1] + ' Expected: "Would you like to load another deck? (y/n)" on line 1'
    assert output_text[2] == "Please choose a deck to examine by typing in the deck name, or press 'q' to quit:", "Your output: " + output_text[2] + ' Expected: '+'"Please choose a deck to examine by typing in the deck name, or press '+"'q'"+' to quit: "'+'on line 2'
    assert output_text[5] == "python_vocab", "Your output: " + output_text[5] + ' Expected: "python_vocab" on line 5'
    assert output_text[-3] == "Exiting flash cards.", "Your output: " + output_text[-3] + ' Expected: "Exiting flash cards." on the second to last line'  # Note last two strings are blank

def test_io_deck_does_not_exist(monkeypatch, capsys):
    inputs = ["test_deck.csv\n", "n\n", "deck_abc\n", "q\n"] # We actually want these inputs for this one
    inputs_str = StringIO(''.join(inputs))
    monkeypatch.setattr('sys.stdin', inputs_str)
    main()
    captured_stdout, _ = capsys.readouterr()
    output_text = captured_stdout.split("\n")
    for line in output_text:
        print(line)
    assert output_text[0] == "Please specify the deck you would like to load by typing in the file name:", "Your output: " + output_text[0] + ' Expected: "Please specify the deck you would like to load by typing in the file name:" on line 0'
    assert output_text[1] == "Would you like to load another deck? (y/n)", "Your output: " + output_text[1] + ' Expected: "Would you like to load another deck? (y/n)" on line 1'
    assert output_text[2] == "Please choose a deck to examine by typing in the deck name, or press 'q' to quit:", "Your output: " + output_text[2] + ' Expected: '+'"Please choose a deck to examine by typing in the deck name, or press '+"'q'"+' to quit: "'+'on line 2'
    assert output_text[8] == "Deck does not exist try again!", "Your output: " + output_text[8] + ' Expected: "Deck does not exist try again!" on line 8'
    assert output_text[10] == "Please choose a deck to examine by typing in the deck name, or press 'q' to quit:", "Your output: " + output_text[10] + ' Expected: '+'"Please choose a deck to examine by typing in the deck name, or press '+"'q'"+' to quit: "'+'on line 2'


def test_io_selecting_deck_from_menu(monkeypatch, capsys):
    inputs = ["test_deck.csv\n", "n\n", "test_deck\n", "f\n" "\n", "\n", "\n", "\n", "q\n"] # We actually want these inputs for this one
    inputs_str = StringIO(''.join(inputs))
    monkeypatch.setattr('sys.stdin', inputs_str)
    main()
    captured_stdout, _ = capsys.readouterr()
    output_text = captured_stdout.split("\n")
    for line in output_text:
        print(line)
    assert output_text[0] == "Please specify the deck you would like to load by typing in the file name:", "Your output: " + output_text[0] + ' Expected: "Please specify the deck you would like to load by typing in the file name:" on line 0'
    assert output_text[1] == "Would you like to load another deck? (y/n)", "Your output: " + output_text[1] + ' Expected: "Would you like to load another deck? (y/n)" on line 1'
    assert output_text[2] == "Please choose a deck to examine by typing in the deck name, or press 'q' to quit:", "Your output: " + output_text[2] + ' Expected: '+'"Please choose a deck to examine by typing in the deck name, or press '+"'q'"+' to quit: "'+'on line 2'
    assert output_text[5] == "test_deck", "Your output: " + output_text[5] + ' Expected: "test_deck" on line 5'


def test_io_read_deck_front(monkeypatch, capsys):
    inputs = ["test_deck.csv\n", "n\n", "test_deck\n", "f\n" "\n", "\n", "\n", "\n", "q\n"] # We actually want these inputs for this one
    inputs_str = StringIO(''.join(inputs))
    monkeypatch.setattr('sys.stdin', inputs_str)
    main()
    captured_stdout, _ = capsys.readouterr()
    output_text = captured_stdout.split("\n")
    for line in output_text:
        print(line)
    assert output_text[0] == "Please specify the deck you would like to load by typing in the file name:", "Your output: " + output_text[0] + ' Expected: "Please specify the deck you would like to load by typing in the file name:" on line 0'
    assert output_text[1] == "Would you like to load another deck? (y/n)", "Your output: " + output_text[1] + ' Expected: "Would you like to load another deck? (y/n)" on line 1'
    assert output_text[2] == "Please choose a deck to examine by typing in the deck name, or press 'q' to quit:", "Your output: " + output_text[2] + ' Expected: '+'"Please choose a deck to examine by typing in the deck name, or press '+"'q'"+' to quit: "'+'on line 2'
    assert output_text[5] == "test_deck", "Your output: " + output_text[5] + ' Expected: "test_deck" on line 5'
    test_1_index = None
    test_2_index = None
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


def test_io_read_deck_back(monkeypatch, capsys):
    inputs = ["test_deck.csv\n", "n\n", "test_deck\n", "b\n" "\n", "\n", "\n", "\n", "q\n"] # We actually want these inputs for this one
    inputs_str = StringIO(''.join(inputs))
    monkeypatch.setattr('sys.stdin', inputs_str)
    main()
    captured_stdout, _ = capsys.readouterr()
    output_text = captured_stdout.split("\n")
    for line in output_text:
        print(line)
    assert output_text[0] == "Please specify the deck you would like to load by typing in the file name:", "Your output: " + output_text[0] + ' Expected: "Please specify the deck you would like to load by typing in the file name:" on line 0'
    assert output_text[1] == "Would you like to load another deck? (y/n)", "Your output: " + output_text[1] + ' Expected: "Would you like to load another deck? (y/n)" on line 1'
    assert output_text[2] == "Please choose a deck to examine by typing in the deck name, or press 'q' to quit:", "Your output: " + output_text[2] + ' Expected: '+'"Please choose a deck to examine by typing in the deck name, or press '+"'q'"+' to quit: "'+'on line 2'
    assert output_text[5] == "test_deck", "Your output: " + output_text[5] + ' Expected: "test_deck" on line 5'
    test_1_index = None
    test_2_index = None
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
        index_2 = output_text[test_2_index].find("2")
        assert index_1 > index_2, "When printing deck front first, your back card was seen before your front card"


def test_io_quit_after_loading_and_using_deck(monkeypatch, capsys):
    inputs = ["test_deck.csv\n", "n\n", "test_deck\n", "f\n" "\n", "\n", "\n", "\n", "q\n"] # We actually want these inputs for this one
    inputs_str = StringIO(''.join(inputs))
    monkeypatch.setattr('sys.stdin', inputs_str)
    main()
    captured_stdout, _ = capsys.readouterr()
    output_text = captured_stdout.split("\n")
    for line in output_text:
        print(line)
    assert output_text[0] == "Please specify the deck you would like to load by typing in the file name:", "\nYour output: " + f'"{output_text[0]}"' + ' \n\n   Expected: "Please specify the deck you would like to load by typing in the file name:" stdout line 0\n\n'
    assert output_text[1] == "Would you like to load another deck? (y/n)", "Your output: " + output_text[1] + ' Expected: "Would you like to load another deck? (y/n)" on line 1'
    assert output_text[2] == "Please choose a deck to examine by typing in the deck name, or press 'q' to quit:", "Your output: " + output_text[2] + ' Expected: '+'"Please choose a deck to examine by typing in the deck name, or press '+"'q'"+' to quit: "'+'on line 2'
    assert output_text[5] == "test_deck", "Your output: " + output_text[5] + ' Expected: "test_deck" on line 5'
    is_test4_in_text = False
    for text in output_text:
        if text.find("test4") != -1:
            is_test4_in_text = True
    assert is_test4_in_text == True, "test4 not found in print out"
    assert output_text[-4] == "*"*20, "Your output: "+ output_text[-4] + ' Expected: "********************" on the fourth to last line' # Make sure it still prints menu when they are done flipping through deck"
    assert output_text[-3] == "Exiting flash cards.", "Your output: " + output_text[-3] + ' Expected: "Exiting flash cards." on the second to last line'  # Note last two strings are blank



