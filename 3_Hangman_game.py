##hangman project
import random

# Hangman stages as comments (6 tries total)
stages = ['''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========
''', '''
#   +---+
#   |   |
#   O   |
#  /|\\  |      # ← Use double backslash to show \ properly
#       |
#       |
# =========
''', '''
#   +---+
#   |   |
#   O   |
#  /|\\  |
#  /    |
#       |
# =========
''', '''
   +---+
   |   |
   O   |
  /|\\  |
  / \\  |
       |
 =========
''']

# Word list
word_list = ["tanish", "tejas", "prince"]

# Game setup
lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)  # For testing only

# Placeholder for blanks
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# Game state
game_over = False
correct_letters = []

# Start game loop
while not game_over:

    # Get letter input from user
    guess = input("guess a letter: ").lower()

    # Create new display after the guess
    display = ""
    for letter in chosen_word:
        if letter == guess:
            correct_letters.append(guess)
            display += letter
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    # If guess is wrong, reduce a life
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("you lose!!")
            print("The word was:", chosen_word)

    # If no underscore left, player wins
    if "_" not in display:
        game_over = True
        print("you win!!!")

    # ✅ FIX: Print stage using 6 - lives to match index
    print(stages[6 - lives])
