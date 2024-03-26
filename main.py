#!/usr/bin/python3

def does_unit_match(expr, string):
    return expr[0] == string[0]


def match_exp(expr, string, match_length=0):
    if len(expr) == 0:
        return [True, match_length]
    if does_unit_match(expr, string):
        return match_exp(expr[1:], string[1:], match_length + 1)
    else:
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