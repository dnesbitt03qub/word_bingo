# Word Bingo

A program to play word bingo by reading in .srt files from TV shows or movies. Each player guesses 5 words and the player who's words appear most often wins!

## Creating a game

The program can be run with:

```
python3 word_bingo.py
```

and the program will ask you:

1. Number of players
2. Player names (in order of selection)
3. Words
4. Name of the save file (game_file)

Words are chosen in snake draft style (e.g. for 4 players `123443211234`

## Evaluating the game

The program can be run in evaluation mode with:

```
python3 word_bingo.py game_file example.srt
```

which will let you step through the results for the top words