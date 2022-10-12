#student name: Kevin Peng
#student number: 94742293

import threading
from tkinter import E

# implement mergesort
def mergesort(array):
  # base case is when array is len 0 or 1
  if len(array) <= 1:
    return array

  # get center index
  center = len(array) // 2

  # split array using center index and call mergesort recursively on both arrays
  leftArray = mergesort(array[:center])
  rightArray = mergesort(array[center:])

  return mergeStepHelper(leftArray, rightArray)

# IMPORTANT: Assumes leftArray and rightArray are sorted already
# does not mutate left and right arrays
def mergeStepHelper(leftArray, rightArray):
  # sorted merged array
  sortedMerge = []

  # used to keep track of current index when adding to sortedMerge array from leftArray and rightArray
  leftIndex = 0
  rightIndex = 0

  # while both arrays are not empty, add lowest current value from either array using current indices
  while leftIndex < len(leftArray) and rightIndex < len(rightArray):
    if leftArray[leftIndex] < rightArray[rightIndex]:
      sortedMerge.append(leftArray[leftIndex])
      leftIndex += 1
    else:
      sortedMerge.append(rightArray[rightIndex])
      rightIndex += 1
  
  # whatever is left in either leftArray or rightArray starting from the remaining indices will be sorted and greater than our sortedMerge array
  sortedMerge.extend(leftArray[leftIndex:])
  sortedMerge.extend(rightArray[rightIndex:])

  return sortedMerge


def sortingWorker(firstHalf: bool) -> None:
    """
       If param firstHalf is True, the method
       takes the first half of the shared list testcase,
       and stores the sorted version of it in the shared 
       variable sortedFirstHalf.
       Otherwise, it takes the second half of the shared list
       testcase, and stores the sorted version of it in 
       the shared variable sortedSecondHalf.
       The sorting is ascending and you can choose any
       sorting algorithm of your choice and code it.
    """
    center = len(testcase) // 2

    if firstHalf:
      global sortedFirstHalf
      sortedFirstHalf = mergesort(testcase[:center])
    else:
      global sortedSecondHalf
      sortedSecondHalf = mergesort(testcase[center:])

def mergingWorker() -> None:
    """ This function uses the two shared variables 
        sortedFirstHalf and sortedSecondHalf, and merges/sorts
        them into a single sorted list that is stored in
        the shared variable sortedFullList.
    """
    pass #to Implement

if __name__ == "__main__":
    #shared variables
    testcase = [8,5,7,7,4,1,3,2]
    sortedFirstHalf: list = []
    sortedSecondHalf: list = []
    SortedFullList: list = []
    
    #to implement the rest of the code below, as specified 


    #as a simple test, printing the final sorted list
    print("The final sorted list is ", SortedFullList)