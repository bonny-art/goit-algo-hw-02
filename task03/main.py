def is_balanced(string):
    stack = []
    matching_bracket = {')': '(', '}': '{', ']': '['}
    
    for char in string:
        if char in matching_bracket.values():
            stack.append(char)
        elif char in matching_bracket.keys():
            if stack == [] or matching_bracket[char] != stack.pop():
                return False
    return stack == []

# Тестові приклади
print(is_balanced("( ){[ 1 ]( 1 + 3 )( ){ }}"))  # Виведе: True
print(is_balanced("( 23 ( 2 - 3);"))           # Виведе: False
print(is_balanced("( 11 }"))                   # Виведе: False