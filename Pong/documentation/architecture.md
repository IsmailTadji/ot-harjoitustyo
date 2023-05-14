# Architecture

## Package and class diagram

![package_and_class](https://github.com/IsmailTadji/ot-harjoitustyo/blob/master/Pong/documentation/pictures/classes_packaging.png)

## Packages
The logic directory, contains all the logic needed to run the game.
The ui directory, contains all the drawing and ui buttons.
The running directory, contains the game loop
The repositories directory, contains the database fetch and add functions.

## UI

The ui folder contains draw, and menu buttons, which have been separate from the games logic and only use the [button_logic](https://github.com/IsmailTadji/ot-harjoitustyo/blob/master/Pong/src/logic/button_logic.py) for the clickability of the main menu buttons. When a button is clicked, a new ui window replaces the previous one. 

## Game logic

The game logic is seperated in its own [directory](https://github.com/IsmailTadji/ot-harjoitustyo/blob/master/Pong/src/logic/pong_logic.py).

![Pong_logic](https://github.com/IsmailTadji/ot-harjoitustyo/blob/master/Pong/documentation/pictures/Pong_logic.png)

Pong class contains all the logic needed for the games functionality. It makes 2 rackets through the [Racket](https://github.com/IsmailTadji/ot-harjoitustyo/blob/master/Pong/src/logic/racket_logic.py) class and a ball through the [Ball](https://github.com/IsmailTadji/ot-harjoitustyo/blob/master/Pong/src/logic/ball_logic.py) class. Movement of the rackets is handled in the Pong class, but the logic is in the Racket class. Same with the ball movement. Collision is handled in the Pong class.

## Database

The players names and their scores are stored in a SQLite table called scores.

The following sequence diagrams illustrate how the data is stored to and fetched from the database.

### During the game end screen:


If the player does not input a name, the score is not saved and you will be returned to the main menu. However if the name is inputted, the name and score will then be saved in the database before returning to the main menu.
![New_score](https://github.com/IsmailTadji/ot-harjoitustyo/blob/master/Pong/documentation/pictures/new_score.png)


### During the main menu:


If the leaderboards button is clicked, the game loop will call the top5_scores function and it will return a list of tuples with the names and scores. Then the game loop will call the draw_leaderboards function and it will display the top 5 scores from the table on the screen.

![Top5_scores](https://github.com/IsmailTadji/ot-harjoitustyo/blob/master/Pong/documentation/pictures/top5_scores.png)


