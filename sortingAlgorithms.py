class sortAlgs():
    def __init__(self,sort):
        self.sort = sort

    def insertionSort(self):
        pass


    def bubbleSort(self):
        sort = self.sort
        # print(sort)
        length = len(sort)-1
        for i in range(-1, length, 1): # Here start from -1 because of the ranges

            for j in range(length, i+1, -1):
                # print(j)
                if sort[j] < sort[j-1]:
                    temp = sort[j]
                    sort[j] = sort[j-1]
                    sort[j-1] = temp

        return sort


def displayProcess():
    pass


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import tinker as tk 
    toBeSorted = [10,3,2,4,5,9,6,7,1]
    sa = sortAlgs(toBeSorted)

    # sa.__init__(sa,toBeSorted)
    sorted = sa.bubbleSort()
    for i in sorted:
        print (i)
