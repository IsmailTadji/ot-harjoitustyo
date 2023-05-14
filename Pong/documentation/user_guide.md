# User guide

Download the game through the latest release

## Installation

Before running the game, install the dependancies with the following command:

```
poetry install
```

Then initialise the databse with the command:

```
poetry run invoke build
```

Now the game is ready to start with the command:

```
poetry run invoke start
```

## Game controls

When running the program, you will be greeted by a main menu with 3 buttons. Clicking any of the buttons will take you to their respective windows. 

In the leaderboards, press `space` to return to the main menu

In single player, move the racket with the arrowkeys `↑` and `↓`

In two player, the other racket can be moved with `W` and `S`

When a two player game is finished, press `Enter` to return to the main menu

When a single player game is finished, you can input your name in a field to save your score, after press `Enter` to return to the main menu