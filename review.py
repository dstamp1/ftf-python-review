### This python file has some question to help you review key concepts
# Each question can be completed independently
# They are somewhat listed in difficulty order

import data

#1 - finish writing a function that repeats a word x times where x is the length
## of the word
# Examples
## 'hi' => 'hihi'
## 'bye' => 'byebyebye'

def word_repeater(word):
    return ''

#2 - finish writing a function that converts a word into Pig Latin
## For words that begin with consonant sounds, all letters before the initial
# vowel are placed at the end of the word sequence. Then, "ay" is added,
# Examples
## "pig" => "igpay"
## "latin" => "atinlay"

# A list of the vowels (data.vowels_list) is available in data.py

def pig_latinzer(word):
    return ''

#3 - finish writing a function that checks if a number is a multiple of 3 or 5
# Examples
## 3 => True
## 5 => True
## 8 => False
## 15 => True

def multiple_of_three_or_five(number):
    return ''

#4 Use a loop to determine the sum of all the multiples of 3 or 5 below 1000.
for i in range(1000):
    ## business logic
    result = ''
print(result)


#5 A mortgage calculator function
## A mortgage is an example of an amortized loan. Amoritized loans pay off principal (the borrowed amount)
### and the interest with a fixed incremental payment.
## A typical mortgage is amoritized monthly for 30 years (n = 360 total payments)
## The monthly payment, A, is based on the initial principal, P, the number of payments, n, and
## the annual interest rate divided by 12 to determine the monthly rate, r
## As a formula,
## A = P*(1+r)^n / ( (1+r)^n - 1)
# Finish writing the function
def mortgage_payment_calculator(P, n, r):
    return ''

#6 Use a loop to count the number of times you would write the number 7 if you
## wrote down all of the numbers between 0 and 100
## Hint: when you write the number 77, that would be two 7s

for i in range(100):
    #business logic
    result = ''
print(result)

#7 Given an integer n, write a function that results the absolute difference between n and 21
## unless n > 21, then result double the difference.

def diff_from_21(number):
    return ''

print(diff_from_21(19)) # =2
print(diff_from_21(10)) # =11
print(diff_from_21(21)) # =0

#8 The Collatz Conjecture
## The Collatz conjecture is a conjecture in mathematics that concerns sequences
## defined as follows: start with any positive integer n. Then each term is obtained
## from the previous term as follows: if the previous term is even, the next term
## is one half of the previous term. If the previous term is odd, the next term
## is 3 times the previous term plus 1. The conjecture is that no matter what
## value of n, the sequence will always reach 1

# The following function applies the rule one time to a number
def collatz_one_step(number):
    if number == 1:
        return 1
    if number % 2 == 0:
        return number / 2
    if number % 2 == 1:
        return 3*number+1

# A while loop lets us repeat a process indefinitely until a condition is met
# use a while loop to apply the collatz_one_step function to count how many steps
# it takes to take an arbitrary number to 1 (also known as stopping time). Your
# function will return the stopping time.

def collatz_step_count(number):
    while number != 1:
        #business logic
        return ''
    return ''

## Challenges:
# Determine the number less than 100 with the largest stopping time.

# Write a new function that returns the list of numbers from each step of following
# the collatze_one_step

#9 Forensic Accounting
## Due to the decimal nature of number systems, a "naturally" occuring data set
## obeys Benford's law. If we take a collection of numbers which span a few orders
## of magnitude and count up the frequency of the digits 1-9 in the largest placevalue,
## we expect there to be more 1s than 9s. (approximately 30% of the leading digits should
## be 1 and 5% should be 9s)

## Write a function to analyze the following two datasets to determine the frequency
## of 1s, 2s, 3s, etc. in the largest placevalue. See if you can determine which
## dataset is "natural" and which is likely tampered with.
benford_dataset_one = data.benford_dataset_one
benford_dataset_two = data.benford_dataset_two




## Additional resources for coding challenges
# https://adventofcode.com/
# https://projecteuler.net/
