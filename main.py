#!/usr/bin/python3
# timeline 39.18
def is_star(char):
    return char == '*'


def is_plus(char):
    return char == '+'


def is_question(char):
    return char == '?'


def is_operator(char):
    return is_star(char) or is_plus(char) or is_question(char)


def is_literal(char):
    return char.isalpha() or char.isdigit() 


def is_set(term):
    return is_open_set(term[0]) and is_close_set(term[-1])


def is_unit(term):
    return is_literal(term[0]) or is_set(term)
   

def is_open_set(char):
    return '['


def is_close_set(char):
    return ']'


def split_expr(expr):
    head = None
    operator = None
    rest = None 
    head_end_pos = None

    if is_open_set(expr[0]):
        head_end_pos = expr.find(']') + 1
        head = expr[0:head_end_pos + 1]
    elif is_literal(expr[0]):
        head_end_pos = 1
        head = expr[0]

    if is_operator(expr[head_end_pos]):
        operator = expr[head_end_pos]
        head_end_pos += 1

    rest = expr[head_end_pos + 1:]
    return head, operator, rest


def does_unit_match(expr, string):
    return expr[0] == string[0]


def match_exp(expr, string, match_length=0):
    if len(expr) == 0:
        return [True, match_length]
    
    if does_unit_match(expr, string):
        return match_exp(expr[1:], string[1:], match_length + 1)
    else:
        print('Unknow token')
    
    return [False, None]


def matc(expr, string):
    match_pos = 0
    matched = False
    max_matched_pos = len(string) - 1
    while not matched and match_pos < max_matched_pos:
        [matched, match_length] = match_exp(expr, string[match_pos:])
        if matched:
            return [matched, match_pos, match_length]
        match_pos += 1
    return [False, None, None]


def main():
    """ main entry of the application """
    # print(split_expr('abc'))
    # print(split_expr('[123]*bc'))
    # print(split_expr('[123]abc'))
    # print(split_expr('[323]+bc'))
    return
    expr = 'abc'
    string = "abc whaever"
    [matched, match_pos, match_length] = matc(expr, string)
    if matched:
        print(f'Mact expession({expr}, {string}) = {string[match_pos: match_pos + match_length]}')
    else:
        print(f'Mact expession({expr}, {string}) = False')

    print("hello")


if __name__ == '__main__':
    main()
