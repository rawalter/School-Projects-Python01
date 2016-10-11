#!/usr/bin/python3.4
#Exercise: 18.6
#By: Robert A. Walters
#Created on: 4/18/16
#Program Description: matching grouping symbols

def check_parentheses(s):
    """ Return True if the parentheses in string s match, otherwise False. """
    j = 0
    for c in s:
        if c == '('or '{' or '[':
            j -= 1
            if j < 0:
                return False
        elif c == ')' or '}' or ']':
            j += 1
    return j == 0

def find_parentheses(s):
    """ Find and return the location of the matching parentheses pairs in s.

    Given a string, s, return a dictionary of start: end pairs giving the
    indexes of the matching parentheses in s. Suitable exceptions are
    raised if s contains unbalanced parentheses.

    """

    # The indexes of the open parentheses are stored in a stack, implemented
    # as a list

    stack = []
    parentheses_locs = {}
    for i, c in enumerate(s):
        if c == '(' or '{' or '[':
            stack.append(i)
        elif c == ')'or '}' or ']':
            try:
                parentheses_locs[stack.pop()] = i
            except IndexError:
                raise IndexError('Too many close groups at index {}'
                                                                .format(i))
    if stack:
        raise IndexError('No matching close groups to open groups '
                         'at index {}'.format(stack.pop()))
    return parentheses_locs

filename = open(input("Enter Filename: "),'r')
#!/usr/bin/python3.4
#Exercise: 18.6
#By: Robert A. Walters
#Created on: 4/18/16
#Program Description: matching grouping symbols

def check_parentheses(s):
    """ Return True if the parentheses in string s match, otherwise False. """
    j = 0
    for c in s:
        if c == ')'or '}' or ']':
            j -= 1
            if j < 0:
                return False
        elif c == '('or '{' or '[':
            j += 1
    return j == 0

def find_parentheses(s):
    """ Find and return the location of the matching parentheses pairs in s.

    Given a string, s, return a dictionary of start: end pairs giving the
    indexes of the matching parentheses in s. Suitable exceptions are
    raised if s contains unbalanced parentheses.

    """

    # The indexes of the open parentheses are stored in a stack, implemented
    # as a list

    stack = []
    parentheses_locs = {}
    for i, c in enumerate(s):
        if c == '('or '{' or '[':
            stack.append(i)
        elif c == ')'or '}' or ']':
            try:
                parentheses_locs[stack.pop()] = i
            except IndexError:
                raise IndexError('Too many close parentheses at index {}'
                                                                .format(i))
    if stack:
        raise IndexError('No matching close parenthesis to open parenthesis '
                         'at index {}'.format(stack.pop()))
    return parentheses_locs

filename = open(input("Enter Filename: "),'r')



for i, s in enumerate(filename, start=1):
    print('\ntest string {}:\n{}'.format(i, s))
    print('Parentheses match?', check_parentheses(s))
    try:
        parentheses_locs = find_parentheses(s)
        print('Parentheses locations:\n{}'.format(str(
                    sorted([(k,v) for k, v in parentheses_locs.items()])
           )))
    except IndexError as e:
        print(str(e))



for i, s in enumerate(filename, start=1):
    print('\ntest string {}:\n{}'.format(i, s))
    print('Parentheses match?', check_parentheses(s))
    try:
        parentheses_locs = find_parentheses(s)
        print('Parentheses locations:\n{}'.format(str(
                    sorted([(k,v) for k, v in parentheses_locs.items()])
           )))
    except IndexError as e:
        print(str(e))
