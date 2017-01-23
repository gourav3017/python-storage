from BinaryTree import BinNode, BinarySearchTree

class Graph:
    def __init__(self, vertices = {}, edgeLists = []):
        self.vertices = vertices
        self.edgeLists = edgeLists
    def addVertex(self, data):
        new_index = len(self.vertices)
        self.vertices[data] = new_index
        self.edgeLists.append(BinarySearchTree())
    def addEdge(self, start, end):
        indexStart = self.vertices[start]
        indexEnd = self.vertices[end]
        self.edgeLists[indexStart].insert(indexEnd)
    def deleteVertex(self, data):
        index = self.vertices[data]
        del self.vertices[data]
        del self.edgeLists[index]
    def deleteEdge(self, start, end):
        indexStart = self.vertices[start]
        indexEnd = self.vertices[end]
        self.edgeLists[indexStart].delete(indexEnd)
    def isAdjacent(self, start, end):
        indexStart = self.vertices[start]
        indexEnd = self.vertices[end]
        return self.edgeLists[indexStart].search(indexEnd)
    def neighborsOf(self, start):
        indexStart = self.vertices[start]
        temp = []
        for k, v in self.vertices.items():
            if self.edgeLists[indexStart].search(v):
                temp.append(k)
        return temp
