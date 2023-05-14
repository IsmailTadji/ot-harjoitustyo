# Testing

The project is tested using automated unittests and manual tests.

## Unittests

### Pong logic

Pong logic is tested with the [TestPong](https://github.com/IsmailTadji/ot-harjoitustyo/blob/master/Pong/src/tests/pong_test.py) class.
The class tests whether the rackets and the ball have initialised, collision and the ai movement.

### Racket logic

Racket logic is tested with the [TestRacket](https://github.com/IsmailTadji/ot-harjoitustyo/blob/master/Pong/src/tests/racket_test.py) class. The class whether the racket is drawn correctly, and its movement.

### Ball logic

Ball logic is tested with the [TestBall](https://github.com/IsmailTadji/ot-harjoitustyo/blob/master/Pong/src/tests/ball_test.py) class. The class tests initial values of the ball, and its movement.

### Score logic

Score logic is tested with the [TestScore](https://github.com/IsmailTadji/ot-harjoitustyo/blob/master/Pong/src/tests/score_test.py) class. The clas tests the initial values, awarding points, and the single player point system.

### Button logic

Button logic is tested with the [TestButton](https://github.com/IsmailTadji/ot-harjoitustyo/blob/master/Pong/src/tests/button_test.py) class. The class tests the initial values of the buttons, and the clicking logic.

## Game loop and UI

The game loop and ui are tested manually, following the [user guide](https://github.com/IsmailTadji/ot-harjoitustyo/blob/master/Pong/documentation/user_guide.md), and with multiple false inputs to detect any malfunctions.

### Coverage report:

![Coverage](https://github.com/IsmailTadji/ot-harjoitustyo/blob/master/Pong/documentation/pictures/cov_rep.png)

## Missing tests:

The database repository has not been tested.