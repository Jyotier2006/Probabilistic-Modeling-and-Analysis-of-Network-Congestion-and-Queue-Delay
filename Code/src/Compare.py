from graph_model import QueueDelayGraph
from dijkstra import run_dijkstra
from astar import run_astar

def load_data(filename):
    with open(filename, "r") as f:
        n, m = map(int, f.readline().split())

        edges = []
        for _ in range(m):
            u, v = map(int, f.readline().split())
            edges.append((u, v))

        queue_len = list(map(int, f.readline().split()))
        service_rate = list(map(int, f.readline().split()))
        source, dest = map(int, f.readline().split())

        coords = {}
        for i in range(n):
            x, y = map(int, f.readline().split())
            coords[i] = (x, y)

    return n, edges, queue_len, service_rate, source, dest, coords

def save_results(filename, results):
    with open(filename, "w") as f:
        for res in results:
            f.write(f"Algorithm: {res['algorithm']}\n")
            f.write(f"Path: {res['path']}\n")
            f.write(f"Total Queue Delay: {res['delay']}\n")
            f.write(f"Expanded Nodes: {res['expanded_nodes']}\n")
            f.write(f"Runtime (sec): {res['runtime_seconds']:.8f}\n")
            f.write("\n")

        if abs(results[0]["delay"] - results[1]["delay"]) < 1e-9:
            f.write("Observation: Both algorithms produced the same minimum queue delay.\n")
        else:
            f.write("Observation: The algorithms produced different queue delays.\n")

        if results[0]["expanded_nodes"] < results[1]["expanded_nodes"]:
            f.write("Observation: Dijkstra expanded fewer nodes.\n")
        elif results[1]["expanded_nodes"] < results[0]["expanded_nodes"]:
            f.write("Observation: A* expanded fewer nodes.\n")
        else:
            f.write("Observation: Both algorithms expanded the same number of nodes.\n")

def main():
    n, edges, queue_len, service_rate, source, dest, coords = load_data("../Data/data_100.txt")
    graph_obj = QueueDelayGraph(n, edges, queue_len, service_rate, coords)

    res1 = run_dijkstra(graph_obj, source, dest)
    res2 = run_astar(graph_obj, source, dest)

    results = [res1, res2]

    for res in results:
        print(f"Algorithm: {res['algorithm']}")
        print(f"Path: {res['path']}")
        print(f"Total Queue Delay: {res['delay']}")
        print(f"Expanded Nodes: {res['expanded_nodes']}")
        print(f"Runtime (sec): {res['runtime_seconds']:.8f}")
        print()

    if abs(res1["delay"] - res2["delay"]) < 1e-9:
        print("Observation: Both algorithms produced the same minimum queue delay.")
    else:
        print("Observation: The algorithms produced different queue delays.")

    if res1["expanded_nodes"] < res2["expanded_nodes"]:
        print("Observation: Dijkstra expanded fewer nodes.")
    elif res2["expanded_nodes"] < res1["expanded_nodes"]:
        print("Observation: A* expanded fewer nodes.")
    else:
        print("Observation: Both algorithms expanded the same number of nodes.")

    save_results("../Experiments/results.txt", results)

if __name__ == "__main__":
    main()
