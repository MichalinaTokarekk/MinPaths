import sys
import math
import time


def read_data(filename: str) -> tuple:
    with open(filename, 'r') as file:
        source = int(file.readline().strip())  # Odczyt wierzchołka początkowego
        size = int(file.readline().strip())
        data = []
        for _ in range(size):
            row = file.readline().strip().split()
            data.append([math.inf if x == '*' else int(x) for x in row])
        return source, data


def dijkstra(data: list, source: int) -> tuple:
    size = len(data)
    distance = [math.inf] * size
    visited = [False] * size
    path = [""] * size

    distance[source] = 0
    path[source] = str(source)

    for _ in range(size):
        min_distance = math.inf
        min_index = -1
        for i in range(size):
            if not visited[i] and distance[i] < min_distance:
                min_distance = distance[i]
                min_index = i

        if min_index == -1:
            break

        visited[min_index] = True

        for j in range(size):
            if not visited[j] and data[min_index][j] != math.inf:
                if distance[min_index] + data[min_index][j] < distance[j]:
                    distance[j] = distance[min_index] + data[min_index][j]
                    path[j] = path[min_index] + " -> " + str(j)

    return distance, path


def bellman_ford(data: list, source: int) -> tuple:
    size = len(data)
    distance = [math.inf] * size
    path = [""] * size

    distance[source] = 0
    path[source] = str(source)

    for _ in range(size - 1):
        for u in range(size):
            for v in range(size):
                if data[u][v] != math.inf and distance[u] != math.inf:
                    if distance[u] + data[u][v] < distance[v]:
                        distance[v] = distance[u] + data[u][v]
                        path[v] = path[u] + " -> " + str(v)

    return distance, path


def main():
    source, data = read_data("data/10.txt")

    # Dijkstra
    start_time = time.perf_counter()
    distance_d, path_d = dijkstra(data, source)
    end_time = time.perf_counter()
    time_d = (end_time - start_time) * 1000

    # Bellman-Ford
    start_time = time.perf_counter()
    distance_b, path_b = bellman_ford(data, source)
    end_time = time.perf_counter()
    time_b = (end_time - start_time) * 1000

    print(f"Dijkstra: \t {time_d:.2f} ms")
    print("Results for Dijkstra:")
    for i in range(len(distance_d)):
        print(f"Distance from {source} to {i} = {distance_d[i]}\t Path: {source}{path_d[i]}")
    
    print()  # Empty line to separate results
    
    print(f"Bellman-Ford: \t {time_b:.2f} ms    ({time_b / time_d:.2f}x slower)")
    print("Results for Bellman-Ford:")
    for i in range(len(distance_b)):
        print(f"Distance from {source} to {i} = {distance_b[i]}\t Path: {source}{path_b[i]}")


if __name__ == "__main__":
    main()
