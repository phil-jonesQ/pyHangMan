
import re
import pygame
import random
from HangManModules import *

# Global Variables
WindowWidth = 800
WindowHeight = 600
x_POS = WindowWidth / 2
y_POS = WindowHeight / 2

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
LIGHT_GREEN = (101, 152, 101)
GREY = (128,128,128)

# Load images
BG = pygame.transform.scale(pygame.image.load("Assets/background.jpeg"), (800, 600))
gallows_base = pygame.transform.scale(pygame.image.load("Assets/Gallows_base.png"), (200, 30))
gallows_post = pygame.transform.scale(pygame.image.load("Assets/Gallows_post.png"), (30, 300))
gallows_top = pygame.transform.scale(pygame.image.load("Assets/Gallows_top.png"), (200, 30))
gallows_skew = pygame.transform.scale(pygame.image.load("Assets/Gallows_skew.png"), (30, 30))
rope = pygame.transform.scale(pygame.image.load("Assets/rope.png"), (5, 30))
head = pygame.transform.scale(pygame.image.load("Assets/head.png"), (40, 40))
body = pygame.transform.scale(pygame.image.load("Assets/body.png"), (5, 50))
arm_left = pygame.transform.scale(pygame.image.load("Assets/arm_left.png"), (30, 30))
arm_right = pygame.transform.scale(pygame.image.load("Assets/arm_right.png"), (30, 30))
leg_left = pygame.transform.scale(pygame.image.load("Assets/leg_left.png"), (30, 30))
leg_right = pygame.transform.scale(pygame.image.load("Assets/leg_right.png"), (30, 30))
head_dead = pygame.transform.scale(pygame.image.load("Assets/head_dead.png"), (40, 40))

# Categories is a dictionary where we can change the status depending on the selection this is global because
# it the default declaration and is over-ridden after game over or won scenario
category = {"Animals": "ON", "Names": "OFF"}

# Char to hide letters
hide_char = "*"

# Lives is a constant
lives = 11

# Use the pygame clock so we can set the frame rate of the game
clock = pygame.time.Clock()


