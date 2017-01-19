#Question link : https://www.hackerrank.com/challenges/kruskalmstrsub

graph_dict = {
    1:[2,3],
    2:[],
    3:[]
}

# def find_cycle_dfs(graph_dict, start_node):
#     start_adj_nodes = [x for x in graph_dict[start_node]]
#     stack = [x for x in graph_dict[start_node]]
#     traversed_nodes = [start_node]
#     while(stack != []):
#         curr_node = stack.pop(0)
#         curr_adj_nodes = graph_dict[curr_node]
#         traversed_nodes.append(curr_node)
#         for each_adj_node in curr_adj_nodes:
#             if(each_adj_node in start_adj_nodes):
#                 return True
#             if(each_adj_node not in stack and each_adj_node not in traversed_nodes):
#                 stack.insert(0, each_adj_node)
#     return False

def find_cycle_dfs(graph_dict, start_node):
    pass
    #implement dfs with path, check whether curr_node adj_nodes in start's adj_node and not in current_path.

#initialize nodes and edges
nodes, edges = [int(x) for x in input().split()]

#initialize empty weight dictionary
weight_dict = {}

#update weight dictionary with input values
for each_edge in range(edges):
    v1,v2,w = [int(x) for x in input().split()]
    if(w not in weight_dict.keys()):
        weight_dict[w] = []
    if([v1, v2] not in weight_dict[w] and [v2, v1] not in weight_dict[w]):
        weight_dict[w].append([v1, v2])



#initialize 0 result weight
res_weight = 0
