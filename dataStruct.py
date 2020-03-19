import sys


class Node:

    def __init__(self, id, distanceToStart=sys.maxint):
        self.id = id
        self.neighbours = {}
        self.distanceToStart = distanceToStart

    def addNeighbour(self, nodeId, distance):
        self.neighbours[nodeId] = distance

    def __eq__(self, other):
        return other.id == self.id

    # These were used by me to test my solution
    def __str__(self):
        n = str(self.neighbours)
        return "Node %s: neighbours: %s distanceToStart: %i" % (self.id, n, self.distanceToStart)

    def __repr__(self):
        n = str(self.neighbours)
        return "Node %s: neighbours: %s distanceToStart: %i" % (self.id, n, self.distanceToStart)


class Graph:

    def __init__(self):
        self.nodes = {}
