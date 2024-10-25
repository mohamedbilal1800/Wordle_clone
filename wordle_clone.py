import pygame
import random
import sys
from nltk_words import meaningful_five_letter_words
from collections import Counter

pygame.init()

WIDTH, HEIGHT = 633, 780

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND = pygame.image.load("assets/Starting Tiles (2).png")
BACKGROUND_RECT = BACKGROUND.get_rect(center=(317, 270))
ICON = pygame.image.load("assets/Icon.png")
pygame.display.set_caption("Wordle!")
pygame.display.set_icon(ICON)

GREEN = "#6aaa64"
YELLOW = "#c9b458"
GREY = "#787c7e"
OUTLINE = "#d3d6da"
FILLED_OUTLINE = "#878a8c"

CORRECT_WORD = "coder"
# CORRECT_WORD = random.choice(meaningful_five_letter_words)

ALPHABET = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]

GUESSED_LETTER_FONT = pygame.font.Font("assets/FreeSansBold.otf", 40)
AVAILABLE_LETTER_FONT = pygame.font.Font("assets/FreeSansBold.otf", 25)

SCREEN.fill("white")
SCREEN.blit(BACKGROUND, BACKGROUND_RECT)
pygame.display.update()

LETTER_X_SPACING = 74
LETTER_Y_SPACING = 6
LETTER_SIZE = 65

guesses_count = 0

guesses = [[]]*6

current_guess = []
current_guess_string = ""
current_letter_bg_x = 135
current_letter_bg_y = 18
indicators = []

game_result = ""

class Letter:
    def __init__(self, text, bg_position):
        self.bg_color = "white"
        self.text_color = "black"
        self.bg_position = bg_position
        self.bg_x = self.bg_position[0]
        self.bg_y = self.bg_position[1]
        self.bg_rect = (self.bg_x, self.bg_y, LETTER_SIZE, LETTER_SIZE)
        self.text = text
        self.text_position = (self.bg_x+36, self.bg_y+34)
        self.text_surface = GUESSED_LETTER_FONT.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.text_position)


    def draw(self):
        # Puts the letter and text on the screen at the desired positions.
        pygame.draw.rect(SCREEN, self.bg_color, self.bg_rect)
        if self.bg_color == "white":
            pygame.draw.rect(SCREEN, FILLED_OUTLINE, self.bg_rect, 3)
        self.text_surface = GUESSED_LETTER_FONT.render(self.text, True, self.text_color)
        SCREEN.blit(self.text_surface, self.text_rect)
        pygame.display.update()

    def delete(self):
        # Fills the letter's spot with the default square, emptying it.
        pygame.draw.rect(SCREEN, "white", self.bg_rect)
        pygame.draw.rect(SCREEN, OUTLINE, self.bg_rect, 3)
        pygame.display.update()

class Indicator:
    def __init__(self, x, y, letter):
        self.x = x
        self.y = y
        self.text = letter
        self.rect = (self.x, self.y, 57, 75)
        self.bg_color = OUTLINE


    def draw(self):
        # Puts the indicator and its text in the screen at the desired position
        pygame.draw.rect(SCREEN, self.bg_color, self.rect)
        self.text_surface = AVAILABLE_LETTER_FONT.render(self.text, True, "white")
        self.text_rect = self.text_surface.get_rect(center=(self.x+27, self.y+30))
        SCREEN.blit(self.text_surface, self.text_rect)
        pygame.display.update()

indicator_x, indicator_y = 20, 530

for i in range(3):
    for letter in ALPHABET[i]:
        new_indicator = Indicator(indicator_x, indicator_y, letter)
        indicators.append(new_indicator)
        new_indicator.draw()
        indicator_x += 60
    indicator_y += 80
    if i==0:
        indicator_x = 50
    elif i==1:
        indicator_x = 105


