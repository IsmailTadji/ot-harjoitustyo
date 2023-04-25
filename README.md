# Software engineering, practical exercise
## Pong-game
Pong 2-player pong, possibly single-player.

## Documentation

[Timelog.md](https://github.com/IsmailTadji/ot-harjoitustyo/blob/master/Pong/documentation/timelog.md)

[Requirements_specifications.md](https://github.com/IsmailTadji/ot-harjoitustyo/blob/master/Pong/documentation/requirements_specifcations.md)

[Changelog.md](https://github.com/IsmailTadji/ot-harjoitustyo/blob/master/Pong/documentation/changelog.md)

[Architecture.md](https://github.com/IsmailTadji/ot-harjoitustyo/blob/master/Pong/documentation/architecture.md)

## Game release

[Release](https://github.com/IsmailTadji/ot-harjoitustyo/releases/tag/Viikko5)

Installing instructions:

1. Install dependancies
```
poetry install
```

2. Start the game
```
poetry run invoke start
```

To test the game, execute the following:
```
poetry run invoke test:
```

To generate a coverage report, execute the following:
``` 
poetry run invoke coverage-report
```

To do pylint checks, execute the following:
```
poetry run invoke lint
```
