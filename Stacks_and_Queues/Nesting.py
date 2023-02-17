# O(N) Time_Complexity
def solution(S):
    characters = {
        ']': '[',
        ')': '(',
        '}': '{',
    }
    stack = []

    for s in S:
        if s in characters:  # search items to see if its a closing bracket
            if not stack:
                return 0
            if stack.pop() != characters[s]:
                return 0
        else:
            stack.append(s)  # add opening brackts to stack
    if stack:
        return 0  # stack is not empty
    else:
        return 1  # stack is properly nested

"""
A string S consisting of N characters is called properly nested if:

S is empty;
S has the form "(U)" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, string "(()(())())" is properly nested but string "())" isn't.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.

For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..1,000,000];
string S is made only of the characters "(" and/or ")".
"""