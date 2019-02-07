import game_data
import subtitle_word_loader as swl

def evaluate_game(game_file_path: str, subtitle_path: str):
    # Load game file from the path
    game = game_data.GameState()
    game.load_from_file(game_file_path)
    
    # Get the list of words from the subtitle file
    words_from_subtitle_file = swl.get_words_from_subtitle_file(subtitle_path)
    
    print(words_from_subtitle_file)
    
    # Get the list of words that the players have guessed
    guessed_words - game.get_all_words()
    
    # Set counts for each of the guessed words
    # Set those counts for each player
    # Extension: Get the top 10 words and fill in
    
    # Display the results all fancy