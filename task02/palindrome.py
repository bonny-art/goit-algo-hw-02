import re
from collections import deque

def is_palindrome(s: str) -> bool:
    """
    Determines whether a given string is a palindrome, ignoring case,
    spaces, punctuation, and special characters.

    This function normalizes the input string by converting it to lowercase 
    and removing all non-alphabetic characters. It then uses a deque to 
    check if the cleaned string is a palindrome by comparing characters 
    from the beginning and the end.

    Args:
        s (str): The input string to be checked.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Remove all non-alphabetic characters and convert to lowercase
    s = re.sub(r'[^a-z]', '', s.lower())

    # Use deque to efficiently pop from both ends
    deq: deque[str] = deque(s)

    while len(deq) > 1:
        if deq.popleft() != deq.pop():
            return False
    return True
