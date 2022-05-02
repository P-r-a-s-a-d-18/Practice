# Count and Say problem or Look and Say problem

def lookandsay(a):
    if a == 1:
        return '1'
    cur = None
    count = 0
    num = ''
    for digit in lookandsay(a - 1) + ' ':
        if digit == cur:
            count += 1
        else:
            if cur:
                num += str(count + 1) + cur
                count = 0
            cur = digit
    return num


n = int(input())
print(lookandsay(n))
