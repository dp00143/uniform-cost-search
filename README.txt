Citymapper Router Challenge
==============================================

This is a solution to the Citymapper Router Challenge implemented by Daniel Puschmann.

How to run the program?
----------
A run.sh file is provided that will execute the main function. Given a graph.dat file a start and an end node the
program will print the length of the shortest path in meters if it exists, and nothing if no such path exists.
For example:
```
./run.sh citymapper-coding-test-graph.dat 876500321 1524235806
```
The program is tested on OS X using python 2.7.10. It may be necessary to change the permissions of the run.sh file
using:
```
chmod u+x job.sh
```

Design decisions
----------
Initially the input file is read and a graph is built. For each node, all it's neighbours are stored with the
information about the distance between this node and the neighbour. Finally, a distance to start variable
is set to ```sys.max``` for each node except the starting node (where the distance is set as 0).
For the calculation of the shortest path, I have decided to implement the uniformCostSearch algorithm.
I chose this algorithm because it only adds nodes to the priority queue as they are discovered, which speeds up the
queue operations. The priority in which neighbouring nodes are visited is given by their distance to the start node.

Assumptions
----------
* If no path exists, nothing needs to be returned.
* The distances between the nodes are positive integers


Ideas of extension
----------
* Return also the path of nodes so that the route will be known for the solution
* Return not only the shortest path, but all paths that are within a threshold to the optimal solution. This
  can be useful if we want to provide alternative routes that may suit the needs of the user better (e.g.
  different transportation modal, better air quality for walking routes, cheaper fare)
