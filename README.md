# Dominoes 42 Game

A Python implementation of the classic Texas domino game "42" with a graphical user interface built using Pygame.

## Description

This project is a digital version of the traditional four-player domino game "42", popular in Texas and surrounding states. The game features one human player competing against three AI opponents in a trick-taking game similar to bridge or spades, but played with dominoes instead of cards.

## Game Rules

42 is played with a standard double-six domino set (28 tiles). The game consists of:

- **Bidding Phase**: Players bid on how many points they think their team can score
- **Trump Selection**: The bid winner selects a trump suit (0-6) or "no trump"
- **Trick Play**: Seven tricks are played, with players following suit when possible
- **Scoring**: Teams score points based on count dominoes (5s and 10s) won in tricks

### Key Gameplay Elements

1. **Following Suit**: Players must play a domino matching the lead suit if they have one
2. **Trump Dominoes**: Trump dominoes can win tricks even when not following suit
3. **Count Dominoes**: Certain dominoes are worth points (5 or 10)
4. **Team Play**: Players work with their partner to meet or set the bid

## Prerequisites

Before running this game, you need:

- **Python 3.x** (Python 3.7 or higher recommended)
- **Pygame library**

## Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/YourUsername/Dominoes42.git
   cd Dominoes42
   ```

2. **Install Pygame**:
   ```bash
   pip install pygame
   ```

3. **Verify the images folder**:
   Make sure the `images/` folder contains all domino tile images and trump button images.

## How to Run

1. Navigate to the project directory
2. Run the main game file:
   ```bash
   python main.py
   ```

## Project Structure

```
Dominoes42/
│
├── main.py                 # Main game loop and event handling
├── DominoTile.py          # DominoTile class definition
├── Player.py              # Player, HumanPlayer, and AIPlayer classes
├── gameLogic.py           # Game logic functions (bidding, trick calculation, etc.)
├── ScreenElements.py      # UI elements (buttons, text display)
├── images/                # Folder containing all domino and UI images
│   ├── Domino00.png
│   ├── Domino01.png
│   └── ...
└── README.md             # This file
```

## Features

- **Interactive GUI**: Click-based interface for bidding and playing dominoes
- **AI Opponents**: Three computer players with basic strategy
- **Visual Feedback**: Clear display of played tricks, scores, and game state
- **Trump Selection**: Visual buttons for selecting trump suit
- **Game State Management**: Handles all phases of the game from dealing to scoring

## Game Controls

- **Mouse Click**: Select bids, choose trump, and play dominoes
- **Visual Indicators**: Highlights valid plays during your turn

## Development Notes

This project was developed as a final project for a Python programming course. It demonstrates:

- Object-oriented programming with classes and inheritance
- Event-driven programming with Pygame
- Game state management
- AI decision-making logic
- File I/O for loading images

## Future Enhancements

Potential improvements for future versions:

- More sophisticated AI strategy
- Multiplayer network play
- Save/load game functionality
- Statistics tracking
- Difficulty levels for AI opponents
- Sound effects and music

## Author

Dianne Purves

## Acknowledgments

- Traditional 42 game rules from Texas domino players
- Pygame community for documentation and examples
- Kris Johnson, my Python class teacher

## License

This project is for educational purposes.
