def solution(n):
    # Your code here
    op = 0
    n = int(n)
    st = str(n) + ' -> '
    while n > 1:
        if n % 2 == 0:
            op += 1
            n /= 2
        elif n == 3 or n % 4 == 1:
            op += 1
            n -= 1
        else:
            op += 1
            n += 1
    #     st += str(n) + ' -> '
    # print("Operations: " + st)
    return op

if __name__ == "__main__":
    print(solution('15'))
    print(solution('4'))
        
