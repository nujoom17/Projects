d = int(input("enter the no of words you wanna add in list?:\t"))
a = []
c = 1
for i in range(d):
    e = input(f"enter the element no{c}: ")
    a.append(e)
    c += 1
def stro(j,k):
    j = input("enter the word from which u want to remove")
    for item in a:
        if item in j:
            k = input("enter n'th word you wanna remove")
            for s in item:
                if s in k:
                    print(item.replace(s,''))


print(stro("sam","2"))















