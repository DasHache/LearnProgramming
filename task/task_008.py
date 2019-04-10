# Task 008.

# Part I. Learning Git.

# Try to run 'git log' command in your project's folder.
# This is a quick way to see the history of all the commits. It shows the most recent commits first.
# The format is:

'''
commit 09f56790a0a6c7a046060f73576af84ec93fa18a
Author: kowaraj <kowaraj4stuff@gmail.com>
Date:   Wed Apr 10 22:47:40 2019 +0200

    Cleaned up. Increased canvas size. Some minor changes.

commit d0b79c2a4b65aa46f7e97291b58a69435401b46d
Author: Darya Chekeres <sha@Daryas-MacBook-Air.local>
Date:   Wed Apr 10 16:59:37 2019 +0200

    added second charge
'''

# So, it shows an ID of the commit (the very long number after the word 'commit')
# (09f56790a0a6c7a046060f73576af84ec93fa18a)
# Then, who committed (Author:). Then, when the commit was made (Date:).
# The last line is the message you gave when committed: "added second charge"

# Part II. Learning Python.
#
# Have a look at the timer class (InfiniteLoopTimer). 
# There is some complicated stuff, you should see it, but you can ignore it for now.
# As usual, try to see what EXACTLY you DO NOT UNDERSTAND and/or you don't know.
#
# Next: modifying the World class: 
# - add 'update' method
# - add a timer in 'run' method
# The idea is the following:
# The timer which is started in the 'run' method will call the 'update' method 
# every time it elapses (every 1 second by default).
# For now, 'update' does almost nothing:
# - it prints a line to the console.
# - it draws a small red circle in the top left corner of the canvas
#   (as an indicator of the 'running' update of the world)
# Later, it will be re-drawing a moving charge when a tank shoots.
