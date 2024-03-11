from itertools import permutations, product

def card_value(card):
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return [1, 11]
    else:
        return int(card)

def solve_24(cards):
    ops_combinations = product('+-*/', repeat=3)
    for perm in permutations(cards):
        a_index = perm.index('A')
        for a_value in card_value('A'):
            perm_with_a = perm[:a_index] + (a_value,) + perm[a_index+1:]
            for ops in ops_combinations:
                expr = f'(({card_value(perm_with_a[0])}{ops[0]}{card_value(perm_with_a[1])}){ops[1]}{card_value(perm_with_a[2])}){ops[2]}{card_value(perm_with_a[3])}'
                try:
                    if eval(expr) == 24:
                        return expr
                except ZeroDivisionError:
                    pass
    return "No solution"

def main():
    cards = input("Please enter four cards separated by spaces (2-10, J, Q, K, A): ").split()
    print("Solution:", solve_24(cards) if len(cards) == 4 else "Please enter exactly four cards.")

if __name__ == "__main__":
    main()