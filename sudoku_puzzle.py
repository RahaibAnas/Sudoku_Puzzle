import numpy as np

# #this is correct sudoku aray
arr = np.array([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
])

# this is not correct sudoku aray
# arr = np.array([
#     [5, 3, 4, 6, 7, 8, 9, 5, 2],
#     [6, 9, 2, 1, 9, 5, 3, 4, 8],
#     [1, 9, 8, 3, 4, 2, 5, 6, 7],
#     [8, 5, 9, 7, 6, 6, 4, 2, 3],
#     [4, 2, 6, 7, 5, 3, 7, 9, 1],
#     [7, 1, 3, 9, 2, 4, 8, 5, 6],
#     [9, 6, 1, 5, 7, 7, 2, 8, 4],
#     [2, 8, 7, 4, 1, 9, 6, 4, 5],
#     [9, 4, 5, 2, 8, 6, 1, 7, 9]
# ])

print("Sudoko puzzle")
def arr_uni(arr):
    x=0
    for i in range(len(arr)):
        if len(np.unique(arr[i])) == len(arr[i]) and len(np.unique(arr[:,i])) == len(arr[:,i]) :
             x +=1
    
    return x

def arr_sum(arr):
    i = 0
    z = 0
    while i != len(arr):
        a = 0
        while a !=len(arr[i]):
            out = arr[i:i+3,a:a+3]
            if np.sum(out) == 45:
                z+=1
            a+=3
        i+=3
    return z
    


def arr_sud( check1 = arr_uni(arr), check2 = arr_sum(arr)):    
    
    if check1 == 9 and check2 == 9:
        print("the array is sudoku")
    else:
        print("The is not suduko")

arr_sud()
