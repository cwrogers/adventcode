##
## NOT MY FILE  
## source: https://gist.github.com/nthistle/5244b04be6a2eae545e6908369d39592/
##


from math import *
from collections import defaultdict, Counter
import re
from typing import TypeVar, Generator, Iterable, Tuple, List
import heapq

hpush = heapq.heappush
hpop = heapq.heappop

_T = TypeVar("T")

def adjacent_pairs(elements: Iterable[_T]) -> Generator[Tuple[_T, _T], None, None]:
    elements_iter = iter(elements)
    last_element = next(elements_iter)
    for element in elements_iter:
        yield (last_element, element)
        last_element = element

def all_pairs(elements: Iterable[_T]) -> Generator[Tuple[_T, _T], None, None]:
    elements_list = list(elements)
    for i in range(len(elements_list)):
        for j in range(i + 1, len(elements_list)):
            yield (elements_list[i], elements_list[j])

def all_tuples(elements: Iterable[_T]) -> Generator[Tuple[_T, _T], None, None]:
    elements_list = list(elements)
    for i in range(len(elements_list)):
        for j in range(len(elements_list)):
            if j == i: continue
            yield (elements_list[i], elements_list[j])


# yes, everyone else calls this "cumsum" but ohwell
def rolling_sum(elements: Iterable[_T], start: _T = None) -> List[_T]:
    rsum = []
    elements_iter = iter(elements)
    
    if start is None:
        rsum.append(next(elements_iter))
    else:
        rsum.append(start)
    
    for element in elements_iter:
        rsum.append(rsum[-1] + element)
    return rsum


# I did some rough experiments with this version vs. a version that uses a deque, which
# has efficient popleft, and it seems like this version actually wins because of how slow
# iterating over a deque is (which you ~have to do if you want to use the results)
def rolling_window(
    elements: Iterable[_T],
    window_size: int,
) -> Generator[Tuple[_T, ...], None, None]:
    current_window = []
    for element in elements:
        current_window.append(element)
        if len(current_window) > window_size:
            del current_window[0]
        if len(current_window) == window_size:
            yield current_window



# this is like slightly borked because it doesn't get negative numbers
# oh well i guess
##nums_regex = regex.compile("([^\\d]*)((?P<nums>\\d+)([^\\d]*))*")
##
##def nums(s):
##    m = nums_regex.match(s)
##    vals = m.capturesdict()["nums"]
##    return [int(x) for x in vals]

def nums(s):
    m = re.findall("-?\d+", s)
    return [int(x) for x in m]

def numsp(s):
    m = re.findall("-?\d+", s)
    return [int(x) for x in m]

def sign(x):
    if x < 0:
        return -1
    elif x == 0:
        return 0
    else:
        return 1

# latest version of IDLE has annoying print behavior, so let's manually
# fix it here

# you get 100 prints before they start getting suppressed
print_counter = -100
next_counter_limit = 10
print_ = print
def print(*args, sep=' ', end='\n', file=None, flush=False):
    global print_counter, next_counter_limit
    if print_counter < 0:
        print_(*args, sep=sep, end=end, file=file, flush=flush)
        print_counter += 1
    elif print_counter == next_counter_limit:
        print_(f"[{next_counter_limit} lines of prints suppressed]")
        print_counter = 0
        next_counter_limit *= 10
    else:
        print_counter += 1

# underscored names are in case functions get shadowed by accident
adjp = _adjp = adjacent_pairs
ap = _ap = all_pairs
at = _at = all_tuples
rw = _rw = rolling_window
rsum = _rsum = rolling_sum

dd = _dd = defaultdict
ctr = _ctr = Counter

adj4 = [(1,0),(0,1),(-1,0),(0,-1)]
adj8 = [(dx,dy) for dx in (-1,0,1) for dy in (-1,0,1) if (dx,dy)!=(0,0)]

