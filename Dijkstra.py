import sys
from collections import defaultdict
import heapq
import math
sys.setrecursionlimit(10**6)


class Graph:

    # graph constructor initalizes verticies, weights, and distance, done, and parent lists
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjList = defaultdict(list)
        self.distance = self.vertices * [math.inf]
        self.done = self.vertices * [False]
        self.parents = self.vertices * [None]

    # buildlist builds the adj list
    def buildlist(self, input):
        start = input[::3]
        end = input[1::3]
        weights = input[2::3]
        for i in range(len(start)):
            self.addEdge(start[i], end[i], weights[i])

    # addEdge adds an edge to the adj list
    def addEdge(self, start, end, weight):
        self.adjList[start].append([weight, end])

    def dijkstra(self, source):

        # put the distance of source node to 0 and create priority queue using heapq
        self.distance[source] = 0
        priorityQ = []

        # put source node onto priority queue
        heapq.heappush(priorityQ, [0, source])

        # run while priority queue is not empty
        while priorityQ != []:
            # extracts the distance and node from queue
            current = heapq.heappop(priorityQ)
            currentdist = int(current[0])
            currentnode = int(current[1])
            # if node in done list is false, set it to true
            if self.done[currentnode] is False:
                self.done[currentnode] = True
                # go through neighbors of the node removed from heap
                for neighbor in self.adjList[currentnode]:
                    [weight, neigh] = neighbor
                    # update distance if not visited yet or if new path is shorter
                    if self.distance[neigh] == math.inf or weight + currentdist < self.distance[neigh]:
                        self.parents[neigh] = currentnode
                        self.distance[neigh] = currentdist + weight
                    # put neighbors into queue
                    heapq.heappush(priorityQ, [self.distance[neigh], neigh])

read = sys.stdin.readlines()

# split input to gather data such as
# number of verticies and edges and weights
line1 = read[0]
vertices = int(line1.split()[0])
edges = int(line1.split()[1])
starting = int(line1.split()[2])
listOfInput = read[1:]

# creates values to be passed in to create adj list
values = []
for i in range(len(listOfInput)):
    a, b, c = list(map(int, listOfInput[i].split()))
    values.append(a)
    values.append(b)
    values.append(c)

# create graph and adj list
graph = Graph(vertices)
graph.buildlist(values)

# call dijkstras
graph.dijkstra(starting)

# for loop prints the output with node, distance, and parent
for node in range(graph.vertices):
    parent = graph.parents[node]
    if parent is not None:
        sys.stdout.write(str(node) + ' ' + str(graph.distance[node]) + ' ' + str(parent) + '\n')
