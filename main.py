
import heapq


def prim_mst(graph, start):
    """
    Build a minimum spanning tree (MST) using Prim's algorithm.

    graph: dict mapping node -> list of (neighbor, weight) pairs.
    start: starting node for Prim's algorithm.

    Returns:
        (mst_edges, total_cost)
        - mst_edges: list of (u, v, w) edges in the MST (order added).
        - total_cost: sum of weights w in all MST edges.

    Assumptions:
        - graph is connected and undirected (neighbors listed both ways).
        - start exists in graph.
    """
    if start not in graph:
        raise KeyError("start node not in graph")

    visited = {start}
    heap = []  # min-heap of (weight, u, v) crossing the cut
    for nbr, w in graph[start]:
        heapq.heappush(heap, (w, start, nbr))

    mst_edges = []
    total_cost = 0

    # Keep adding the smallest edge that connects to an unvisited node
    while heap and len(visited) < len(graph):
        w, u, v = heapq.heappop(heap)
        if v in visited:
            continue
        visited.add(v)
        mst_edges.append((u, v, w))
        total_cost += w

        for nbr, wt in graph.get(v, []):
            if nbr not in visited:
                heapq.heappush(heap, (wt, v, nbr))

    return mst_edges, total_cost


if __name__ == "__main__":
    # Optional manual test
    sample_graph = {
        "G1": [("G2", 4), ("G3", 2)],
        "G2": [("G1", 4), ("G3", 3)],
        "G3": [("G1", 2), ("G2", 3)],
    }
    edges, cost = prim_mst(sample_graph, "G1")
    print("Sample MST edges:", edges)
    print("Total cost:", cost)
