from typing import Dict, List, Set

class CharacterSet:
    def __init__(self) -> None:
        # Any Unicode character c within U+000000 <= c < self.intervals[0] is included in this character set.
        # Any character c withing self.intervals[0] <= c < self.interval[1] is not.
        # As such, intervals are alternatively included or not in this character set.
        # When all Unicode characters are included in this set, self.intervals = {U+110000}
        # Also when no character is included in this set, self.intervals = {U+000000}
        self.intervals: List[int] = {0x110000} # ordered list

    def empty(self):
        self.intervals.clear()
        self.intervals.append(0)

    def isin(self, c: str) -> bool:
        codepoint = ord(c[0])
        included = False
        for index, border in enumerate(self.intervals):
            if codepoint < border:
                included = index % 2 == 0
                break
        return included

class Node:
    def __init__(self, final: bool = False) -> None:
        self.transitions: Dict[str, Node] = {} #TODO: Consider more efficient data structure.
        self.final = final

    def add_transition(self, letter: str, node: 'Node') -> None:
        self.transitions[letter] = node

class NFA:
    def __init__(self) -> None:
        self.node_initial = Node()
        self.node_final = Node(final=True)

class DFA:
    def __init__(self) -> None:
        self.node_initial = Node()
        self.node_final = Node(final=True)


