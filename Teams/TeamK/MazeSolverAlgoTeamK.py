
"""
This class is the template class for the Maze solver
"""

import sys
from math import sqrt
import numpy
import queue

class MazeSolverAlgoTeamK:

    EMPTY = 0       # empty cell
    OBSTACLE = 1    # cell with obstacle / blocked cell
    START = 2       # the start position of the maze (red color)
    TARGET = 3      # the target/end position of the maze (green color)

    def __init__(self):
        self.dimCols =0
        self.dimRows=0
        self.startCol=0
        self.startRow=0
        self.endCol=0
        self.endRow=0
        self.grid=[[]]
        print("Klasse vorhanden")

    # Setter method for the maze dimension of the rows
    def setDimRows(self, rows):
        self.dimRows=rows

    # Setter method for the maze dimension of the columns
    def setDimCols(self, cols):
        self.dimCols=cols
        
    # Setter method for the column of the start position 
    def setStartCol(self, col):
        self.startCol =col

    # Setter method for the row of the start position 
    def setStartRow(self, row):
        self.startRow = row

    # Setter method for the column of the end position 
    def setEndCol(self, col):
        self.endCol=col
        
    # Setter method for the row of the end position 
    def setEndRow(self, row):
        self.endRow = row

    # Setter method for blocked grid elements
    def setBlocked(self,row ,col):
        self.grid[row][col]=self.OBSTACLE

    # Start to build up a new maze
    # HINT: don't forget to initialize all member variables of this class (grid, start position, end position, dimension,...)
    def startMaze(self, columns=0, rows=0):
        if rows == 0 and columns == 0:
            self.startCol = 0 
            self.startRow = 0 
            self.endCol = 0 
            self.endRow = 0 

        self.grid=[[]]          


        if rows>0 and columns>0:
            self.grid = numpy.empty((rows,columns), dtype =int)
            for i in range(rows):
                for j in range(columns):
                    self.grid[i][j]=self.EMPTY

        self.printMaze()
        #HINT: populate grid with dimension row,column with zeros

    # Define what shall happen after the full information of a maze has been received
    def endMaze(self):
        self.grid[self.startRow][self.startCol] = self.START
        self.grid[self.endRow][self.endCol]= self.TARGET
        # HINT: did you set start position and end position correctly?

    # just prints a maze on the command line
    def printMaze(self):
        print("Array ausgeben")
        print(self.grid)

    # loads a maze from a file pathToConfigFile
    def loadMaze(self,pathToConfigFile):
        self.grid = numpy.loadtxt(pathToConfigFile,delimiter=',',dtype=int)
        print(self.grid)
        self.dimRows = self.grid.shape[1]
        self.dimCols = self.grid.shape[0]


        start = numpy.where(self.grid ==2)
        self.startRow = start[0][0]
        self.startCol = start[1][0]

        ende = numpy.where(self.grid ==3)
        self.endRow = ende[0][0]
        self.endCol = ende[1][0]

        print(self.dimRows, self.dimCols, self.startRow, self.startCol, self.endRow, self.endCol)        
    
        

    # clears the complete maze 
    def clearMaze(self):
        self.dimCols = 0
        self.dimRows = 0
        self.startMaze(0,0)

    # Decides whether a certain row,column grid element is inside the maze or outside
    def isInGrid(self,row,column):
        if row < 0:
            return False

        if column <0:
            return False

        if row >= self.grid.shape[1]:
            return False

        if column >= self.grid.shape[0]:
            return False  
        return True


    # Returns a list of all grid elements neighboured to the grid element row,column
    def getNeighbours(self,row,column):
        neighbours=[]

        if self.isInGrid(row, column) == False:
            return neighbours

        if self.grid[row,column]==self.OBSTACLE:
            return neighbours
        
        nextRow= row +1
        if (self.isInGrid(nextRow, column)) is True and (self.grid[nextRow][column] != self.OBSTACLE):
            neighbours.append([nextRow,column])

        lastRow = row -1
        if (self.isInGrid(lastRow, column)) is True and (self.grid[lastRow][column] != self.OBSTACLE):
            neighbours.append([lastRow,column])

        nextCol = column +1
        if (self.isInGrid(row,nextCol)) is True and (self.grid[row][nextCol]!= self.OBSTACLE):
            neighbours.append([row,nextCol])

        lastCol = column -1
        if (self.isInGrid(row,lastCol)) is True and (self.grid[row][lastCol]!= self.OBSTACLE):
            neighbours.append([row,lastCol])

        return neighbours
        # TODO: Add a Unit Test Case --> Very good example for boundary tests and condition coverage

    # Gives a grid element as string, the result should be a string row,column
    def gridElementToString(self,row,col):
        result = ""
        result += str(row)
        result += ","
        result += str(col)
        return result
    
    # check whether two different grid elements are identical
    # aGrid and bGrid are both elements [row,column]
    def isSameGridElement(self, aGrid, bGrid):
        if (aGrid[0] == bGrid[0] and aGrid[1] == bGrid[1]):
            return True
            
        return False


    # Defines a heuristic method used for A* algorithm
    # aGrid and bGrid are both elements [row,column]
    def heuristic(self, aGrid, bGrid):
        # TODO: this is you job now :-)
        # HINT: a good heuristic could be the distance between to grid elements aGrid and bGrid
        pass

    # Generates the resulting path as string from the came_from list
    def generateResultPath(self,came_from):
        
        # HINT: this method is a bit tricky as you have to invert the came_from list (follow the path from end to start)
        pass

   #############################
    # Definition of Maze solver algorithm
    #
    # implementation taken from https://www.redblobgames.com/pathfinding/a-star/introduction.html
   ##############################

    def breadthFirstSearch(self):

        start = [self.startRow, self.startCol]
        frontier = queue.Queue()
        frontier.put(start)
        startKey = self.gridElementToString(self.startRow, self.startCol)
        came_from ={}
        came_from[startKey] = None

        while not frontier.empty():
            current = frontier.get()

            for next in self.getNeighbours(current[0],current[1]):
                nextKey = self.gridElementToString(next[0], next[1])#next, da current bereits in String gespeichert
            
                if nextKey not in came_from:
                    frontier.put(next)
                    came_from[nextKey]=current
            #print(came_from)

        current = self.gridElementToString(self.endRow,self.endCol)
        path=[]

        while current != startKey:
            if current not in came_from:
                print("Pfad konnte nicht gefunden werden")
                break
            elif current in came_from:
                path.append(current)
                current = came_from[current]
                current = self.gridElementToString(current[0],current[1])
            

        path.append(startKey)
        path.reverse()
        print(path)
        
 

    def myMazeSolver(self):
        # TODO: this is you job now :-)
        pass

    # Command for starting the solving procedure
    def solveMaze(self):
        return self.myMazeSolver()


if __name__ == '__main__':
    mg = MazeSolverAlgoTeamK()


    # HINT: in case you want to develop the solver without MQTT messages and without always
    #       loading new different mazes --> just load any maze you would like from a file

    mg.loadMaze("C:\\Users\\Kora\\Desktop\\Kora\\Privat\\Furtwangen\\CodeCamp\\MazeRunner\\MazeExamples\\maze3.txt")
    
    versuch= mg.getNeighbours(0,2)
    print(versuch)

    v2 = mg.isSameGridElement([0,0],[0,0])
    print(v2)

    mg.breadthFirstSearch()
    #solutionString = mg.solveMaze()
    #print(solutionString)
   
