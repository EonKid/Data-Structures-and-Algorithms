# Uses python3


def edit_distance(s, t):
    n = len(s)
    m = len(t)
    D = [[float('inf')] * (m+1) for _ in range(n+1)]
    for i in range(0, n+1):
        D[i][0] = i
    for j in range(0, m+1):
        D[0][j] = j

    for i in range(1, n+1):
        for j in range(1, m+1):
            insertion = D[i][j-1] + 1
            deletion = D[i-1][j] + 1
            mismatch = D[i-1][j-1] + 1
            matched = D[i-1][j-1]
            if s[i-1] == t[j-1]:
                D[i][j] = min(insertion, deletion, matched)
            else:
                D[i][j] = min(insertion, deletion, mismatch)
    return D[n][m]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
