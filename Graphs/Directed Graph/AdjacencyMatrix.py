class DirectedGraphAdjMatrix:
    def __init__(self, vertices):
        self.vertices = vertices  # Number of vertices in the graph
        # Create a 2D list (matrix) initialized to 0
        self.matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v):
        # Mark `u -> v` as 1 in the matrix since the graph is directed
        self.matrix[u][v] = 1

    def display(self):
        # Print the adjacency matrix row by row
        for row in self.matrix:
            print(row)