def findZigZagSequence(a, n):
    a.sort()
    # First Change
    mid = int(n / 2)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    # Second Change
    ed = n - 2
    while st <= ed:
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        # Third Change
        ed = ed - 1

    for i in range(n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end=' ')
    return


findZigZagSequence([1, 2, 3, 4, 5, 6, 7], 7)
