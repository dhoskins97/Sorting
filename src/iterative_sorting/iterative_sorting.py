# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # initialize the dynamic starting point at the first index
    DSP = 0

    # run the sorting code until the dynamic starting point reaches the final index, at which case we have accomplished what we meant
    while (DSP < len(arr)):

        # at the beginning of each iteration, make the smallest value's index the same as our dynamic starting point for comparison
        smallestValue = DSP

        # loop through each element of the "unsorted" portion, aka everything at our starting point and after
        for i in range(DSP, len(arr)):

            # if we encounter a smaller value than the one we started with, it becomes the new smallest
            if arr[i] < arr[smallestValue]:
                smallestValue = i

        # swap the smallest value with the value at our starting point, adding the value to our "sorted array"
        arr[smallestValue], arr[DSP] = arr[DSP], arr[smallestValue]

        #increment the starting point for the next iteration, so we don't try to sort the portion of the array that's already sorted
        DSP += 1

    return arr



# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # initialize a dynamic starting point at the beginning of the array
    needsToRun = True

    # keep track of how many switches are made, and run this code until a switch is NOT made
    while (needsToRun):
        DSP = 0
        switchCounter = 0
        while (DSP <= len(arr) - 2):
            # check arr[DSP] and arr[DSP + 1] and if they are out of order, switch them and increment switch counter
            if arr[DSP] > arr[DSP + 1]:
                arr[DSP], arr[DSP + 1] = arr[DSP + 1], arr[DSP]
                switchCounter += 1
            # increment our starting point
            DSP += 1
        if switchCounter < 1:
            needsToRun = False
    return arr




# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr