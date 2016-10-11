#!/usr/bin/python3.4

#Exercise: 11.2
#By: Robert A. Walters
#Created on: 1/29/15
#Program Description: A 4x4 matrix that sums up all elements
#in a major diagonal

def majorDiagonal(m):
        total = 0
        row=0
        column=0
        for row in range(0,len(m)):
                total+=m[row][column]
                row+=1
        return total
def main():
        m=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]] #4x4 matrix
        print("The sum of the elements in the diagonal is", majorDiagonal(m))
main()#runs it
#Shout out to Andrew Wiegand for helping me a lot