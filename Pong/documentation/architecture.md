# Architecture

## Package and class diagram

![package_and_class](https://github.com/IsmailTadji/ot-harjoitustyo/blob/master/Pong/documentation/pictures/classes_packaging.png)

# Packages
logic, contains all the logic needed to run the game.
ui, contains all the drawing and ui buttons.
running, contains the game loop
repositories, contains the database fetch and add functions.

# UI

The ui folder contains draw, and menu buttons, which have been separate from the games logic and only use the [button_logic](https://github.com/IsmailTadji/ot-harjoitustyo/blob/master/Pong/src/logic/button_logic.py) for the clickability of the main menu buttons. When a button is clicked, a new ui window replaces the previous one. 

# Game logic

The game logic is seperated in its own [class](https://github.com/IsmailTadji/ot-harjoitustyo/blob/master/Pong/src/logic/pong_logic.py).

![Pong_logic](https://github.com/IsmailTadji/ot-harjoitustyo/blob/master/Pong/documentation/pictures/Pong_logic.png)
Pong class contains all the logic needed for the games functionality. It makes 2 rackets through the [Racket](https://github.com/IsmailTadji/ot-harjoitustyo/blob/master/Pong/src/logic/racket_logic.py) class and a [ball](https://github.com/IsmailTadji/ot-harjoitustyo/blob/master/Pong/src/logic/ball_logic.py) through the ball class. Movement of the rackets is handled in the Pong class, but the logic is in the Racket class. Same with the ball movement. Collision is handled in the Pong class.



