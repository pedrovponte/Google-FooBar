def solution(xs):
    # Your code here
    result = "0"
    if(len(xs) > 0):
        if(len(xs) == 1 and xs[0] <= 0):
            result = str(xs[0])
            return result
        sorted_arr = xs
        sorted_arr.sort()
        # print("SORTED: " + str(sorted_arr))
        neg_list = list(filter(lambda x: (x < 0), sorted_arr))
        neg_list.sort()
        pos_list = list(filter(lambda x: (x >= 0), sorted_arr))
        pos_list.sort()
        # print("POS LIST: " + str(pos_list))
        # print("NEG LIST: " + str(neg_list))
        if len(neg_list) % 2 != 0:
            neg_list = neg_list[:len(neg_list)-1]
        # print("NEG LIST1: " + str(neg_list))

        new_arr = neg_list + pos_list
        # print("NEW ARR: " + str(new_arr))

        product = 1
        count = 0
        for x in new_arr:
            if(x != 0):
                count += 1
                product *= x
        if count > 0:
            result = str(product)
        #print("Result: " + result)
    
    return result


if __name__ == "__main__":
    # print(solution([5,3,-1,-2,8,-10,6]))
    # print(solution([2,0,2,2,0]))
    # print(solution([-2,-3,4,-5]))
    print(solution([-3]))