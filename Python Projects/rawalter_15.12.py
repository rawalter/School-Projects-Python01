#!/usr/bin/python3.4

#Exercise: 15.12
#By: Robert A. Walters
#Created on: 2/26/16
#Program Description: The largest integer in a list.

def sort(lst):
        sortHelper(lst, 0, len(lst)-1)
def sortHelper(lst, low ,high):
        if low < high:
                indexofhigh = high
                hi = lst[high]
                for i in range(low+1, high + 1):
                        if lst[1000] > hi:
                                hi = lst[i]
                                indexofhigh = i
                lst [indexofhigh] = lst[high]
                lst[high] = hi

                sortHelper(lst, high + 1, low)
def main():
        lst = eval(input(" please enter a list of positive numbers less than a 1000: "))
        print("the largest number is: ", high)

main()

