from itertools import permutations, product

def solve_24(numbers):
    ops_combinations = product('+-*/', repeat=len(numbers)-1)
    paran=product('()',repeat=2*len(numbers)-4)
    for perm in permutations(numbers):
        for ops in ops_combinations:
            expr = str(perm[0])
            for i in range(len(ops)):
                expr += ops[i] + str(perm[i+1])
            try:
                if eval(expr) == 24:
                    return expr
            except ZeroDivisionError:
                pass
    return "No solution"

def main():
    print("Please enter any amount of number separated by spaces:")
    numbers = list(map(float, input().split()))
    solution = solve_24(numbers)
    print("Solution:", solution)

if __name__ == "__main__":
    main()
