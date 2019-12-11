# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    counter = 0
    while (len(arrA) > 0 and len(arrB) > 0):
        
        if arrA[0] < arrB[0]:
            # print(f"{arrA[0]} is less than {arrB[0]}")
            merged_arr[counter] = arrA[0]
            arrA.remove(arrA[0])
        elif arrB[0] < arrA[0]:
            # print(f"{arrB[0]} is less than {arrA[0]}")
            merged_arr[counter] = arrB[0]
            arrB.remove(arrB[0])
        counter += 1
    
    while (len(arrA) > 0):
        # print(f"arrA still has values, adding {arrA[0]} to merged array")
        merged_arr[counter] = arrA[0]
        arrA.remove(arrA[0])
        counter += 1
    
    while (len(arrB) > 0):
        # print(f"arr still has values, adding {arrA[0]} to merged array")        
        merged_arr[counter] = arrB[0]
        arrB.remove(arrB[0])
        counter += 1
    
    return merged_arr




# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr

    retArr1 = []
    retArr2 = []
    for i in range(0, int(len(arr) / 2)):
        retArr1.append(arr[i])
    for i in range(int(len(arr) / 2), len(arr)):
        retArr2.append(arr[i])
    
    retArr1 = merge_sort(retArr1)
    retArr2 = merge_sort(retArr2)
    # print(f"arr1 = {retArr1}, arr2 = {retArr2}")

    return merge(retArr1, retArr2)

arr3 = [9, 3, 2, 4]
print(merge_sort(arr3))











# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
