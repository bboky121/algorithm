from sys import stdin, stdout

if __name__ == '__main__':
    N = stdin.readline()
    A = sorted(map(int, stdin.readline().split()))
    M = stdin.readline()
    D = map(int, stdin.readline().split())


    def binary(lists, data, start, end):
        if start > end:
            return 0
        pos = (start + end) // 2
        if lists[pos] == data:
            return 1
        elif lists[pos] > data:
            return binary(lists, data, start, pos - 1)
        else:
            return binary(lists, data, pos + 1, end)


    for i in D:
        print(binary(A, i, 0, len(A) - 1))
