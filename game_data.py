import json

class GameState:
    
    __init__((player_count: int, players: List[str], words: Dict[str, List[str]]):
        self.player_count = player_count
        self.players = players
        self.words = words
        
    # Load the game state from JSON
    __init__(path: str):
        with open(path, 'r') as read_file:
            self = json.load(read_file)
        
    # Save the game state to JSON
    def save(path: str):
        with open(path, 'w') as write_file:
            json.dump(self, write_file)