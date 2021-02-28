from typing import Dict, List, Set
from .lexer_node import LexerNode

class DFA:
    def __init__(self) -> None:
        self.node_initial = LexerNode()
        self.node_final = LexerNode(final=True)

