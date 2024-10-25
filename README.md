# Wordle_clone

A Python-based Wordle clone created using **Pygame** and **NLTK**. This game replicates the classic word-guessing experience where players have six attempts to guess a hidden five-letter word. Each guess provides feedback on letter accuracy to help players narrow down the solution.

## Table of Contents

- [Features](#features)
- [Gameplay Instructions](#gameplay-instructions)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Dependencies](#dependencies)
- [Future Improvements](#future-improvements)
- [Credits](#credits)

---

## Features

- **Interactive Gameplay**: Users can input their guesses and receive real-time feedback on letter accuracy.
- **Color-coded Hints**:
  - **Green**: Correct letter in the correct position.
  - **Yellow**: Correct letter but in the wrong position.
  - **Grey**: Letter is not in the word.
- **Virtual Keyboard**: Displays each letter’s feedback after each guess.
- **Replay Option**: Start a new game after completing a round.

---

## Gameplay Instructions

1. Guess the hidden five-letter word in **six tries** or fewer.
2. After each guess, the game provides color-coded hints:
   - **Green**: Letter is correct and in the correct position.
   - **Yellow**: Letter is correct but in the wrong position.
   - **Grey**: Letter is incorrect.
3. Use these hints to deduce the correct word!

---

## Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/yourusername/wordle-clone.git
   cd wordle-clone
   ```

2. **Install Python Dependencies**:
   - Ensure you have Python 3.x installed.
   - Install required packages:
     ```bash
     pip install pygame nltk
     ```

3. **Download NLTK Word Corpus**:
   - Open a Python shell and run:
     ```python
     import nltk
     nltk.download('words')
     nltk.download('wordnet')
     ```

4. **Run the Game**:
   ```bash
   python wordle_clone.py
   ```

---

## How to Play

1. **Start the game** by entering a five-letter word as your first guess.
2. **Use unique letters** in your first few guesses to quickly identify correct letters.
3. After each guess, use the feedback to refine your next guesses.
4. **Guess wisely!** You only have six tries to find the hidden word.

---

## Dependencies

- **Python**: Version 3.x
- **Pygame**: For rendering the game interface
- **NLTK (Natural Language Toolkit)**: To generate a list of meaningful five-letter words.

To install dependencies:
```bash
pip install -r requirements.txt
```

---

## Future Improvements

- **Difficulty Levels**: Option to choose from varying difficulty levels.
- **Leaderboard**: Track high scores and lowest attempts.
- **Hints**: Provide hints or the first letter after multiple incorrect guesses.
- **Multiplayer Mode**: Allow players to compete by guessing the same word in turns.

---

## Credits

- **Pygame**: For providing an accessible way to build a GUI-based game.
- **NLTK**: For enabling access to a comprehensive English word corpus.
- **Wordle**: Original game concept by Josh Wardle, published by the New York Times.
