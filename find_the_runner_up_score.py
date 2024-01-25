if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    res = sorted(list(set(arr)))[len(list(set(arr)))-2]
    print(res)
     