def event():
    b = 0
    with open("help/count.txt", "rb") as f:
        f = f.read()
        b = int(f)
        b+=1
        b = str(b)
    with open("help/count.txt", "w") as f:
        f.write(b)