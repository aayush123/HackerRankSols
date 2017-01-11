#Question link : https://www.hackerrank.com/challenges/primsmstsub

#initialize nodes and edges
nodes, edges = [int(x) for x in input().split()]

#initialize empty adjacency dictionary
adj_dict = {}
for each_node in range(1,nodes+1):
    adj_dict[each_node] = []

#update adjacency dictionary with input values
for each_edge in range(edges):
    v1,v2,w = [int(x) for x in input().split()]
    adj_dict[v1].append([v2,w])
    adj_dict[v2].append([v1,w])

#get start node
start_node = int(input())

#initialize empty tree node list
tree_nodes = []

#initialize 0 result weight
res_weight = 0

#initialize list of possible nodes with adj(start)
possible_edges_dict = {}
adj_nodes = adj_dict[start_node]
tree_nodes.append(start_node)
for each_adj_node in adj_nodes:
    weight = each_adj_node[1]
    if(weight not in possible_edges_dict.keys()):
        possible_edges_dict[weight] = [[start_node, each_adj_node[0]]]
    else:
        possible_edges_dict[weight].append([start_node, each_adj_node[0]])

#start Prim's Algo
while(len(tree_nodes) != nodes):
    #get minimum weight from all possible edges
    min_weight = min(possible_edges_dict.keys())

    #get all edges with minimum weight
    greedy_edges = possible_edges_dict[min_weight]

    for each_edge in greedy_edges:
        #pop each edge that is examined and remove minimum weight key from dict if it gets empty.
        possible_edges_dict[min_weight].remove(each_edge)
        if(possible_edges_dict[min_weight] == []):
            possible_edges_dict.pop(min_weight)

        #If an edge with minimum weight connect the tree to a node not yet in tree,
        #add the node to tree, add weight to total result and add all adjacent edges to possible_edges_dict
        if(each_edge[0] in tree_nodes and each_edge[1] not in tree_nodes):
            res_weight += min_weight
            new_node = each_edge[1]
            tree_nodes.append(new_node)
            adj_nodes = adj_dict[new_node]
            for each_adj_node in adj_nodes:
                weight = each_adj_node[1]
                if(weight not in possible_edges_dict.keys()):
                    possible_edges_dict[weight] = [[start_node, each_adj_node[0]]]
                else:
                    possible_edges_dict[weight].append([start_node, each_adj_node[0]])

print(res_weight)
