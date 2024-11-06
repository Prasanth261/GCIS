# lyrics="""Find your dreams come true
# And I wonder if you know
# What it means, what it means
# And I wonder if you know
# What it means, what it means
# And I wonder if you know
# What it means to find your dreams
# I've been waiting on this my whole life
# These dreams be waking me up at night (night, night)
# (And I wonder) you say I think I'm never wrong (wrong, wrong)
# (And I wonder) you know what, maybe you're right, aight?
# And I wonder if you know
# What it means, what it means
# And I wonder if you know
# What it means to find your dreams
# word
# (And I wonder) do you even remember what the issue is?
# You just trying to find where the tissue is
# You can still be who you wish you is
# It ain't happen yet
# And that's what the intuition is (and I wonder)
# When you hop back in the car
# Drive back to the crib
# Run back to their arms
# The smokescreens
# The chokes and the screams
# You ever wonder what it all really mean
# And I wonder if you know
# What it means, what it means
# And I wonder if you know
# What it means to find your dreams
# and I'm back on my grind
# A psychic read my lifeline
# Told me in my lifetime
# My name would help light up the Chicago skyline
# And that's what I'm (and I wonder)
# Seven o'clock, that's primetime
# Heaven'll watch, God calling from the hotlines
# Why he keep giving me hot lines?
# I'm a star, how could I not shine? (And I wonder)
# How many ladies in the house (if you know)
# How many ladies in the house without a spouse (what it means)
# Something in your blouse got me feeling so aroused (what it means)
# What you about? (And I wonder)
# On that independent shit (if you know)
# Trade it all for a husband and some kids (what it means)
# You ever wonder what it all really mean? (To find your dreams come true)
# You ever wonder if you'll find your dreams"""
lyrics="Hey this is a test"

def slices(string):
    list1=[]
    list1.append(string)
    start=0
    end=0
    count=0
    list2=[]
    for i in string:
        if i.isalnum():
            start+=1
        else:
            if count==0:
                list2.append(string[:start])
                end=start+1
                count+=1
            else:
                list2.append(string[end:start+1])
                end=start
    print(len(list2))
    print(len(string))
    print(list2)
slices(lyrics)

    

