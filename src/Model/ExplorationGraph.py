# -*- coding: utf-8 -*-

class ExplorationGraph:
    
        def __init__(self, beliefEnv):
            self.graph = beliefEnv  # a voir si transforme beliefEnv en graphe
            visited = [] # List to keep track of visited nodes.
            queue = [] #Initialize a queue
            graph = []
            
        def bfs(node): ##non terminé
            visited.append(node)
            queue.append(node)
            while queue:
                s = queue.pop(0) 
                print (s, end = " ") 

            for neighbour in graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
