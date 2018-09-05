print "Look, isn't it a dynamic binding?"

def f():
    print "No definition of 'a' in 'f'. But, a = ", a

print "Let's now define 'a' = 5 (outside of f)"  
a = 5

print "Then, call f()"
f()

print "Now, redefine 'a' = 6 (still outside of f)"
a = 6

print "Calling the same f() again"
f()

