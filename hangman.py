import random

words = open('word_list.txt', 'r')

random_word = random.choice(words.read().split())
lives = 7
guessed_letters = ''

def init_game():
    print('')
    print('*                                         *')
    print('--          Welcome to HangMan           --')
    print('*                                         *')
    print('')
    print("Guess a word or Die!")
    print("")



def draw_hangman():
    if lives == 7:
        print("   +------+")
        print("    |    |")
        print("    |")
        print("    |")
        print("    |")
        print("  =====  ")
    elif lives == 6:
        print("   +------+")
        print("    |    |")
        print("    |    O")
        print("    |")
        print("    |")
        print("  =====  ")
    elif lives == 5:
        print("   +------+")
        print("    |    |")
        print("    |    O")
        print("    |    |")
        print("    |")
        print("  =====  ")
    elif lives == 4:
        print("   +------+")
        print("    |    |")
        print("    |    O")
        print("        /|")
        print("    |")
        print("  =====  ")
    elif lives == 3:
        print("   +------+")
        print("    |    |")
        print("    |    O")
        print("        /|\\")
        print("    |")
        print("  =====  ")
    elif lives == 2:
        print("   +------+")
        print("    |    |")
        print("    |    O")
        print("        /|\\")
        print("    |   /")
        print("  =====  ")
    elif lives == 1:
        print("   +------+")
        print("    |    |")
        print("    |    O")
        print("        /|\\")
        print("    |   / \\")
        print("  =====  ")


init_game()

while lives > 0:
    rounds = 0
    draw_hangman()
    print("")

    for char in random_word:
        if char in guessed_letters:
            print(char, end="")
        else:
            print("_", end="")
            rounds += 1
        
    if rounds == 0:
        print("")
        print("")
        print("")
        print("YOU GUESS IT!!")
        break

    print("")
    print("")
    while True:
        guess = str(input("Enter a letter: "))
        if len(guess) > 1:
            print("Enter only one word!")
        else:
            break
    print("")
    guessed_letters += guess
 
    if guess not in random_word:
        lives -= 1
    if lives == 0:
        print("YOU LOSE!")
        print("The word was: " + random_word)