def main():
    pygame.init()
    # Create the Window
    hangmanwindow = pygame.display.set_mode((WindowWidth, WindowHeight))
    pygame.display.set_caption("Hangman V1.0")

    # Create an empty list so we can track guessed letters
    guessed_letters = []

    # Get word based on the default "ON" category
    for cat_status in category:
        if cat_status == "Animals" and category.get(cat_status) == "ON":
            word = rand_word_animals()
        if cat_status == "Names" and category.get(cat_status) == "ON":
            word = rand_words_names()

    # Ensure any words imported from any lists are made to upper case
    my_word = word.upper()

    # Calculate the length of the word
    word_length = len(my_word)

    # Game loop and control booleans / counters
    loop = True
    game_over = False
    guess_count = 0

    # Track each key event with a boolean, to disable keys and avoid multiple inputs
    a = True
    b = True
    c = True
    d = True
    e = True
    f = True
    g = True
    h = True
    i = True
    j = True
    k = True
    l = True
    m = True
    n = True
    o = True
    p = True
    q = True
    r = True
    s = True
    t = True
    u = True
    v = True
    w = True
    x = True
    y = True
    z = True

    # Generate Starred out Word
    my_display_word = (hide_char * word_length)

    # Initialise fonts we will use
    font = pygame.font.SysFont('Arial', 50, False, False)

    # Start main game loop
    while loop:

        # Draw background image
        hangmanwindow.blit(BG, [0, 0])

        # Game "grid" system padding
        pad = 35
        letter_pad = 0

        # Show user the category
        y_pos = 0
        for name in category:
            my_status = category.get(name)
            if my_status == "ON" and game_over:
                text = font.render(name, True, GREEN)
            if my_status == "ON" and not game_over:
                text = font.render(name, True, LIGHT_GREEN)
            if my_status == "OFF":
                text = font.render(name, True, GREY)
            hangmanwindow.blit(text, [WindowWidth - 200, y_pos])
            y_pos += 45

        # Draw Blanks
        for letter in range(word_length):
            text = font.render(my_display_word[letter], True, BLACK)
            offset = letter + 1
            hangmanwindow.blit(text, [x_POS + (offset * pad), y_POS])

        # Display guessed letters
        for letterDisplay in guessed_letters:
            text = font.render(letterDisplay, True, RED)
            hangmanwindow.blit(text, [0 + letter_pad, 0])
            letter_pad = letter_pad + pad

        # Display Word based on guesses
        for myGuess in guessed_letters:
            for m in re.finditer(myGuess, my_word):
                my_index = m.end()
                # Erase out the *
                text = font.render(my_display_word[my_index - 1], True, WHITE)
                hangmanwindow.blit(text, [x_POS + (my_index * pad), y_POS])
                # Draw in the correct indexed letters
                text = font.render(my_word[my_index - 1], True, BLUE)
                hangmanwindow.blit(text, [x_POS + (my_index * pad), y_POS])

        # Check if the guess was good or bad - we have two counters, one for correct gusses (don't include duplicate
        # letters) and one for the real amount of correct letter guesses
        correct_guess_count2 = 0
        for letter in my_word:
            correct_guess_count = 0
            for myGuess in guessed_letters:
                count = my_word.count(myGuess)
                if count >= 1:
                    correct_guess_count += 1
                if letter == myGuess:
                    correct_guess_count2 += 1

        # Check if we have won the game
        if correct_guess_count2 == word_length:
            game_over = True
            text = font.render("YOU GOT IT!!!", True, GREEN)
            hangmanwindow.blit(text, [100, 100])
            text = font.render("SPACE to play AGAIN!!", True, BLUE)
            hangmanwindow.blit(text, [100, 150])

        # Took me a while to figure this out but bad guesses are calculated by this simple maths
        bad_guess_count = guess_count - correct_guess_count
        # Render graphics depending on bad guesses
        if bad_guess_count < 0:
            bad_guess_count = 0
        if bad_guess_count >= 1:
            hangmanwindow.blit(gallows_base, [40, WindowHeight - 80])
        if bad_guess_count >= 2:
            hangmanwindow.blit(gallows_post, [60, WindowHeight - 360])
        if bad_guess_count >= 3:
            hangmanwindow.blit(gallows_top, [60, WindowHeight - 360])
        if bad_guess_count >= 4:
            hangmanwindow.blit(gallows_skew, [80, WindowHeight - 330])
        if bad_guess_count >= 5:
            hangmanwindow.blit(rope, [195, WindowHeight - 330])
        if bad_guess_count >= 6:
            hangmanwindow.blit(head, [177, WindowHeight - 310])
        if bad_guess_count >= 7:
            hangmanwindow.blit(body, [195, WindowHeight - 270])
        if bad_guess_count >= 8:
            hangmanwindow.blit(arm_left, [167, WindowHeight - 280])
        if bad_guess_count >= 9:
            hangmanwindow.blit(arm_right, [197, WindowHeight - 280])
        if bad_guess_count >= 10:
            hangmanwindow.blit(leg_left, [167, WindowHeight - 222])
        if bad_guess_count >= 11:
            hangmanwindow.blit(leg_right, [197, WindowHeight - 222])
            hangmanwindow.blit(head_dead, [177, WindowHeight - 310])

        # Check if we have lost
        if bad_guess_count >= lives:
            game_over = True
            text = font.render("The word was " + my_word, True, RED)
            hangmanwindow.blit(text, [100, 100])
            text = font.render("SPACE to play AGAIN!!", True, BLUE)
            hangmanwindow.blit(text, [100, 150])

        # Update the screen
        pygame.display.flip()

        # Keep frame rate at 60 - clearly not needed for this type of game
        clock.tick(60)
        # Handle user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                pygame.quit()
            # Handle Category selection
            if event.type == pygame.KEYDOWN and game_over:
                if event.key == pygame.K_DOWN:
                    category.update({"Animals": "OFF", "Names": "ON"})
                if event.key == pygame.K_UP:
                    category.update({"Animals": "ON", "Names": "OFF"})

            # Is game over?
            if event.type == pygame.KEYDOWN and game_over:
                if event.key == pygame.K_SPACE:
                    main()
            # Don't react to letter keys if the game is over
            if event.type == pygame.KEYDOWN and not game_over:
                if event.key == pygame.K_a and a:
                    # Increment guess count
                    guess_count += 1
                    # Disable this guess
                    a = False
                    # Add the guessed letter to our guesses list
                    guessed_letters.append("A")
                if event.key == pygame.K_b and b:
                    guess_count += 1
                    b = False
                    guessed_letters.append("B")
                if event.key == pygame.K_c and c:
                    guess_count += 1
                    c = False
                    guessed_letters.append("C")
                if event.key == pygame.K_d and d:
                    guess_count += 1
                    d = False
                    guessed_letters.append("D")
                if event.key == pygame.K_e and e:
                    guess_count += 1
                    e = False
                    guessed_letters.append("E")
                if event.key == pygame.K_f and f:
                    guess_count += 1
                    f = False
                    guessed_letters.append("F")
                if event.key == pygame.K_g and g:
                    guess_count += 1
                    g = False
                    guessed_letters.append("G")
                if event.key == pygame.K_h and h:
                    guess_count += 1
                    h = False
                    guessed_letters.append("H")
                if event.key == pygame.K_i and i:
                    guess_count += 1
                    i = False
                    guessed_letters.append("I")
                if event.key == pygame.K_j and j:
                    guess_count += 1
                    j = False
                    guessed_letters.append("J")
                if event.key == pygame.K_k and k:
                    guess_count += 1
                    k = False
                    guessed_letters.append("K")
                if event.key == pygame.K_l and l:
                    guess_count += 1
                    l = False
                    guessed_letters.append("L")
                if event.key == pygame.K_m and m:
                    guess_count += 1
                    m = False
                    guessed_letters.append("M")
                if event.key == pygame.K_n and n:
                    guess_count += 1
                    n = False
                    guessed_letters.append("N")
                if event.key == pygame.K_o and o:
                    guess_count += 1
                    o = False
                    guessed_letters.append("O")
                if event.key == pygame.K_p and p:
                    guess_count += 1
                    p = False
                    guessed_letters.append("P")
                if event.key == pygame.K_q and q:
                    guess_count += 1
                    q = False
                    guessed_letters.append("Q")
                if event.key == pygame.K_r and r:
                    guess_count += 1
                    r = False
                    guessed_letters.append("R")
                if event.key == pygame.K_s and s:
                    guess_count += 1
                    s = False
                    guessed_letters.append("S")
                if event.key == pygame.K_t and t:
                    guess_count += 1
                    t = False
                    guessed_letters.append("T")
                if event.key == pygame.K_u and u:
                    guess_count += 1
                    u = False
                    guessed_letters.append("U")
                if event.key == pygame.K_v and v:
                    guess_count += 1
                    v = False
                    guessed_letters.append("V")
                if event.key == pygame.K_w and w:
                    guess_count += 1
                    w = False
                    guessed_letters.append("W")
                if event.key == pygame.K_x and x:
                    guess_count += 1
                    x = False
                    guessed_letters.append("X")
                if event.key == pygame.K_y and y:
                    guess_count += 1
                    y = False
                    guessed_letters.append("Y")
                if event.key == pygame.K_z and z:
                    guess_count += 1
                    z = False
                    guessed_letters.append("Z")


# Call main
if __name__ == "__main__":
    main()
