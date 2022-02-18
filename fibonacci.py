def fibonacci(N: int) -> int:
    arr = [0, 1]
    if N < 2:
        return arr[N]
    for i in range(N-1):
        arr[0], arr[1] = arr[1], arr[0]+arr[1]
    return arr[1]
