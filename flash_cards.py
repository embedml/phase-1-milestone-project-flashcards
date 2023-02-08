# Using csv import below do not remove
import csv # Need this for grabbing from a csv file

#### Card Class ####
'''
Create a class called Card

Create a constructor that takes in `front` and `back` assigning
them to the attributes `front` and back`. 

This will act as our flash card! Our flash cards have both 
a front and a back. 

'''

####################


#### Deck Class ####
'''
1. Create a class called Deck

This class will be used to store many cards. It will also create
the cards from a .csv (comma separated values) file. You can 
see these files in your "Explorer Window". The two provided for
you are "python_vocab.csv" and "test_deck.csv". Please do not alter
these to files until you have submitted the project. 

2. Create a constructor that takes in a `file_name` and `name`, 
Have the constructor assign `file_name` to an attribute called 
`file_name`. Have the `name` argument be a default argument equal to None.

3. Create an attribute called `cards` that is an empty list, and an 
attribute called `name` that is equal to None.

4. In the constructor check if the `name` argument passed in is None, if
it is None, then slice the `file_name` cutting off the `.csv` and storing
it into the `name` attribute. (Hint: negative value slicing may help here!)

Otherwise just store the `name` parameter into the `name` attribute. 

5. Load the values from the csv file. For each row, create a 
`Card` object storing the first value in each row to the front 
of the card, adn second value in each row to the back of the Card. 
Once the Card is created append it to the `cards` attribute of the Deck
class. Do this for every row in the csv file. 

This is populating our Deck with cards that we can read through later!

6. Create a new method called `rename`, have it pass in a `name` and
reassign the `name` attribute to that new name.

'''


####################



#### DeckReader Class ####
''''
1. Create a class called DeckReader

This is an object that we can use to read and load our decks. 
This type of class is sometimes called a "Manager". You can think 
of it as a high level/abstraction class to make it easier to 
deal with many decks (and cards). 

This will be our main way to load decks, organize them, and read 
them. 

This class will have some IO (Input Output), so please reference the 
README file. You can always view the README file easier by clicking
on the file and pressing the "Magnifying Glass on a Page" icon in the
top right of the VS Code window.
'''



#########################

#### The main function ####
'''
This next section looks like like a lot! The goal with verbose instructions is to try to reduce 
confusion (not intimidate you). If you have any questions please reach out! 


1. Create a function called main(), have it take in no arguments

This function will be IO (Input Output) HEAVY, so please reference the 
README file. You can always view the README file easier by clicking
on the file and pressing the "Magnifying Glass on a Page" icon in the
top right of the VS Code window.

main() will also be testing you on control flow, so please reference 
any diagrams in the README to help. 

If you think your IO is correct and the test cases still seem to be failing 
please contact a TA or your instructor. Due to the nature of IO testing it is hard 
to capture every edge case, so you may be correct and the testing is wrong. (Note: make
sure you are passing all other tests as they may be correct for future tests)

2. Create a DeckReader object. This is the main object we will be calling methods from.

3. Get an input from the user asking "Please specify the deck you would like to load by typing in the file name:\n"
(Note: All input function calls should have \n at the end, this helps with grading. print() 
statements should also have \n at the end of the string)

4. Load the deck into the DeckReader Object from the file input. 

Run your program and see what it looks like

5. Make sure you are passing the test `test_io_first_deck_file`

6. Constantly get the user's input asking "Would you like to load another deck? (y/n)\n", if the result
is not "n" then get the user's input of what deck they would ike to load with the string "Please specify the deck you would like to load by typing in the file name:\n"
Then load the user specified deck into the DeckReader object. 
If the user says "n" (no), then stop asking if they would like to load another deck. 
(Hint: Look at the diagram in the README file)

Run your program and see what it looks like.

7. Make sure you are passing `test_io_loading_another_deck_no`

8. Make sure you are passing `test_io_loading_another_deck_yes`

Next we are going into our loop of printing out which decks we have loaded, asking the user
to select one to read, then asking if they would like to read the front first or the back first. Once they 
are done reading a deck, then we need to go back and print the menu and ask to print another deck. Then the cycle continues. 

The general idea:
Ask which deck they would like -> print menu -> get input -> asking front or back -> read deck -> finish reading -> Ask which deck they would like

9. Lets start with constantly printing the menu and grabbing an input. This should happen in this order:
print out "Please choose a deck to examine by typing in the deck name, or press 'q' to quit:\n", then print out the menu from the deck reader
using the .print_menu() method. Then get an input from the user while displaying "Input:\n" (in the input() function)

10. Right now since we are constantly asking for an input from the user but not using it, the user is not able to exit our program. Go ahead and check if the 
input is "q", if it is "q" then we should break out of the while loop with our "print_menu" call, causing the program to end. 

Run your program and see what it looks like. 

11. Make sure you are passing "test_io_quit"

12. Next if the input is not "q" then we want to check to see if the input was a deck we showed in the print menu. We can do this 
by calling our handy "does_deck_exist" function which returns True if it exists and false if it does not. If it does not exits then print 
out "Deck does not exist try again!\n". This should cause us to go back up to our while loop to ask the user to examine a list and 
re print the menu.

13. Make sure you are passing "test_io_deck_does_not_exist"

Run your program. What does it look like? Does the output and flow of the program make sense?

Recap: At this point, we load in a deck, then we ask if we want to load in another. If we do, we specify which one. If not then we move to a while loop 
where we ask the user to select a deck from the printed menu. If the user presses q then we exit the program. If the user 
types in a deck that does not exist we tell the user it does not exist and to try selecting another deck. 

15. Next we need to examine the deck the user selects from the menu (if it exists)! We are going to implement two methods of examining the deck
which are described below:

a. Deck can be read with the front of the cards being shown first, then the back second which we will denote as the option f. 
 - We have implemented this with the Deck.play_front_first() method.
b. Deck can be read with the back of the cards being shown first, then the front second which we will denote as the option b.
- We have implemented this with the Deck.play_back_first() method.

We want the user to either select the "f" option which plays the deck front first, or the "b" method which plays the deck back first.

If the user does not input "f" or "b" then we want to tell the user "Your input was invalid please try again\n", and then reask
"Would you like to show the front or bac first (f/b)?\n". Hint: This cyclical nature of incorrect inputs means we will need a while loop! 

If "f" or "b" is selected call the appropriate method, and break out of the while loop to go back up a level to ask the user which deck 
they would like to select and printing the menu. (Again I suggest referencing the diagram in teh README.md file)

16. Make sure you are passing "test_io_read_deck_front"

17. Make sure you are passing "test_io_read_deck_back"

18. Make sure you are passing "test_io_quit_after_loading_and_using_deck" (this should be a passive test you pass from previous implementations)

Run your program! You should now have flashcards completed and passing all tests! 

'''

###########################

def main():
    '''Control flow will be here!'''
    print("Delete this line once you start!")


if __name__ == "__main__":
   main()