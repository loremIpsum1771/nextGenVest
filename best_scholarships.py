def maxPathProduct(matrix, maxLen):
    numRows = len(matrix)
    numCols = len(matrix[0])
    maxProduct = -1
    maxList = []
    
    for dir in range(1,4):
        if dir == 1:
            numLines = numCols
        elif dir == 2:
            numLines = numRows
        elif dir == 3:
            numLines = numRows + numCols -1
        
        for line in range (0,numLines):
            pathProduct = 1
            pathLen = 0
            if dir == 1:
                headRow = 0
                headCol = line
            elif dir ==2:
                headCol = 0
                headRow = line
            elif dir == 3:
                headRow =  0 if line  >= numRows else line
                headCol =  line-numRows if line  >= numRows else 0
            tailRow = headRow
            tailCol = headCol
            pathList = []
            while headRow < numRows  and headCol < numCols:
                pathList.append(matrix[headRow][headCol])
                pathProduct *= matrix[headRow][headCol]
                pathLen+=1
                if pathLen > maxLen:
                    pathProduct /= matrix[tailRow][tailCol]
                    pathList = pathList[1:]
                    if dir== 1:
                        tailRow += 1
                    elif dir == 2:
                        tailCol += 1
                    elif dir == 3:
                        tailCol += 1
                        tailRow += 1
                if pathProduct > maxProduct:
                    maxProduct = pathProduct
                    maxList = pathList
                if dir== 1:
                        headRow += 1
                elif dir == 2:
                    headCol += 1
                elif dir == 3:
                    headCol += 1
                    headRow += 1


    return maxProduct, maxList

matrix = [
    [1,  2,  3,  4,  5],
    [1,  1,  2,  3,  5],
    [3,  4,  5,  5,  5],
    [3,  4,  5, 9,  5],
    [1,  1,  5,  5, 25],
];
