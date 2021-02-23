def Minimumdistances(a):
    a = a.split(" ")
    length = len(a)//2 
    left = length - 1
    right = 0
    if len(a) % 2 != 0:
        right = length + 1
    else:
        right = length
    for i in range(length):
        print(a[int(left)],a[int(right)],"difference {}".format(int(right)-int(left)))
        if a[int(left)] == a[int(right)]:
            print(int(right)-int(left))
        right += 1 
        left  -= 1
Minimumdistances("454 9087 239")
