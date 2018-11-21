
def check(duplicate,a):
    p=0
    for i in duplicate:
        if i==a:
            p=p+1
    return p
duplicate = [2, 4, 10, 20, 5, 2, 20, 4,4,4,4,4,4,4,4,4,]

print(check(duplicate,4))

