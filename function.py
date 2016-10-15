"""x for x in s1 if x in s2"""
"""X=99
def func(Y):
    Z=X+Y
    return Z
print (func(1))"""

def maker(N):
    def action (X):
        return X**N
    return action
"""f=maker(2)
print(f)
print(f(3))"""
g=maker(3)
print(g)
print(g(3))