def check_guess(guess_to_check):
    global current_guess, current_guess_string, guesses_count, current_letter_bg_x, current_letter_bg_y, game_result
    game_decided = False

    correct_word_letter_count = Counter(CORRECT_WORD)
    # Counts occurrences of each letter in the correct word

    # First pass - Marks the letters in the correct position (Green)
    for i in range(5):
        lowercase_letter = guess_to_check[i].text.lower()
        if lowercase_letter == CORRECT_WORD[i]:
            guess_to_check[i].bg_color = GREEN
            for indicator in indicators:
                if indicator.text == lowercase_letter.upper():
                    indicator.bg_color = GREEN
                    indicator.draw()
            guess_to_check[i].text_color = "white"
            correct_word_letter_count[lowercase_letter] -= 1
            # Decreases count of matched letter
            if not game_decided:
                game_result = "W"
        else:
            game_result = ""
            game_decided = True

    # Second pass - Marks the misplaced letters (Yellow) if they exist somewhere else in the correct word
    for i in range(5):
        lowercase_letter = guess_to_check[i].text.lower()
        if guess_to_check[i].bg_color != GREEN:
            # Already green letters can be skipped
            if lowercase_letter in CORRECT_WORD and correct_word_letter_count[lowercase_letter] > 0:
                guess_to_check[i].bg_color = YELLOW
                for indicator in indicators:
                    if indicator.text == lowercase_letter.upper() and indicator.bg_color != GREEN:
                        indicator.bg_color = YELLOW
                        indicator.draw()
                guess_to_check[i].text_color = "white"
                correct_word_letter_count[lowercase_letter] -= 1
                # Decreases the count of the letter for misplaced match
            else:
                guess_to_check[i].bg_color = GREY
                for indicator in indicators:
                    if indicator.text == lowercase_letter.upper() and indicator.bg_color != GREEN and indicator.bg_color != YELLOW:
                        indicator.bg_color = GREY
                        indicator.draw()
                guess_to_check[i].text_color = "white"

        # Redraws each letter with the updated background color
        guess_to_check[i].draw()

    pygame.display.update()

    # Move to the next guess
    guesses_count += 1
    current_guess = []
    current_guess_string = ""
    current_letter_bg_x = 135
    current_letter_bg_y += 88

    if guesses_count == 6 and game_result == "":
        game_result = "L"


def play_again():
    # Puts the play again text on the screen
    pygame.draw.rect(SCREEN, "white", (10, 600, 1000, 600))
    play_again_font = pygame.font.Font("assets/FreeSansBold.otf", 40)
    play_again_text = play_again_font.render("Press ENTER to Play Again!", True, "black")
    play_again_rect = play_again_text.get_rect(center=(WIDTH/2, 700))
    word_was_text = play_again_font.render(f"The Word was {CORRECT_WORD}!", True, "black")
    word_was_rect = word_was_text.get_rect(center=(WIDTH/2, 650))
    SCREEN.blit(word_was_text, word_was_rect)
    SCREEN.blit(play_again_text, play_again_rect)
    pygame.display.update()

def reset():
    # Resets all global variables to their dafault states
    global guesses_count, CORRECT_WORD, guesses, current_guess, current_guess_string, game_result, current_letter_bg_y, current_letter_bg_x
    SCREEN.fill("white")
    SCREEN.blit(BACKGROUND, BACKGROUND_RECT)
    guesses_count = 0
    CORRECT_WORD = random.choice(meaningful_five_letter_words)
    guesses = [[]] * 6
    current_guess = []
    current_guess_string = ""
    game_result = ""
    current_letter_bg_x = 135
    current_letter_bg_y = 18
    pygame.display.update()
    for indicator in indicators:
        indicator.bg_color = OUTLINE
        indicator.draw()

def create_new_letter():
    # Creates a new letter and adds it to the current guess
    global current_guess_string, current_letter_bg_x
    current_guess_string += key_pressed
    new_letter = Letter(key_pressed, (current_letter_bg_x, current_letter_bg_y))
    current_letter_bg_x += LETTER_X_SPACING
    guesses[guesses_count].append(new_letter)
    current_guess.append(new_letter)
    for guess in guesses:
        for letter in guess:
            letter.draw()

def delete_letter():
    # deletes the last letter from the current guess
    global current_guess_string, current_letter_bg_x
    guesses[guesses_count][-1].delete()
    guesses[guesses_count].pop()
    current_guess_string = current_guess_string[:-1]
    current_guess.pop()
    current_letter_bg_x -= LETTER_X_SPACING

while True:
    if game_result != "":
        play_again()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if game_result != "":
                    reset()
                else:
                    if len(current_guess_string)==5 and current_guess_string.lower() in meaningful_five_letter_words:
                        check_guess(current_guess)
            elif event.key == pygame.K_BACKSPACE:
                if len(current_guess_string)>0:
                    delete_letter()
            else:
                key_pressed = event.unicode.upper()
                if key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and key_pressed != "":
                    if len(current_guess_string)<5:
                        create_new_letter()
