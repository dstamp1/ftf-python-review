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

## Additional resources for coding challenges
# https://adventofcode.com/
# https://projecteuler.net/
