import re
from collections import deque

def is_palindrome(s: str) -> bool:
    s = re.sub(r'[^a-z]', '', s.lower())

    deq = deque(s)

    while len(deq) > 1:
        if deq.popleft() != deq.pop():
            return False
    return True
    