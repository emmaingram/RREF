# Emma Ingram
# CSCI 101 - Section F
# Create Project
# This program takes an mxn matrix and puts it in reduced row echelon form.

def get_matrix():
    file = input('Input file containing your matrix:\nFILE> ')
    matrixF = open(file, "r")
    matrix = [[int(n) for n in line.split()] for line in matrixF] #store matrix as 2D list
    return matrix

def rref(M):
    m = len(M) #number of rows
    n = len(M[0]) #number of columns

    printMatrix(M)

    #loop to go through matrix
    current = 0
    for r in range(m):
        if current >= n:
            return
        i = r
        while M[i][current] == 0:
            i += 1
            if i == m:
                i = r
                current += 1
                if n == current:
                    return
        M[i],M[r] = M[r],M[i] #swap rows
        if i != r:
            print('\nSwap rows', i+1, 'and', r+1)
            printMatrix(M)
        old_val = M[r][current]
        if round(old_val, 1) != 1.0:
            M[r] = [(round(cur_val/float(old_val),1)+0.0) for cur_val in M[r]] #make pivots 1
            if old_val == int(old_val): old_val = int(old_val) #get rid of redundant 0's
            print('\nMultiply R', r+1, ' by 1/', old_val, sep='')
            printMatrix(M)
        for i in range(m): #make entries below pivots 0
            if i != r:
                old_val = M[i][current]
                change = -old_val*M[r][current]+0.0
                if change == int(change): change = int(change)
                if change != 0.0:
                    M[i] = [(round(cur - old_val*pivot, 1)+0.0) for pivot,cur in zip(M[r],M[i])]
                    print('\nAdd ', change, ' times R', r+1, ' to R', i+1, sep='')
                    printMatrix(M)
        current += 1
    print()
    

def printMatrix(M):
    print()
    for row in M:
        for col in row:
            if col == int(col): col = int(col)
            print('%5s' %str(col), end=' ')
        print()

print('       Reduced Row Echelon Form of a Matrix       ')
print('--------------------------------------------------')

rref(get_matrix())
