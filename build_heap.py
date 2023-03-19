def heapify(data, i, n, swaps):
    min_index = i
    left_child_index = 2 * i + 1
    right_child_index = 2 * i + 2

    if left_child_index < n and data[left_child_index] < data[min_index]:
        min_index = left_child_index

    if right_child_index < n and data[right_child_index] < data[min_index]:
        min_index = right_child_index

    if i != min_index:
        data[i], data[min_index] = data[min_index], data[i]
        swaps.append((i, min_index))
        heapify(data, min_index, n, swaps)

def build_heap(data):
    swaps = []
    n = len(data)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, i, n, swaps)
    
    return swaps

def check(data, swaps):
    n = len(data)
    for i in range(n):
        for j in range(i + 1, n):
            if data[j] < data[i]:
                data[i], data[j] = data[j], data[i]
                swaps.append((i, j))

    return swaps

def main():
    txt = input().strip()

    if 'F' in txt:
        filename = input().strip()
        if 'a' not in filename:
            f_path = './tests/' + filename
            with open(f_path) as f:
                n = int(f.readline())
                data = list(map(int, f.readline().split()))

    if 'I' in txt:
        n = int(input())
        data = list(map(int, input().split()))

    assert len(data) == n

    swaps = build_heap(data)
    

    print('swaps')
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == '__main__':
    main()
