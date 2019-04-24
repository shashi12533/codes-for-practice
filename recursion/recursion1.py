question description

:Write a function to generate all possible n pairs of balanced parentheses.
Examples:

Input : n=1
Output: {}

Input : n=2
Output: 
{}{}
{{}}




def _printParenthesis(open, close,output):
    # import pdb
    # pdb.set_trace()
    if open == 0 and close == 0:
            print(output)
            return


    if open:
        _printParenthesis(open-1, close, output+"(");

    if open < close:
        _printParenthesis(open, close-1, output+")");


n = 2;
str = [""] * 2 * n;
output=""
_printParenthesis(n, n,output);