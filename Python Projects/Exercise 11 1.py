#!/usr/bin/python3.4
# Exercise:11.1
#By:Robert A. Walters
#Created on: 1/22/16
#Program Descripition: add the sum of a 3 by 4 matrix
def sumColumn(m, columnIndex):#required for it to work
        for column in range(columnIndex):
                total = 0
                for row in range(len(m)):
                        total += m[row][column]
                print("Sum for column",column,"is",total)

def main():
        m = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]#the list for the matrix
        columnIndex = len(m[0])
        print(m)
        sumColumn(m,columnIndex)
main() #runs it
# Shout out to Anthony Wiegand for helping me
