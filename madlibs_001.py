#!/bin/python2
"""
This is a fun little Madlibs game written by Michael "Don't play with him" Bruno
"""

# You are able to write documentation for a python script inside the script
# uncomment the line below and rerun the script to see what happens
#help(__name__)

# The first line uses something called a "shebang"
# python scripts can be run using "python some_script" which uses the program 
# python to interpret the script specified. A script can also specify the
# program that should be used to interpret it using a shebang
# https://en.wikipedia.org/wiki/Shebang_%28Unix%29



print ("_" * 10) + " Welcome to to Mad Libs! " + ("_" * 10)
# python is neat how it lets you do math on strings

# python has a datatype called a list that allows you to store several variables
# lists use square brackets and can hold a variable number of varying types of 
# values
nouns = []
print  "Give me a noun:",
nouns.append(raw_input())
# using the append function we can append the output of raw_input to the list

# Some functions in python are overloaded. This means you can use the same function
# but with varying numbers and types of arguments
nouns.append(raw_input("Please give me another noun:"))
# inputting a string to raw_input makes that string the prompt

nouns.append(raw_input("And another noun:"))

# always use the most descriptive names you can
# make them short enough that you can remember them but this isn't jeopardy 
# you don't need to buy letters try not to shorten words unless it's either
# really necessary, a really common way to shorten the word
family_member    = raw_input("Please give me the name of a family member:")
# an example of a really common way to shorten a word: tmp = temporary
# There are only two problems hard problems in computer science
# cache invalidation, naming things and off by one errors

nouns.append(raw_input("Noun:"))

emotion    = raw_input("Name an emotion:")

nouns.append(raw_input("A person, place, or thing:"))

verb_1 = raw_input("Please give me a verb:")

verb_2 = raw_input("How about another verb?! :")

nouns.append(raw_input("Type a noun:"))

verb_3 = raw_input("I need a verb:")

verb_4 = raw_input("And quick! Type another verb here! :")

size   = raw_input("Enter a word you would use to describe 'size':")

verb_5 = raw_input("Please enter a verb:")

family_member_2  = raw_input("Alright I need another family member's name:")

# Lists may not seem like such a big improvement yet but imagine if you have a
# loop. It is much easier to append items to a list than to change the name
# of a variable on every iteration of a loop

for i in range(0, 2):
    nouns.append(raw_input("Another noun:"))

family_member_3  = raw_input("And to wrap this up, I need one more family member's name:")

print "+++++++++++++++++++++++++++++++"


# our noun list can now be accessed at different indices. Some languages count 
# beginning at 0 some start at 1. Python starts at 0
print """
The %s of Athena : Zeus, the %s of the Gods was married to a nice 
%s named Metis.  But one day, his %s told him that when Metic had 
a %s, it would overthrow him.  He was very %s.  Soon, when Metis 
was transforming into various %s, she %s into a dragonfly, and 
Zeus ate her.  Metis %s inside of Zeus' head for a very long 
time.  Eventually, she had her baby, and the %s began to grow 
older.  Metis taught her daughter about %s and %s.  One day, the 
inside of Zeus' head became too %s for both of them to live in, 
and Zeus got a headache.  He %s his %s and ask them to split his 
%s open to get out whatever was hurting him.  They split open his 
%s, and out came Metis' %s: the goddess Athena. 
""" % (nouns[0], nouns[1], nouns[2], family_member, nouns[3], emotion, nouns[4], verb_1, 
       verb_2, nouns[5], verb_3, verb_4, size, verb_5, family_member_2, nouns[6], 
       nouns[7], family_member_3)
# it is considered good practice to break lines longer than 80 characters
# this practice comes from old terminals being 80 characters wide. Which itself
# comes from punch cards being 80 characters wide. Usually only 72 punchcard
# holes would be used and the last 8 would be used for the sequence number
# https://en.wikipedia.org/wiki/Punched_card#IBM_80-column_punched_card_formats_and_character_codes
# note that the above line does not follow this practice because I have a 4k
# monitor and I dgaf

# You can also use functions that have been written by other people to do things
# to a list

print "All your nouns sorted!"
print sorted(nouns)
# sorted takes a list as an argument and returns a sorted list

# We can also iterate over a list using a loop
for noun in nouns:
    print "I'm iterating over the nouns list showing you each noun! " + noun

# note that I did this before by iterating over a range from 
# 0 to 2 including 0 excluding 2
# range is a function that returns a list of numbers between the start and end
# values It will be one of the most useful functions to you and I'd suggest
# playing around with it

# Here's a different way to make strings centered
print "You just played Mad Libs!".center(50, "_")

# Remember to never thank the user. They are the enemy.




