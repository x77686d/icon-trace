#
# TODOs at bottom
#
# Experimenting with tracing
#
# Show calls:
#   python -m trace --trace trace1.py 
#
#from rec_examples import *

"""

     1  procedure main(a)
     2      write(fact(integer(a[1])))
     3  end
     4  
     5  procedure fact(n)
     6      return if n = 1 then 1 else n*fact(n-1)
     7  end

             :       main(list_1 = ["5"])
fact.icn     :    2  | fact(5)    # line 2 called fact(5)
fact.icn     :    6  | | fact(4)
fact.icn     :    6  | | | fact(3)
fact.icn     :    6  | | | | fact(2)
fact.icn     :    6  | | | | | fact(1)
fact.icn     :    6  | | | | | fact returned 1
fact.icn     :    6  | | | | fact returned 2
fact.icn     :    6  | | | fact returned 6
fact.icn     :    6  | | fact returned 24
fact.icn     :    6  | fact returned 120
120
fact.icn     :    3  main failed

file
line

"""

import sys

# from https://stackoverflow.com/questions/8315389/how-do-i-print-functions-as-they-are-called

def start():
    sys.setprofile(icon_trace)

def basename(path):
    rpos = path.rfind("/")
    if rpos == -1:
        return path
    else:
        return path[rpos+1:]

def icon_trace(frame, event, arg, depth = [2]):
    #print("depth: ",depth)
    
    if event == "call":
        if depth[0] <= 0:
            return
        depth[0] += 1
        #print("-" * indent[0] + "> call function", frame.f_code.co_name)
        #print(dir(frame))
        #for x in dir(frame): print(x, type(frame.__getattribute__(x)))
        f_locals = frame.__getattribute__("f_locals")
        #print("f_locals",f_locals) # has params but not in right order
        f_code = frame.__getattribute__("f_code")
        #print("f_code",dir(f_code))
        #print("function:", f_code.co_name)  # <module>
        #print("file:", f_code.co_filename)
        #print("line:", frame.f_lineno)
        f_back = frame.__getattribute__("f_back")
        #print("called from", f_back.f_lineno)
        #print("co_argcount", f_code.co_argcount)
        #print("co_varnames", f_code.co_varnames)
        args = []
        for var in f_code.co_varnames[:f_code.co_argcount]:
            try:
                args.append("{} = {}".format(var, repr(f_locals.get(var,None))))
            except:
                args.append("{} = ???".format(var))
                
        print("{:15s} : {:4d}  {} {}({})".format(
            basename(f_code.co_filename),
            f_back.f_lineno,
            ("| " * (depth[0]-1))[:-1],
            f_code.co_name, ", ".join(args)))
        return
        
    if event == "return":
        if depth[0] < 0:
            return
        # fact.icn     :    6  | | | fact returned 6

        f_code = frame.__getattribute__("f_code")
        print("{:15s} : {:4d}  {} {} returned {}".format(
            basename(f_code.co_filename),
            frame.f_lineno,
            ("| " * (depth[0]-1))[:-1], f_code.co_name, repr(arg)))
        #print(dir(frame))
        #for x in dir(frame): print(x, type(frame.__getattribute__(x)))
        #print(frame.__getattribute__("f_locals"))
        depth[0] -= 1
        
    return icon_trace

"""
TODO:
    Shows locals along with args:
        divide(L = ['6', '0', '2', '3', '8'], value = 0, pos = None)

    Don't trace for code not in current directory

    strings in calls aren't shown in quotes!

    See bug in a12/huffman-ma.py
"""
