class sortAlgs():
    def __init__(self, sort):
        self.sort = sort
        self.counter = 0
    def insertionSort(self):
        sorted = []
        sort = self.sort
        length = len(self.sort)
        sorted.append(sort[0])
        holePosition = 0
        valueToInsert =-1

        for i in range(1,length):
            valueToInsert = sort[i]
            holePosition = i
            while holePosition > 0 and sort[holePosition-1] > valueToInsert:
                print("Insertion :)")
                print("Before insertion : ")
                displayList(sort)
                sort[holePosition] = sort[holePosition-1]
                holePosition = holePosition-1
                print("After Insertion : ")
                displayList(sort)
            sort[holePosition] = valueToInsert
        return sort

    def bubbleSort(self):
        count = 0
        sort = self.sort
        # print(sort)
        length = len(sort) - 1
        for i in range(-1, length, 1):  # Here start from -1 because of the ranges

            for j in range(length, i + 1, -1):
                # print(j)
                if sort[j] < sort[j - 1]:
                    print("Swapping :)")
                    print("Before Swapping : ")
                    count +=1
                    displayList(self.sort)
                    temp = sort[j]
                    sort[j] = sort[j - 1]
                    sort[j - 1] = temp
                    print("After Swapping : ")
                    displayList(self.sort)
        print("The number of swap is : " + str(count))
        return sort
"""
Here is a basic version of HEAP sort
"""
    def heapSort(self):
        heap = []
        
    


"""
Basic version for displaying 
"""
def displayList(li):
    for i in range(len(li)):
        print("This is " + str(i) + "th elements : " + str(li[i]))

"""
Want to use poker card to display what is going on 
step by step
can be done afterwards
"""
def displayProcess():
    pass


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import tkinter as tk
    import numpy as np
    import random as rd

    toBeSorted = [10, 8,3, 2, 4, 5, 9, 6, 7, 1]
    sa = sortAlgs(toBeSorted)


    # sa.__init__(sa,toBeSorted)
    sorted_bubble = sa.bubbleSort()
    sorted_insertion = sa.insertionSort()
    for i in sorted_insertion:
        print(i)

