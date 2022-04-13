# Write a Program to check whether a string is a valid shuffle of two strings or not

def isInterleaving(X, Y, S):
    if not X and not Y and not S:
        return True

    if not S:
        return False

    if X and S[0] == X[0]:
        return isInterleaving(X[1:], Y, S[1:])

    if Y and S[0] == Y[0]:
        return isInterleaving(X, Y[1:], S[1:])

    return False


if __name__ == '__main__':

    X = input("Enter 1st string : ")
    Y = input("Enter 2nd string : ")
    S = input("Enter 3rd string : ")

    if isInterleaving(X, Y, S):
        print('Interleaving')
    else:
        print('Not an Interleaving')
