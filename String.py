def isalpha(a):
    if ord(a) in range(65, 91) or ord(a) in range(97, 123):
        return True


def rev(randstr):
    list1 = randstr.split(" ")
    for i in range(0, len(list1)):
        list1[i] = list1[i][::-1]
    list1.reverse()
    randstr = " ".join(list1)
    return randstr
