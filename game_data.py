import json
from typing import List, Dict

class GameState:
    
    def set_members(self, player_count: int, players: List[str], words: Dict[str, List[str]]):
        self.player_count = player_count
        self.players = players
        self.words = words
        
    # Load the game state from JSON
    def load_from_file(self, path: str):
        with open(path, 'r') as read_file:
            self.__dict__ = json.load(read_file)
        
    # Save the game state to JSON
    def save(self, path: str):
        with open(path, 'w') as write_file:
            json.dump(self.__dict__, write_file)