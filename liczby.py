import itertools
from operator import itemgetter
import operator
import functools
import math

numbers = []

for i in range(5):
    print("Enter number no " + str(i+1))
    given_number = int(input())
    numbers.append(given_number)

print("Chosen numbers:")
print(numbers)


index_list = list(itertools.combinations([0,1,2,3,4], 3))

first_list = []
second_list = []

#locate elements that are not in index, prepare two list consist accordingly of 3 and 2 elements
for ix in index_list:
    not_in_ix = list(set([0,1,2,3,4]) - set(ix))
    first_list.append(itemgetter(*ix)(numbers))
    second_list.append(itemgetter(*not_in_ix)(numbers))


def sum(a, b):
    return a+b

diff_list = []

#check if sum is positive
for i in range(10):
    curr_sum = functools.reduce(sum, first_list[i]) - functools.reduce(sum,second_list[i])
    print("Difference is " + str(curr_sum))
    if curr_sum <= 0:
        print("Difference is negative or equals 0.")
        exit()
    else:
        diff_list.append(curr_sum)

print("Differences are correct!")

#check multiplication of differences vs square of given numbers
final_check_diff = functools.reduce(operator.mul, diff_list)
final_check_numbers =  int(math.pow(functools.reduce(operator.mul, numbers), 2))

if final_check_diff <= final_check_numbers:
    print("Multiplied differences give " + str(final_check_diff) + ". Squared and multiplied numbers give " + str(final_check_numbers) + ". Multiplication of all differences is equal or smaller than squared and multiplicated given numbers.")
else:
    print("Chosen numbers don't satisfy excercise conditions")



