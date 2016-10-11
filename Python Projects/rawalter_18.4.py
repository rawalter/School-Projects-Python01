#!/usr/bin/python3.4
#Robert A. Walters
#Thanks to kyle Carr

from LinkedList import LinkedList
from LinkedList import LinkedListIterator
from LinkedList import Node

def main():
        list = LinkedList()

        list.add("USA")
        list.add("Canada")
        list.add("Antarctica")
        list.add("Russia")
        list.add("Asia")
        list.add("Australia")
        list.add("South America")

        iterator = iter(list)

        Next = True
        lst = []
        lst2 = []

        while Next:
                temp, temp2 = next(iterator)
                if temp == None:
                        Next = False
                else:
                        lst.append(temp)
                        lst2.append(temp2)

        print(lst)
        print(lst2)

main()
