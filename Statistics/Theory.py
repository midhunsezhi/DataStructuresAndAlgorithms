""" quartiles 3 points q1, q2 and q3 in a data, such that q2 is median of data, 
    q1 is median of first half and q3 is median of second half. 

    Inter Quartile Range is q3-q1.
"""

"""
Mean m = sum of all elements / number of elements
variance = (sum of squares of distances of each element from mean) / number of elements 
Standard Deviation : math.sqrt(variance)
"""

"""
Conditional probability:
P(A ^ B) = P(B | A) * P(A)

Bayes' Theorem:

P(A | B) = (P(B | A) * P(A)) / P(B)

P(B) = P(B | A) * P(A) + P(B | A') * P(A')

"""

"""
Binomial Distribution:

The number of sucesses is x 
The number of trials is n 
The probability of success of 1 trail is p 
The probability of failute of 1 trial is q = 1 - p 
b(x, n, p) is the probability of having exactly x successes out of n trials. 

Then Binomial distribution is given by:

b(x, n, p) = nCx * p^x * q^(n-x)

Cumulative Probability:
if F(x) = P(X < x):

    P(a < X <= b) = F(b) - F(a)

"""