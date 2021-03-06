class Dirkstra(object):
    def __init__(self):
        pass

    def run(self, graph, source, goal):
        '''
        @param, graph, represented by adjacency list
        @param, source, the source vertex
        @param, goal, the goal vertex
        @return, boolean, return true if a path is found, return false otherwise
                 shortest_path, a list of vertice if shortest path is found
                 shortest_path_len, the length of shortest path if found.
        '''

        # initialzie
        unvisited_vertices_set = set()
        shortest_path = []
        shortest_path_len = 0
        # dist = [0] * len(graph)
        dist = {}
        prev = {}

        for v in graph:
            dist[v] = float('inf')
            unvisited_vertices_set.add(v)
        dist[source] = 0 # distance to source is 0

        # run algorithm
        path_exist = True
        while len(unvisited_vertices_set) > 0:
            min_dist = float('inf')
            for v in unvisited_vertices_set:
                if dist[v] < min_dist:
                    min_dist = dist[v]
                    min_v = v

            # print("mid_dist: {}".format(min_dist))
            # there is no path
            if min_dist == float('inf'):
                path_exist = False
                break

            # path to goal is found
            if min_v == goal:
                break

            unvisited_vertices_set.remove(min_v)

            for v, edge_length in graph[min_v].items():
                if v in unvisited_vertices_set:
                    if dist[min_v] + edge_length < dist[v]:
                        dist[v] = dist[min_v] + edge_length
                        prev[v] = min_v

        if path_exist:
            # extract shortest path:
            shortest_path.insert(0, goal)
            v = goal
            prev_v = prev[v]
            while prev_v != -1 and prev_v != source:
                shortest_path.insert(0, prev_v)
                prev_v = prev[prev_v]

            shortest_path.insert(0, source)
            shortest_path_len = dist[goal]
            return (True, shortest_path, shortest_path_len)
        else:
            return (False, None, None)