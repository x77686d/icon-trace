import icon_trace
icon_trace.start()

def f(s):
    return len(g(s + "." + s))

def g(r):
    return h(("|"+r+"|").replace("e","."))

def h(p):
    return "-".join(h1(p.upper()[3:-3]))

def h1(seg):
    return list(seg)

f("test")

        

"""
trace.py  :  16  | f(s = 'test')
trace.py  :   5  | | g(r = 'test.test')
trace.py  :   8  | | | h(p = '|t.st.t.st|')
trace.py  :  11  | | | | h1(seg = 'ST.T.')
trace.py  :  14  | | | | h1 returned ['S', 'T', '.', 'T', '.']
trace.py  :  11  | | | h returned 'T-.-T-.'
trace.py  :   8  | | g returned 'T-.-T-.'
trace.py  :   5  | f returned 7
"""
