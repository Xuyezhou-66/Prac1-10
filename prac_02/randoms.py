import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

#What did you see on line 1? #Generates an integer random number from 5 to 20
#What was the smallest number you could have seen, what was the largest? 6

#What did you see on line 2? #Generates a random a integer with an interval of 2 from 3
#What was the smallest number you could have seen, what was the largest? 3 9
#Could line 2 have produced a 4? No

#What did you see on line 3? #Generate random floating point numbers between 2.5 and 5.5
#What was the smallest number you could have seen, what was the largest? 2.5-5.5

#Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1,100))
