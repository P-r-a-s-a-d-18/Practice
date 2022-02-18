def solution(d1, c1, m1, s1):

    i = 0
    while i < len(s1):
        if d1 > 0 and c1 > 0:
            if s1[i] == 'C':
                c1 = c1 - 1
                i = i + 1
            elif s1[i] == 'D':
                d1 = d1 - 1
                c1 = c1 + m1
                i = i + 1
        else:
            break
    return i + 1


if __name__ == "__main__":

    n = input().split()
    d, c, m = (int(x) for x in n)
    s = input("String : ")

    res = s[solution(d, c, m, s):]
    print(res)

    if 'D' in res:
        print("No all dogs feed")
    else:
        print('All dogs feed')
