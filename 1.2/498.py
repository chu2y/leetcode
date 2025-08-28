


cx, cy = 0, 0

m, n = 3, 3

ox, oy = -1, 1

mat = [[1,2,3],[4,5,6],[7,8,9]]

while cx != m-1 and cy != n-1:
    print(mat[cx][cy])

    if cx == 0 and cy % 2 == 0:
        cx, cy =

    if cx < 0:
        cx = 0
        ox = 1
        oy = -1
    elif cx >= m:
        cx = m
        ox = 1
        oy = 1

    if cy < 0:
        cy = 0
        oy = 1
        ox = -1
    elif cy >= n:
        cy = n
        oy = -1
        ox = 1
    cx, cy = cx + ox, cy + oy




