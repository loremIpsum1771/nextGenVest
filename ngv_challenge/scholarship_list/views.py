from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser


class ScholarshipView(APIView):
    """
    View which accepts a JSON object and returns a JSON Response
    Can accept POST requests with JSON content
    """
    parser_classes = (JSONParser,)
    def post(self, request):
        """
        Take a JSON object that contains a 2D Array of scholarships
        and return a JSON response of the best 11 scholarships and their total product
        """
        matrix = request.data["data"]
        maxProduct, maxList = self.maxPathProduct(matrix, 11)
        return Response({'sequence': maxList, 'total':maxProduct})

    def maxPathProduct(self,matrix, maxLen):
        """
        Take a 2D Array of ints
        and return the largest Product of list of ints of length maxLen
        and the product of the list integers
        """
        maxProduct = -1
        maxList = []
        if len(matrix) == 0 or len(matrix) < maxLen and len(matrix[0]) < maxLen:
            return maxProduct, maxList
        numRows = len(matrix)
        numCols = len(matrix[0])
        numDiagonals = numRows + numCols -1
        #list containing protocol for iterating through lines based on direction
        directions = [(1, 0, numCols), (0, 1, numRows), (1, 1, numDiagonals)]
        for i in range(len(directions)):
            numLines = directions[i][2] #Set numLines based on the current direction
            for line in range(0, numLines):
                pathProduct = 1
                pathLen = 0
                if i == 0: #iterate through columns
                    headRow = 0
                    headCol = line
                elif i ==1:#iterate through rows
                    headCol = 0
                    headRow = line
                else:#iterate through diagonals
                    headRow = 0 if line >= numRows else line
                    headCol = line-numRows if line >= numRows else 0 
                tailRow = headRow
                tailCol = headCol
                pathList = []
                while headRow < numRows  and headCol < numCols:
                    pathList.append(matrix[headRow][headCol])
                    pathProduct *= matrix[headRow][headCol]
                    pathLen += 1
                    if pathLen > maxLen: 
                        pathProduct /= matrix[tailRow][tailCol]
                        pathList = pathList[1:]
                        tailRow += directions[i][0]
                        tailCol += directions[i][1]
                    if pathProduct > maxProduct:
                        maxProduct = pathProduct
                        maxList = pathList
                    headRow += directions[i][0]
                    headCol += directions[i][1]
        return maxProduct, maxList


    
