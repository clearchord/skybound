from typing import Dict, List, Set

class CharacterSet:
    SENTINEL = 0x110000

    def __init__(self, intervals: List[int] = [0, CharacterSet.SENTINEL]) -> None:
        # This set includes 
        #     self.intervals[0] <= c < self.intervals[1]
        #     self.intervals[2] <= c < self.intervals[3]
        #     ...
        # and does not include
        #     U+000000 <= c < self.intervals[0] (if 0 < self.intervals[0])
        #     self.intervals[1] <= c < self.intervals[2], 
        #     self.intervals[3] <= c < self.intervals[4], 
        #     ...
        intervals = sorted(set(intervals))
        if intervals[-1] != CharacterSet.SENTINEL:
            intervals.append(CharacterSet.SENTINEL)

        self.intervals: List[int] = intervals # must be ordered list and terminated with SENTINEL

    def empty(self):
        self.intervals.clear()
        self.intervals.append(CharacterSet.SENTINEL)

    def is_empty(self):
        return len(self.intervals) == 1

    def includes(self, c: str) -> bool:
        codepoint = ord(c[0])
        included = False
        for index, border in enumerate(self.intervals):
            if codepoint < border:
                included = index % 2 == 0
                break
        return included

    def is_contiguous(self) -> bool:
        size = len(self.intervals)
        return size == 2 or size == 3

    def complement(self) -> CharacterSet:
        if self.intervals[0] == 0:
            result = CharacterSet(self.intervals[1:])
        else:
            result = CharacterSet([0] + self.intervals)
        return result

    def divide(self) -> List[CharacterSet]:
        return []

def new_interval(lower: int, upper:int) -> CharacterSet:
    initial = [] if lower == upper else [lower, upper]
    return CharacterSet(initial)


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


