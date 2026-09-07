"""First python file"""
from operator import floordiv, mod 
def divider(m, n):
    return mod(m, n), floordiv(m, n)
remainder, quotient = divider(22198734, 8.3)
print(remainder, quotient)
