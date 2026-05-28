'''
RECURSION refers to a function calling itself to solve a problem.
It involves two critical components:
Base case: This is the condition that terminates the recursion.

Without it, the recursive calls would continue forever, eventually causing the function to crash or exhaust available memory
'''


# example
def countdown(n):
    print(n)

    if n == 0:
        return

    countdown(n - 1)

countdown(3)