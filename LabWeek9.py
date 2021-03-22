#define a matrix full of zeros loop:
def makeMatrixLoop(n, m):
    l1 = [0] * n
    for i in range (n):
        l1[i] = [0] * m
    return l1

print(makeMatrixLoop(3, 4))

#define matrix full of zeros list comprehension:
def makeMatrixComprehension(n, m):
    l = [[0 for columns in range(n)] for rows in range(m)]
    return l

print(makeMatrixComprehension(3, 4))

#print the matrix:
def printMatrix(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end = " ")
        print()

matrix = makeMatrixComprehension(3, 4)
printMatrix(matrix)

#accessing items in a matrix
myMatrix = [[1, 2, 3], ["a", "b", "c"], ["red", "yellow", "blue"]]

#print the first list in the myMatrix
#print the letter 3 using myMatrix
#print the "red" using myMatrix
#print the list of characters using myMatrix
#change the color yellow in the third list to "purple"

#Create the following matrix using a for loop:
#[[1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]]

#appending and extending arrays
colors = [["red", "yellow", "blue"], ["orange", "green", "purple"]]
colors.append(["white", "gray", "black"])
print(colors)

evenOdd = [[1, 3, 5, 7], [2, 4, 6, 8, 10]]
evenOdd[0].extend([9])
print(evenOdd)
