'''
Created on 26 Apr 2014

@author: Nigel Steven Fernandez (IMT2013027)
'''

import time
import copy
from sudoku_methods import input_board, create_graph, print_board

def BFS(source, graph):
    '''
    Applies breadth first search on the graph with source as the first vertex
    The BFS ordering is used to colour the graph 
    '''
    
    #stores the number of colours used
    colours_used = 0 
    #stores the number of nodes coloured using colours > 9
    illegal_nodes = 0
    node_list = []
    for node in graph.adjacency.keys():
        node.parent = None
        node.search_colour = node.colour
    source.parent = source
    node_list.append(source)
    while(len(node_list) != 0):
        #list of possible colours
        #cannot exceed 21 as degree is 20
        colours = range(1, 22) 
        current_node = node_list.pop(0)
        for node in graph.adjacency[current_node]:
            if(current_node.search_colour == 0):
                if(node.search_colour != 0):
                    for k in range(len(colours)):
                        if (colours[k] == node.search_colour):
                            del colours[k]
                            break
            if (node.parent == None):
                node.parent = current_node
                node_list.append(node)  
        if(current_node.search_colour == 0):
            current_node.search_colour = colours[0]
            if(colours[0] > 9):
                illegal_nodes += 1
            if(colours[0] > colours_used):
                colours_used = colours[0]        

    return colours_used, illegal_nodes


def DFS(source, graph):
    '''
    Applies breadth first search on the graph with source as the first vertex
    The BFS ordering is used to colour the graph 
    '''
    
    #stores the number of colours used
    colours_used = 0 
    #stores the number of nodes coloured using colours > 9
    illegal_nodes = 0
    node_list = []
    for node in graph.adjacency.keys():
        node.parent = None
        node.search_colour = node.colour
    source.parent = source
    node_list.insert(0, source)
    while(len(node_list) != 0):
        #list of possible colours
        #cannot exceed 21 as degree is 20        
        colours = range(1, 22) 
        current_node = node_list.pop(0)
        for node in graph.adjacency[current_node]:
            if(current_node.search_colour == 0):
                if(node.search_colour != 0):
                    for k in range(len(colours)):
                        if (colours[k] == node.search_colour):
                            del colours[k]
                            break
            if (node.parent == None):
                node.parent = current_node
                node_list.insert(0, node)  
        if(current_node.search_colour == 0):
            current_node.search_colour = colours[0]
            if(colours[0] > 9):
                illegal_nodes += 1
            if(colours[0] > colours_used):
                colours_used = colours[0]     
        
    return colours_used, illegal_nodes
    
   
if __name__ == '__main__':
    '''
    Applies BFS and DFS on every node of the Sudoku graph
    Attempts to solve the Sudoku puzzle using graph colouring 
    '''
    
    board = input_board()
    sudoku, graph = create_graph(board)
    
    max_colour = 21
    #81 - 9 = 72
    illegal_nodes = 72
    start = time.time()
    for node in graph.adjacency.keys():
        colours_used, nodes = BFS(node, graph);
        if(colours_used < max_colour or (colours_used == max_colour and nodes < illegal_nodes)):
            max_colour = colours_used
            illegal_nodes = nodes
            #stores a copy of the Sudoku board  
            sudoku_coloured = copy.deepcopy(sudoku)
    stop_bfs = time.time()
    print_board(sudoku_coloured)
    print "No of colours used: {}".format(max_colour)
    print "No of illegal nodes: {}".format(illegal_nodes)
    print "All source BFS completed in " + str(stop_bfs - start) + " s\n"
    
    max_colour = 21
    illegal_nodes = 72
    for node in graph.adjacency.keys():
        colours_used, nodes = DFS(node, graph);
        if(colours_used < max_colour or (colours_used == max_colour and nodes < illegal_nodes)):
            max_colour = colours_used
            illegal_nodes = nodes
            #stores a copy of the Sudoku board  
            sudoku_coloured = copy.deepcopy(sudoku) 
    stop_dfs = time.time()
    print_board(sudoku_coloured)
    print "\nNo of Colours used: {}".format(max_colour)
    print "No of illegal nodes: {}".format(illegal_nodes)
    print "All source DFS completed in " + str(stop_dfs - stop_bfs) + " s"