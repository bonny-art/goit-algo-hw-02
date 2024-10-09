def is_balanced(string: str) -> bool:
    """
    Checks if a given string has balanced brackets and prints the result.

    This function determines whether the parentheses, curly braces, and square
    brackets in a string are correctly balanced. It ignores non-bracket characters.

    Args:
        string (str): The input string containing brackets and other characters.

    Returns:
        bool: True if the brackets are balanced, False otherwise.
    """
    stack: list[str] = []
    matching_bracket: dict[str, str] = {')': '(', '}': '{', ']': '['}

    print(f'\nChecking string: {string}')
    
    for char in string:
        if char in matching_bracket.values():
            stack.append(char)
        elif char in matching_bracket.keys():
            if not stack or matching_bracket[char] != stack.pop():
                print('Result: Not balanced')
                return False

    result = not stack
    print(f'Result: {"Balanced" if result else "Not balanced"}')
    return result

# Test examples
is_balanced("( ){[ 1 ]( 1 + 3 )( ){ }}")  # Outputs: Balanced
is_balanced("( 23 ( 2 - 3);")             # Outputs: Not balanced
is_balanced("( 11 }")                     # Outputs: Not balanced
is_balanced("([]){}")                     # Balanced
is_balanced("[{()}]")                     # Balanced
is_balanced("{[()()]}")                   # Balanced
is_balanced("{[(])}")                     # Not balanced
is_balanced("(((()")                      # Not balanced
is_balanced("({[}])")                     # Not balanced



