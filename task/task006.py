# Task 006 - Learn to find a correct manual. 

# 1. Add a charge at the end of the barrel.

# 2. Add a timer.
#
# Think about why you need a timer.
# In any game there is something that is moving/changing, right?
# In real life (as far as we know) everything changes in time. Time goes on.
# We do not know if there is a step. 1s? 0.00001s? 1e-999s?
# Now it's........ Sunday 20 January 2019 14:29:17.
# What is 'next'?  Sunday 20 January 2019 14:29:17.001? 
# .................Sunday 20 January 2019 14:29:17.0000000000001?
#
# Anyway, in our game we will change the state of the game every 'dt' seconds.
# Let's say for now that df = 1 second.
# What does it mean?
# At least, we have to redraw everything once every 1s. (if nothing moves).
# If something moved, we have to draw everything the same but this object.
# If the charge moves, we need to know how?
# How stuff moves described in a physics book. (it's up to you to learn)
# For now, we consider we have only linear movement with constant velocity.
# Means, there is now acceleration of any kind.
# Stuff either stays still or it moves straight forward by the same distance every 1s.
# Ok?
# 
# Now, what about a timer?
# The timer is a way to keep track of the time.
# You set it up. It goes. It expires! Then we know 1 second passed.
# Then we redraw the world as it should look in 1 second.
# Restart the timer. Repeat.
#
# You do not need to IMPLEMENT a timer yourself. It has been done for you. Use it.
# Python has a class for that, it's called Timer. 
# Normally, we shoold be able to google the rest yourself. 
# To make it easier, here is what you need to know:
# - The official documentation on Python version 2.7 :
#   https://docs.python.org/2/index.html
#   (there is a 'quick search' window on the page, use it)
#   ! Remember this link. It's the main RTFM you need for python 2.7.
# - The library that contains the class Timer is called 'threading' : 
#   https://docs.python.org/2/library/threading.html?highlight=timer#module-threading
#   (once you are on the page, use Control-F key to open a 'search' tool.)
#
# Again, normally, this should be enough to find this page:
# https://docs.python.org/2/library/threading.html?highlight=timer#timer-objects
# It tells you all you need to know to start using a timer in python.
# !!!  Try not to use this link, try to find this page yourself. !!! 
# If you couldn't find this page, try to understand why. It will help next time.
# 
# Google is poweful, but requires some understanding of what you're looking for
# and a correct way of thinking about the subject.
# 
# So, your task if to make a game that prints 'hello world' on the console every 1s. 
# (5 points)
# A more advanced task is to make the charge change its color every 1s (red-blue-red-...).
# (+5 points)
# A final task is to make the charge change its position every second (x + 10).
# (+5 points)




#   PS:
# 
#   To find what python version you are using just run 'python':
#   >> [dasha@macbook: ~ ] python
#   >> Python 2.7.10 ...
#   >> ... more stuff you do not care for now about ... 
#
#   You should be using 2.7.x. Version 3.y.y is a little different.

