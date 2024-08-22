n, m = map(int,input().split())
path = ""
fn = 1
while True:
    path += str(fn)
    fn = 1 + (fn - 2 + m) % n
    if fn == 1:
        break
print(path)


