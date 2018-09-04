# Task 004.

# So, what is the "scope"? 
#
# "Scope of a name binding" is....
# well, let's find out what we already know.
# We do not know what "scope" or "binding" mean. But we do know what is a name.
# Actually, a name of a variable. Like here:
a = 5

# Here, "a" is a variable. Its name is... well, "a". 
# What is its value? Correct, it's 5.
# What is "="? Correct, it's an operator (a function).
# This function binds a value "5" to a name "a". It creates a "binding".

# If you try the following:
print "I am " + age + " years old."
age = 15

# ... you will get an error:
# >>  NameError: name 'age' is not defined

# If you try this:
age = 15
print "I am " + age + " years old."

# ... no errors. Because at the first time, name "age" has not been bound to a value yet.
# Clear?

# Now, what happens here:

def f1():
    a1 = 5
    print "a = ", a1

    





# PS: 
# You might have also read about it in the wiki:
# https://en.wikipedia.org/wiki/Scope_(computer_science)
# Or you could have asked Google, but... 
# That's not easy to ask something when you don't know what you need to ask about.
