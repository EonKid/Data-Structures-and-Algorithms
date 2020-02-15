"""
https://www.hackerrank.com/challenges/balanced-brackets/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues

"""
from data_structures_algorithms.stacks.stacks import Stack

def isBalanced(s):
    if len(s) == 0: return True

    exp_stack = Stack()

    for chr in s:
        if chr is '(' or chr is '{' or chr is '[':
            exp_stack.push_stack(chr)
        else:
            if exp_stack.is_empty(): return False
            current_top = exp_stack.pop_stack()
            if current_top is not None:
                top_char = current_top.key
                if top_char is '(' and chr is not ')' or top_char is '{' and chr is not '}' or top_char is '[' and chr is not ']':
                    return False
    return exp_stack.is_empty()

string = '(){}['
print(isBalanced(string))