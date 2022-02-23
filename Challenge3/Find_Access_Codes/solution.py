def solution(l):
    # Your code here
    count = 0
    n = len(l)
    arr = [0] * n
    for i in range(n):
        for j in range(i+1, n):
            if l[j] % l[i] == 0:
                arr[i] += 1
    
    for i in range(n):
        for j in range(i+1, n):
            if l[j] % l[i] == 0:
                count += arr[j]

    return count

if __name__ == "__main__":
    print(solution([1, 2, 3, 4, 5, 6]))
    print(solution([1, 1, 1]))