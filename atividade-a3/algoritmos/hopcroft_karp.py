from collections import deque

def hopcroft_karp(G):
    D = [float('inf') for _ in range(G.qtdVertices)]

    mate = [None for _ in range(G.qtdVertices)]

    m = 0

    while(bfs(G, mate, D)):
        for x in G.X():
            if(mate[x - 1] == None):
                if(dfs(G, mate, x, D)):
                    m += 1
    return m, mate

def bfs(G, mate, D):
    Q = deque()

    for x in G.X():
        if (mate[x - 1] == None):
            D[x - 1] = 0
            Q.append(x)
        else:
            D[x - 1] = float('inf')
    
    Dnull = float('inf')

    while(len(Q)):
        x = Q.popleft()
        if(D[x - 1] < Dnull):
            for y in G.Y():
                if(mate[int(y) - 1] != None):
                    if(D[mate[int(y) - 1]] == float('inf')):
                        D[mate[y.id - 1]] = D[int(x) - 1] + 1
                        Q.append(mate[y - 1])

    return Dnull != float('inf')


def dfs(G, mate, x, D):
    if (x != None):
        for y in G.vizinhos(x).keys():
            if (mate[y - 1] != None):
                if(D[mate[y - 1]] == D[x - 1] + 1):
                    if(dfs(G, mate, mate[y - 1], D)):
                        mate[x - 1] = y
                        mate[y - 1] = x
                        return True
        D[x - 1] = float('inf')
        return False
    return True
