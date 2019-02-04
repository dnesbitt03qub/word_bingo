import game_data
from typing import List, Dict

ROUNDS = 5
DEFAULT_SAVE_PATH = 'game_state.json'

def get_player_count() -> int:
    player_count = input('How many people are playing? ')
    return int(player_count)    
    
def get_players(player_count: int) -> List[str]:
    player_list = input('Who is playing? (Enter ' + str(player_count) + ' players separated by spaces) ')
    players = player_list.split()
    return players
    
# Returns the order of selection from the list of players in snake draft order
def get_selection_order(players: List[str], rounds: int) -> List[str]:
    selection_order = []
    
    reverse = False
    for i in range(0,rounds):
        if reverse:
            selection_order.append(players.reverse())
            reverse = False
        else:
            selection_order.append(players)
            reverse = True
    
    return selection_order
    
def get_word(player: str) -> str:
    word = input(player + ' select a word: ')
    return word

def get_save_path() -> str:
    path = input('File to save game to [Default ' + DEFAULT_SAVE_PATH + ']')
    if path:
        return path
    else:
        return DEFAULT_SAVE_PATH

def get_words(players: List[str], rounds: int) -> Dict[str, List[str]]:
    words = {}
    
    # The list of players names in order of word selection (snake draft)
    selection_order = get_selection_order(players, rounds)
    
    print('Select your words!')
    
    # Loop through and get all the words from input
    for player_selecting in selection_order:
        list_for_player = words[player_selecting]
        word = get_word(player_selecting)
        list_for_player.append(word)
        
    return words
    
def save_game_info(player_count: int, players: List[str], words: Dict[str, List[str]], game_file_path: str):
    game_state = game_data.GameState(player_count, players, words)
    game_state.save(game_file_path)

# Create the game - define values and save to file
def create_game():
    
    # Get game info
    player_count = get_player_count()
    players = get_players(player_count)
    words = get_words(players, ROUNDS)
    game_file_path = get_save_path()
    
    # Save game info
    save_game_info(player_count, players, words, game_file_path)
    
