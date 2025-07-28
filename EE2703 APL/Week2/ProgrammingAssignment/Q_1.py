def list_rotate(l, N):
    return l[N%len(l):] + (l[0:N%len(l)])

print(list_rotate([1, 2, 3, 4], 11))