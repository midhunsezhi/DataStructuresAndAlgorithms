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

"""
negative binomial experiment
A negative binomial experiment is a statistical experiment that has the following properties:
The experiment consists of n repeated trials.
The trials are independent.
The outcome of each trial is either success with probabbility p or failure with q.
p is the same for every trial.
The experiment continues until x successes are observed.

If x is the number of experiments until the  success occurs, then X is a discrete random variable
called a negative binomial.

b*(x,n,p) = (n-1)C(x-1) *  p^x * q^(n-x)

negative binomial probability  meaning the probability of having x-1 successes after n-1 trials and
having x successes after n trials.

The geometric distribution is a special case of the negative binomial distribution that deals with
the number of Bernoulli trials required to get a success
(i.e., counting the number of failures before the first success)

g(n,p) = p * q^(n-1)
"""

"""
for a specified region P(l) is the Poisson probability,
which is the probability of getting exactly k successes
when the average number of successes is l.

P(l) = (l ^ k) * e ^ (-l) / k!

Special case: if expectation of poisson random variable is E[X],
E[X^2] = l + l^2
"""
