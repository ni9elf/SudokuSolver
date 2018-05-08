'''
Created on 27 Apr 2014

@author: Nigel Steven Fernandez (IMT2013027)
'''

from graph import Graph, Node

def input_board():
    '''
    Inputs the Sudoku board from a file
    '''
    
    fread = open("easy_input.dat", "r")
    board = [list(row[:-1]) for row in fread]
    fread.close()
    
    return board
    

def create_graph(board):
    '''
    Stores the Sudoku board as a graph of 81 vertices and 810 edges
    Also creates a board of corresponding Sudoku nodes 
    '''
    
    row = []
    #stores the board of Sudoku nodes
    sudoku = []
    #stores the Sudoku graph
    graph = Graph()
    for line in board:
        for cell in line:
            colour = (int(cell) if cell != '.' else 0)
            node = Node(colour)
            graph.add_node(node)
            row.append(node)
        sudoku.append(row)
        row = []
    
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            node = sudoku[i][j]
            #add 20 undirected edges for each node
            for k in range(9):
                if(k != i):
                    graph.add_edge(node, sudoku[k][j])
                if(k != j):
                    graph.add_edge(node, sudoku[i][k])
            for i_1 in range((i / 3) * 3, ((i / 3) * 3) + 3): 
                for j_1 in range((j / 3) * 3, ((j / 3) * 3) + 3):
                    if(i_1 != i or j_1 != j):
                        graph.add_edge(node, sudoku[i_1][j_1])
            
    return sudoku, graph


def print_board(sudoku):
    '''
    Prints the Sudoku puzzle at the current state
    '''
    
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            if(sudoku[i][j].search_colour != 0):
                print(sudoku[i][j].search_colour),
            else:
                print '.',
                #for printing candidates instead:
                #print sudoku[i][j].candidates,
            if ((j + 1) % 3 == 0):
                print(" "),
        if((i + 1) % 3 == 0):
            print
        print