# Pong

A Pong game with single and two player modes, with a leaderboard for single player.

## Documentation

[Timelog.md](https://github.com/IsmailTadji/ot-harjoitustyo/blob/master/Pong/documentation/timelog.md)

[Requirements_specifications.md](https://github.com/IsmailTadji/ot-harjoitustyo/blob/master/Pong/documentation/requirements_specifcations.md)

[Changelog.md](https://github.com/IsmailTadji/ot-harjoitustyo/blob/master/Pong/documentation/changelog.md)

[Architecture.md](https://github.com/IsmailTadji/ot-harjoitustyo/blob/master/Pong/documentation/architecture.md)

## Game release

[Full release](https://github.com/IsmailTadji/ot-harjoitustyo/releases/tag/Viikko5)

## Documentation:

[Architecture:](https://github.com/IsmailTadji/ot-harjoitustyo/blob/master/Pong/documentation/architecture.md)

[Changelog:](https://github.com/IsmailTadji/ot-harjoitustyo/blob/master/Pong/documentation/changelog.md)

[Requirements specifications:](https://github.com/IsmailTadji/ot-harjoitustyo/blob/master/Pong/documentation/requirements_specifications.md)

[Testing:](https://github.com/IsmailTadji/ot-harjoitustyo/blob/master/Pong/documentation/testing.md)

[Timelog:](https://github.com/IsmailTadji/ot-harjoitustyo/blob/master/Pong/documentation/timelog.md)

[User guide:](https://github.com/IsmailTadji/ot-harjoitustyo/blob/master/Pong/documentation/user_guide.md)

Installing instructions:



1. Install dependancies
```
poetry install
```

2. Initialise the database
```
poetry run invoke build
```

3. Start the game
```
poetry run invoke start
```

## Command-line tasks

To test the game, execute the following:
```
poetry run invoke test
```

To generate a coverege of the tests, execute the following:
```
poetry run invoke coverage
```

To generate the coverage into a report, execute the following:
``` 
poetry run invoke coverage-report
```

To open said report, execute the following:
```
poetry run invoke coverage-report-open
```

To do pylint checks, execute the following:
```
poetry run invoke lint
```
