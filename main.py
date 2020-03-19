import sys
from pprint import pprint
from readData import buildGraph
from uniformCostSearch import uniformCostSearch

if __name__ == '__main__':
    f_name = sys.argv[1]
    start_node = sys.argv[2]
    end_node = sys.argv[3]
    #First build the graph
    graph = buildGraph(f_name)
    #Calculate the shortest distance. If None is returned, there is no path between
    #start and end node
    result = uniformCostSearch(graph, start_node, end_node)
    if result:
        print result


