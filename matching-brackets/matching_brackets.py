L_BRACKETS = ['[', '{', '(']
R_BRACKETS = [']', '}', ')']

def is_paired(input_string):

    stack = []

    for c in input_string:

        if c in L_BRACKETS:
            # Add all found left brackets to the stack
            stack.append(c)
        if c in R_BRACKETS:
            # A right bracket is only valid if there is a matching left
            # bracket at the top of the stack
            if len(stack) == 0:
                return False
            if stack[-1] == L_BRACKETS[R_BRACKETS.index(c)]:
                stack.pop()
            else:
                return False

    # If there are items left in the stack the expression is not fully matched
    return len(stack) == 0

is_paired("[({}])")