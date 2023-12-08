# comp1510-term-game-project

## Your name:
Caroline Su

## Your student number:
A01369603

## Your GitHub ID:
Juntingg

## Any important comments you'd like to make about your work:
First time building a game in python. Excited!

# Text-Based Adventure Game

This text-based adventure game simulates an explorer navigating through a forest, leveling up, and eventually confronting a dragon at the dark castle. Players input directions (S, W, N, E) to control the character.

## How to Play

1. Run the `game()` function from the main file.
2. The game introduces the player to the forest, generates a character, and creates a game board.
3. Players input directions to navigate through the forest.

## Game Mechanics

| Mechanic               | Description                                                                            |
|------------------------|----------------------------------------------------------------------------------------|
| **Character Movement** | Use valid directional inputs (S, W, N, E) to move the character.                       |
| **More Instruction**   | Enter "help", "state" or "hint" to see more information if you need to.                |
| **Events**             | Various random events occur based on character movements.                              |
| **Battles**            | Character will encounter battle in a random chance.                                    |
| **Upgrades**           | Character level upgrades happen when getting more EX.                                  |
| **Objectives**         | Players need to reach level 3, find a key, and confront the dragon at the dark castle. |

## Game Progression

- Character enter the forest and explore around and trigger random events.
- Character upgrade his level by trigger different events and defeat enemies.
- Character will drop into a hole which is created randomly and find the key in it.
- Until character reach level 3 and get the key, user will go to the castle and defeat the dragon.
- During the process, if character dies before defeat the dragon, users lose the game.

## Game Loop Functionality

| Functionality                      | Description                                                                                                                                                                   |
|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Game Initialization**            | Introduces the game, generates a character, and creates a game board.                                                                                                           |
| **Character Movement**             | Validates character movements and triggers various in-game events.                                                                                                               |
| **Upgrades and Events**            | Manages character upgrades, battles, and random events.                                                                                                                           |
| **Objectives and Reminders**       | Provides reminders and updates on game objectives.                                                                                                                                |
| **Boss Fight**                     | Initiates a boss fight upon reaching the dark castle.                                                                                                                             |

