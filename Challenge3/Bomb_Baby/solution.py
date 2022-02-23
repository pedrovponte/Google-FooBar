def solution(x, y):
    # Your code here
    M = int(x)
    F = int(y)
    count = 0

    while (M > 0 and F > 0):
        if(M > F):
            count += M // F
            M = M % F
        else:
            count += F // M
            F = F % M
        # print("M: " + str(M))
        # print("F: " + str(F))
    
    if (M != 1 and F != 1):
        return "impossible"
    
    return str(count - 1)

if __name__ == "__main__":
    print(solution('4', '7'))
    print(solution('2', '1'))