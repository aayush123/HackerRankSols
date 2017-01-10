#Question link : https://www.hackerrank.com/challenges/bfsshortreach

test_cases = int(input())
for each_test_case in range(test_cases):
    #ASSUME ALL LISTS 1 INDEXED NOT 0!!
    
    #initialize number of nodes and edges
    nodes, edges = [int(x) for x in input().split()]
    
    #initialize empty adjacency dictionary
    adj_dict = {}
    for each_node in range(1,nodes+1):
        adj_dict[each_node] = []
    
    #update adjacency dictionary with input values
    for each_edge in range(edges):
        v1,v2 = [int(x) for x in input().split()]
        if(v2 not in adj_dict[v1]):
            adj_dict[v1].append(v2)
        if(v1 not in adj_dict[v2]):
            adj_dict[v2].append(v1)
    
    #get start node
    start_node = int(input())
    
    #initialize result vector
    res_list = []
    for each_node in range(nodes):
        res_list.append(-1)
    #set start_node result to 0
    res_list[start_node-1] = 0

    #initialize empty Traversed List
    trav_list = []

    #initialize BFS queue
    q = []

    #start BFS
    q.append([start_node,0])
    while(q != []):
        current_node, current_lvl = q.pop(0)
        trav_list.append(current_node)
        adj_nodes = adj_dict[current_node]
        for each_adj_node in adj_nodes:
            to_be_trav = False
            for each_pair in q:
                if(each_pair[0] == each_adj_node):
                    to_be_trav = True
                    break
            if(each_adj_node not in trav_list and to_be_trav is False):
                q.append([each_adj_node,current_lvl+1])
        res_list[current_node-1] = current_lvl
        #print(res_list)
        #print(q)
    
    answer_string = ""
    
    for each_dist in res_list:
        if(each_dist == -1):
            answer_string += str(each_dist)+' '
        if(each_dist == 0):
            continue
        if(each_dist > 0):
            answer_string += str(each_dist*6)+' '
    
    print(answer_string)