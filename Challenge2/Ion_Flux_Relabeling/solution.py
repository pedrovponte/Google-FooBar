def solution(h, q):
    # Your code here
    ret_list = []
    for node in q:
        start = 1
        end = pow(2, h) - 1
    
        # Check whether the given node
        # is a root node.if it is then
        # return -1 because root
        # node has no parent
        if (end == node):
            ret_list.append(-1)
            continue
    
        # Loop till we found
        # the given node
        while(node >= 1):
    
            end = end - 1
    
            # Find the middle node of the
            # tree because at every level
            # tree parent is divided
            # into two halves
            mid = start + (end - start)//2
    
            # if the node is found
            # return the parent
            # always the child nodes of every
            # node is node / 2 or (node-1)
            if(mid == node or end == node):
                ret_list.append(end + 1)
                break
            
            # if the node to be found is greater
            # than the mid search for left
            # subtree else search in right subtree
            elif (node < mid):
                end = mid
    
            else:
                start = mid
    return ret_list
 
# Driver code
if __name__ == "__main__":
    # height = 5
    # node = 14
     
    # Function Call
    print(solution(3, [7, 3, 5, 1]))
    print(solution(5, [19, 14, 28]))