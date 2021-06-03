import random, Clock

#first make 3 arrays/lists are made, which are going to get sorted
best = [1, 2, 3, 4, 5, 6]
average = [4, 2, 3, 1, 6, 5]
worst = [6, 5, 4, 3, 2, 1]

#now the sorting-function is defined
def sort(arr):
    for run in range(len(arr)-1):
        corrected = False
        for i in range(0, len(arr) -1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                corrected = True
    return arr

#making another array, which is big, though
bigList = [i for i in range(1, 30001)]
random.shuffle(bigList)
#actually print and sort the arrays
print(sort(best))
print(sort(average))
print(sort(worst))

print("The big list follows:")
c = Clock.Clock()
print(sort(bigList))

c.measureTime();