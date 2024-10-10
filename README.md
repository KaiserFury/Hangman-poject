```markdown
# Friend Name Guessing Game

This is a simple terminal-based name guessing game, inspired by the classic "Hangman" game. The objective is to guess the letters in a randomly selected friend's name before running out of chances. Each wrong guess brings you closer to losing!

## Features
- The game randomly selects a name from a predefined list of friend names.
- Players must guess the letters in the name, with each correct guess revealing the letter.
- You have 6 chances (lives) to guess the correct letters before you lose.
- The game provides visual feedback of the stages of a "hangman" with each incorrect guess.
  
## How to Play
1. The game selects a random name from the list.
2. You are prompted to guess a letter.
3. If you guess a correct letter, it will appear in its correct position in the name.
4. If you guess an incorrect letter, you lose a life, and the hangman drawing progresses closer to completion.
5. The game continues until:
   - You guess all the letters correctly, in which case you win.
   - You run out of lives, and the hangman is fully drawn, in which case you lose.

## How to Run

To play the game, follow these steps:

1. Ensure you have Python installed on your system.
2. Download or clone the repository.
3. Run the `guessing_game.py` script in your terminal:
   ```bash
   python guessing_game.py
   ```

## Dependencies
This game uses the `os` module to clear the terminal screen after each guess. It works on both Windows and Unix-based systems (Linux, MacOS).

## Game Structure

### `clear()`
Clears the terminal screen between each round for better readability.

### `stages`
An array of ASCII art representing the stages of the hangman drawing. Each wrong guess shows the next stage, giving the player visual feedback.

### `name`
A predefined list of names (friends' names) from which the game randomly selects one for the player to guess.

## Example Gameplay
```bash
Welcome to the Friend Name Guessing Game.
You have to enter the letter which is in your friend's name.

Enter the letter: a
_ a _ _ _

You guessed a.

Enter the letter: e
Your guessed e, that's not in the word. You lose a life.

  +---+
  |   |
  O   |
      |
      |
      |
=========

Enter the letter: p
_ a _ _ p

You guessed p.
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Let me know if you'd like to make any modifications or if you need more details!
