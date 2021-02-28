from typing import Dict, List, Set

class CharacterSet:
    '''文字集合を表す。
    必ず偶数個の要素からなり、以下の条件を満たす文字cはこの集合に含まれる。
    intervals[2*n] <= c < intervals[2*n + 1]
    where 0 <= n in Z

    以上の条件から、intervalsは同一の要素を持たない。∵同一の要素が2個あれば空集合を表すため、削除できる。

    全文字集合: intervals = [LOWER_BOUND, UPPER_BOUND]
    空文字集合: intervals = []

    補集合を取るには、次の操作を行えばよい。
        - intervals[0]がLOWER_BOUND -> intervals[0]を削除。そうでなければLOWER_BOUNDをintervalsの最初に追加。
        - intervals[-1]がUPPER_BOUND -> intervals[-1]を削除。そうでなければUPPER_BOUNDをintervalsの最後に追加。

        例: intervals = [j, k, l, m] として、
            1) j = LOWER_BOUND, m = UPPER_BOUND なら、
                intervals: LOWER_BOUND <= c < k, l <= c < UPPER_BOUND
                intervals^c: k <= c < l
                    -> intervals = [k, l]
            2) j = LOWER_BOUND, m < UPPER_BOUND なら、
                intervals: LOWER_BOUND <= c < k, l <= c < m
                intervals^c: k <= c < l, m <= c < UPPER_BOUND
                    -> intervals = [k, l, m, UPPER_BOUND]
            3) LOWER_BOUND < j, m = UPPER_BOUND なら、
                intervals: j <= c < k, l <= c < UPPER_BOUND
                intervals^c: LOWER_BOUND <= c < j, k <= c < l
                    -> intervals = [LOWER_BOUND, j, k, l]
            4) LOWER_BOUND < j, m < UPPER_BOUND なら、
                intervals: j <= c < k, l <= c < m
                intervals^c: LOWER_BOUND <= c < j, k <= c < l, m <= c < UPPER_BOUND
                    -> intervals = [LOWER_BOUND, j, k, l, m, UPPER_BOUND]
    '''
    LOWER_BOUND = 0
    UPPER_BOUND = 0x110000

    def __init__(self, intervals: List[int] = []) -> None:
        intervals = [c for c in intervals if CharacterSet.LOWER_BOUND <= c <= CharacterSet.UPPER_BOUND]
        self.intervals = sorted(set(intervals))
        # 重複要素を除いたあと、要素数が奇数だった場合、upper boundを調整する。
        if len(self.intervals) % 2 == 1:
            self._complement_upper_bound()

    def _complement_lower_bound(self):
        if self.intervals[0] == CharacterSet.LOWER_BOUND:
            self.intervals = self.intervals[1:]
        else:
            self.intervals.insert(0, CharacterSet.LOWER_BOUND)

    def _complement_upper_bound(self):
        if self.intervals[-1] == CharacterSet.UPPER_BOUND:
            self.intervals = self.intervals[0:-1]
        else:
            self.intervals.append(CharacterSet.UPPER_BOUND)

    def empty(self):
        self.intervals.clear()

    def is_empty(self):
        return len(self.intervals) == 0

    def includes(self, c: str) -> bool:
        codepoint = ord(c[0]) # cに文字列が指定されたら先頭の文字が指定されたものとみなす。
        included = False
        for i in range(0, len(self.intervals), 2):
            if self.intervals[i] <= c < self.intervals[i + 1]:
                included = True
                break
        return included

    def is_continuous(self) -> bool:
        return len(self.intervals) == 2

    def count(self):
        count = 0
        for i in range(0, len(self.intervals), 2):
            count += self.intervals[i + 1] - self.intervals[i]
        return count

    def complement(self) -> CharacterSet:
        cloned = CharacterSet(self.intervals)
        cloned._complement_lower_bound()
        cloned._complement_upper_bound()
        return cloned

    def divide(self) -> List[CharacterSet]:
        result = []
        for i in range(0, len(self.intervals), 2):
            charset = CharacterSet([self.intervals[i], self.intervals[i + 1]])
            result.append(charset)
        return result
    
    def divide_into_tuples(self) -> List[Tuple[int, int]]:
        result = []
        for i in range(0, len(self.intervals), 2):
            charset = (self.intervals[i], self.intervals[i + 1])
            result.append(charset)
        return result

    def add_interval(self, interval: CharacterSet) -> CharacterSet:
        divided_self = self.divide()
        return None

    def subtract_interval(self, interval: CharacterSet) -> CharacterSet:
        return None

def new_interval(lower: int, upper:int) -> CharacterSet:
    initial = [] if lower == upper else [lower, upper]
    return CharacterSet(initial)
