#!/usr/bin/python3.4

#Exercise: 11.6
#By: Robert A. Walters
#Created on: 2/4/16
#Program Description: A 2x2 matrices that multiplies

def getMatrix():
        matrix = [] #Create an empty matrix
        numberOfRows = 3
        numberOfColumns = 3
        for row in range(numberOfRows):
                matrix.append([]) #adds empty row
                for column in range(numberOfColumns):
                        value = eval(input("Enter a value and press Enter: "))
                        matrix[row].append(value)

        return matrix


c = [0,0,0],[0,0,0],[0,0,0]#empty matrix

def multiMatrix(a, b):
        for i in range(len(a)):#Goes through column a
                for j in range(len(b[0])):#Goes through column b
                        for k in range(len(b)):#Goes through row b
                                c[i][j] += a[i][k] * b[k][j]
        return a, b
def main():
        a = getMatrix()#Make matrix a
        b = getMatrix()#Makes matrix b
        print("The first matrix is: ", a)
        print("The second matrix is: ", b)
        multiMatrix(a,b)
        for r in c:
                print(r)
main()#runs it

#thanks to frankie formcola

