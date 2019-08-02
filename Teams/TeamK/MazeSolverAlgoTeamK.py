
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
        print("dimRows = " , self.dimRows)

    # Setter method for the maze dimension of the columns
    def setDimCols(self, cols):
        self.dimCols=cols
        print("DimCols =", self.dimCols)
        
    # Setter method for the column of the start position 
    def setStartCol(self, col):
        self.startCol =col
        print("startCol=", self.startCol)

    # Setter method for the row of the start position 
    def setStartRow(self, row):
        self.startRow = row
        print("startRow= ",self.startRow)

    # Setter method for the column of the end position 
    def setEndCol(self, col):
        self.endCol=col
        print("endCol=", self.endCol)
        
    # Setter method for the row of the end position 
    def setEndRow(self, row):
        self.endRow = row
        print("endRow=", self.endRow)

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
        # check whether a function numpy.loadtxt() could be useful
        # TODO: this is you job now :-)
        pass

    # clears the complete maze 
    def clearMaze(self):
        self.dimCols = 0
        self.dimRows = 0
        self.startMaze(0,0)

    # Decides whether a certain row,column grid element is inside the maze or outside
    def isInGrid(self,row,column):
        # TODO: this is you job now :-)
        pass


    # Returns a list of all grid elements neighboured to the grid element row,column
    def getNeighbours(self,row,column):
        # TODO: this is you job now :-)
        # TODO: Add a Unit Test Case --> Very good example for boundary tests and condition coverage
        pass

    # Gives a grid element as string, the result should be a string row,column
    def gridElementToString(self,row,col):
        # TODO: this is you job now :-)
        # HINT: this method is used as primary key in a lookup table
        pass
    
    # check whether two different grid elements are identical
    # aGrid and bGrid are both elements [row,column]
    def isSameGridElement(self, aGrid, bGrid):
        # TODO: this is you job now :-)
        pass


    # Defines a heuristic method used for A* algorithm
    # aGrid and bGrid are both elements [row,column]
    def heuristic(self, aGrid, bGrid):
        # TODO: this is you job now :-)
        # HINT: a good heuristic could be the distance between to grid elements aGrid and bGrid
        pass

    # Generates the resulting path as string from the came_from list
    def generateResultPath(self,came_from):
        # TODO: this is you job now :-)
        # HINT: this method is a bit tricky as you have to invert the came_from list (follow the path from end to start)
        pass

    #############################
    # Definition of Maze solver algorithm
    #
    # implementation taken from https://www.redblobgames.com/pathfinding/a-star/introduction.html
    #############################
    def myMazeSolver(self):
        # TODO: this is you job now :-)
        pass

    # Command for starting the solving procedure
    def solveMaze(self):
        return self.myMazeSolver()


if __name__ == '__main__':
    mg = MazeSolverAlgoTemplate()


    # HINT: in case you want to develop the solver without MQTT messages and without always
    #       loading new different mazes --> just load any maze you would like from a file

    #mg.loadMaze("..\\MazeExamples\\Maze1.txt")
    #solutionString = mg.solveMaze()
    #print(solutionString)
   
