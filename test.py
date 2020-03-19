from readData import buildGraph
from uniformCostSearch import uniformCostSearch

def testShortestPath():
    graph = buildGraph("test.dat")
    result = uniformCostSearch(graph, "1", "10")
    print result
    assert (result==40)

def testNoPathFound():
    graph = buildGraph("test.dat")
    result = uniformCostSearch(graph, "1", "9")
    print result
    assert (result is None)


if __name__ == '__main__':
    testShortestPath()
    testNoPathFound()