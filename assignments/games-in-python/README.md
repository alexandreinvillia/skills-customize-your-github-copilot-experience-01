# 📘 Assignment: Games in Python

## 🎯 Objetivo

Build a simple Hangman game to practice core Python concepts such as loops, conditionals, strings, and user input. By the end, students should be able to manage game state and user interaction in a complete program.

## 📝 Tarefas

### 🛠️ Build the Core Hangman Loop

#### Description
Create the base version of Hangman where the program selects a random word and the player guesses one letter at a time.

#### Requirements
Completed program should:

- Randomly choose a word from a predefined list.
- Display the hidden word using underscores for unknown letters.
- Ask the player for a letter guess in each turn.
- Reveal correctly guessed letters in all matching positions.
- Decrease remaining attempts for incorrect guesses.

Example interaction:
```text
Word: _ _ _ _ _
Guess a letter: a
Word: _ a _ _ a
Remaining attempts: 5
```

### 🛠️ Add Win/Lose Conditions and Feedback

#### Description
Improve the game by adding clear ending conditions and student-friendly feedback messages.

#### Requirements
Completed program should:

- End the game with a win message when all letters are guessed.
- End the game with a lose message when attempts reach zero.
- Show letters already guessed to avoid repeated input confusion.
- Validate input so only a single alphabetic character is accepted.
- Display the final word at the end of the game.

Example end message:
```text
Congratulations! You guessed the word: banana
```
