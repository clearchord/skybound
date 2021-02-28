from typing import Dict, List, Set

class LexerNode:
    def __init__(self, final: bool = False) -> None:
        self.transitions: Dict[str, 'LexerNode'] = {} #TODO: Consider more efficient data structure.
        self.final = final

    def add_transition(self, letter: str, node: 'LexerNode') -> None:
        self.transitions[letter] = node


