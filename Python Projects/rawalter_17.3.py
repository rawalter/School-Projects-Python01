#!/usr/bin/python3.4
#Exercise: 17.3
#By: Robert A. Walters
#Created on: 4/08/16
#Program Description: A mini heap
from class_heap import Heap

def heapSort(list):
    heap = Heap() # Create a Heap

    # Add elements to the heap
    for v in list:
        heap.add(v)

    # Remove elements from the heap
    for i in range(len(list)):
        list[len(list) - 1 - i] = heap.remove()

def main():
    list = [-44, -5, -3, 3, 3, 1, -4, 0, 1, 2, 4, 5, 53]
    heapSort(list)
    for v in list:
        print(str(v) + " ", end = " ")

main()