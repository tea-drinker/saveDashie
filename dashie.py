
(top, left, bottom, right) = (406, 760, 471, 802)
img = [   [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 14, 14, 14, -1, 15, 15, 15, -1, 14, -1, -1, 14, -1, 15, 15, 15, -1, 14, 14, 14, -1, 15, 15, 15, -1, 14, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 14, -1, 14, -1, 15, -1, 15, -1, 14, 14, -1, 14, -1, -1, 15, -1, -1, 14, -1, -1, -1, 15, -1, -1, -1, 14, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 14, 14, 14, -1, 15, -1, 15, -1, 14, 14, 14, 14, -1, -1, 15, -1, -1, 14, 14, 14, -1, 15, 15, 15, -1, 14, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 14, -1, -1, -1, 15, -1, 15, -1, 14, -1, 14, 14, -1, -1, 15, -1, -1, 14, -1, -1, -1, -1, -1, 15, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 14, -1, -1, -1, 15, 15, 15, -1, 14, -1, -1, 14, -1, 15, 15, 15, -1, 14, 14, 14, -1, 15, 15, 15, -1, 14, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, 12, 12, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, 12, 12, 12, 12, 12, 12, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, 12, 12, 12, 5, 5, 5, 5, 12, 12, 12, -1, -1, -1, -1, -1, -1, -1, -1, 12, 12, 8, 8, 8, 8, 8, 6, 6, 12, 12, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, 12, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 12, -1, 12, -1, -1, -1, -1, 12, 10, 10, 10, 10, 8, 8, 8, 8, 6, 6, 6, 12, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, 12, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 12, 11, 12, -1, -1, -1, 10, 10, 10, 10, 10, 10, 8, 8, 8, 8, 6, 6, 5, 12, -1, -1, -1, -1],
    [-1, -1, -1, -1, 12, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 8, 11, 11, 11, 12, -1, 12, 10, 10, 10, 10, 10, 10, 10, 8, 8, 8, 8, 6, 5, 5, 12, -1, -1, -1],
    [-1, -1, -1, 12, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 8, 8, 8, 8, 11, 11, 11, 12, 12, 12, 12, 12, 10, 10, 10, 10, 10, 10, 8, 8, 8, 6, 6, 5, 5, 12, -1, -1],
    [-1, -1, 12, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 8, 8, 8, 12, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 10, 10, 10, 8, 8, 8, 6, 6, 5, 12, -1, -1],
    [-1, -1, 12, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 8, 8, 8, 8, 12, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 10, 10, 8, 8, 8, 6, 6, 5, 12, -1, -1],
    [-1, -1, 12, 5, 5, 5, 6, 6, 6, 6, 6, 6, 8, 8, 8, 8, 12, 11, 11, 11, 11, 12, 12, 15, 15, 15, 12, 12, 12, 12, 12, 12, 12, 10, 8, 8, 6, 6, 5, 12, -1, -1],
    [-1, -1, 12, 5, 5, 5, 6, 6, 6, 6, 6, 8, 8, 8, 8, 12, 11, 11, 11, 11, 11, 12, 15, 15, 12, 12, 11, 11, 11, 11, 11, 11, 12, 10, 8, 8, 6, 6, 5, 12, -1, -1],
    [-1, -1, 12, 5, 5, 5, 6, 6, 6, 6, 6, 8, 8, 8, 8, 12, 11, 11, 11, 11, 11, 12, 15, 15, 12, 12, 12, 11, 11, 11, 11, 11, 11, 12, 10, 8, 6, 6, 5, 12, -1, -1],
    [-1, -1, 12, 5, 5, 6, 6, 6, 6, 6, 8, 8, 12, 8, 12, 11, 11, 11, 11, 11, 3, 12, 12, 11, 11, 11, 11, 11, 12, 11, 11, 12, 11, 11, 12, 12, 6, 6, 5, 12, -1, -1],
    [-1, -1, -1, 12, 5, 6, 6, 6, 6, 8, 8, 8, 12, 8, 12, 11, 11, 11, 3, 3, 3, 12, 11, 11, 11, 11, 11, 12, 11, 12, 12, 0, 12, 11, 11, 12, 6, 5, 5, 12, -1, -1],
    [-1, -1, -1, 12, 5, 6, 6, 6, 6, 8, 8, 8, 12, 8, 12, 11, 11, 11, 3, 11, 11, 12, 11, 11, 12, 12, 12, 12, 12, 12, 0, 0, 0, 12, 11, 11, 6, 5, 5, 12, -1, -1],
    [-1, -1, -1, 12, 5, 6, 6, 6, 6, 8, 8, 12, 12, 12, 3, 11, 11, 3, 11, 11, 12, 11, 11, 12, 11, 12, 11, 11, 11, 11, 12, 12, 12, 11, 11, 11, 12, 5, 12, -1, -1, -1],
    [-1, -1, -1, 12, 6, 6, 6, 6, 6, 8, 8, 3, 12, 12, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 11, 11, 11, 11, 11, -1, -1, -1, 11, 11, 11, 12, 5, 12, -1, -1, -1],
    [-1, -1, -1, 12, 6, 6, 6, 6, 8, 8, 12, 11, 11, 12, 11, 11, 11, 11, 11, 12, 12, 11, 11, 11, 12, 11, 11, 11, 11, 11, 11, -1, -1, 11, 11, 11, 11, 12, -1, -1, -1, -1],
    [-1, -1, -1, -1, 12, 6, 6, 6, 8, 8, 12, 12, 11, 11, 11, 11, 11, 12, 12, 11, 11, 11, 11, 11, 12, 11, 11, 11, 11, 11, 11, 11, -1, 11, 11, 11, 11, 12, -1, -1, -1, -1],
    [-1, -1, -1, -1, 12, 6, 6, 6, 8, 8, 12, 11, 12, 12, 11, 12, 12, 12, 11, 11, 11, 11, 11, 11, 12, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, 12, 6, 6, 6, 8, 8, 12, 11, 11, 11, 12, 11, 12, 11, 11, 11, 11, 11, 11, 11, 12, 12, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, 12, 6, 6, 8, 8, 12, 11, 11, 11, 11, 11, 12, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 11, 11, 11, 11, 11, 11, 12, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, 12, 6, 6, 8, 8, 12, 12, 11, 11, 11, 11, 11, 12, 11, 11, 11, 12, 10, 12, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, 12, 6, 8, 8, 12, 15, 12, 12, 12, 11, 11, 12, 11, 12, 12, 10, 10, 12, 12, 11, 11, 11, 11, 11, 11, 11, 11, 12, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, 12, 8, 8, 12, 15, 15, 15, 15, 12, 12, 12, 12, 10, 10, 10, 10, 10, 12, 12, 12, 12, 12, 12, 12, 12, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, 12, 8, 12, 15, 15, 15, 15, 12, 12, 12, 10, 10, 10, 10, 10, 8, 8, 8, 8, 6, 5, 5, 5, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, 12, 8, 12, 15, 15, 15, 15, 15, 12, 12, 10, 10, 10, 10, 8, 8, 8, 8, 6, 5, 5, 5, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, 12, 12, 15, 15, 15, 15, 15, 12, 12, 12, 10, 10, 10, 8, 8, 8, 6, 6, 5, 5, 5, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, 15, 15, 15, 15, 12, 12, 12, 10, 10, 8, 8, 8, 6, 6, 5, 5, 5, 5, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, 15, 15, 15, 15, 12, 12, 12, 10, 8, 8, 8, 6, 6, 5, 5, 5, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, 12, 15, 15, 15, 12, 12, 12, 10, 8, 8, 8, 6, 5, 5, 5, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, 15, 15, 12, 12, 12, 10, 8, 8, 6, 6, 5, 5, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, 15, 15, 12, 12, 12, 10, 8, 6, 6, 5, 5, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, 15, 15, 12, 12, 12, 10, 8, 6, 6, 5, 5, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, 15, 15, 12, 12, 12, 10, 8, 6, 5, 5, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, 15, 15, 12, 12, 12, 10, 6, 6, 5, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, 15, 15, 12, 12, 10, 10, 6, 5, 5, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, 15, 12, 12, 12, 10, 8, 6, 5, 5, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, 15, 12, 12, 10, 10, 8, 5, 5, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, 15, 12, 12, 10, 10, 8, 5, 5, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, 12, 12, 10, 8, 6, 5, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, 12, 12, 10, 8, 6, 5, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, 12, 12, 10, 8, 6, 5, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, 12, 12, 10, 8, 6, 12, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, 12, 10, 8, 6, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, 12, 10, 8, 6, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, 10, 8, 6, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, 12, 8, 6, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, 8, 6, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, 8, 6, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, 12, 6, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, 6, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, 6, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]

