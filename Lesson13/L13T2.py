# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.


def symmetric(liste):
    # Your code here
    if not liste:
        return False
    inv = invert(liste)
    if len(liste) != len(inv):
        return False
    for i in range(len(liste)):
        if liste[i] != inv[i]:
            return False
    return True


def invert(liste):
    hilf1 = []
    for i in range(len(liste)):
        hilf2 = []
        for j in liste:
            try:
                hilf2.append(j[i])
            except:
                return None
        hilf1.append(hilf2)
    return hilf1

# a = [['cricket', 'football', 'tennis'], ['golf']]
# b = invert(a)

print(symmetric([[1, 2, 3],
                 [2, 3, 4],
                 [3, 4, 1]]))
# >>> True

print(symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "fish"],
                ["fish", "fish", "cat"]]))
# >>> True

print(symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish","fish","cat"]]))
# >>> False

print(symmetric([[1, 2],
                [2, 1]]))
# >>> True

print(symmetric([[1, 2, 3, 4],
                [2, 3, 4, 5],
                [3, 4, 5, 6]]))
# >>> False

print(symmetric([[1,2,3],
                 [2,3,1]]))
# >>> False