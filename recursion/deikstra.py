def graph_search():
    infinity = float('inf')
    shortest_path = []
    graph  = dict()
    graph['start'] = {}
    graph['start']['a'] = 6
    graph['start']['b'] = 2
    print(graph['start'].keys())
    print(graph['start']['a'])
    graph['a'] = {}
    graph['a']['fin'] = 1
    graph['b'] = {}
    graph['b']['a'] = 3
    graph['b']['fin'] = 5
    graph['fin'] = {}

    costs = dict()
    costs['a'] = 6
    costs['b'] = 2
    costs['fin'] = infinity

    parents = dict()
    parents['a'] = 'start'
    parents['b'] = 'start'
    parents['fin'] = None

    processed = []

    def find_lowest_cost_node(costs):
        lowest_cost = float('inf')
        lowest_cost_node = None
        for node in costs:
            cost = costs[node]
            if cost < lowest_cost and node not in processed:
                lowest_cost = cost
                lowest_cost_node = node
        print('lowest cost node ', lowest_cost_node)
        return lowest_cost_node

    node = find_lowest_cost_node(costs)

    while node is not None:
        shortest_path.append(node)
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)



if __name__ == '__main__':
    graph_search()