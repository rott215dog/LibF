def __bub_check(L):
        for i in range(len(L) - 1):
            if L[i + 1] < L[i]:
                return False
        return True

def __index_smallest(L):
    small = L[0]
    to_return = 0
    for i in range(len(L)):
        elem = L[i]
        if elem < small:
            small = elem
            to_return = i
    return to_return


def bubble_sort(L):
    while True:
        for i in range(len(L) - 1):
            if L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]
        if __bub_check(L):
            break

def bubble_sort_count(L):
    count = 0
    while True:
        for i in range(len(L) - 1):
            if L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]
                count += 1
        if __bub_check(L) == True:
            break
    return count

def selection_sort(L):
    for i in range(len(L)):
        k = __index_smallest(L[i:]) + i
        L.insert(i, L.pop(k))
        if __bub_check(L) == True:
            break

def selection_sort_count(Lst):
    L = Lst[:]
    count = 0
    for i in range(len(L)):
        k = __index_smallest(L[i:]) + i
        L.insert(i, L.pop(k))
        count += (k - i)
        if __bub_check(L) == True:
            break
    return count

def elim_dups(L):
    check = []
    for i in range(len(L)):
        if L[i] not in check:
            check.append(L[i])
    while True:
        if L == []:
            break
        L.remove(L[-1])
    for j in range(len(check)):
        L.append(check[j])

def exchange(L,a,b):
    L[a], L[b] = L[b], L[a]

def qsort(L):
    if len(L) <= 1:
        return L
    P = L[len(L) // 2]
    R = []
    K = []
    for i in range(len(L)):
        if L[i] >= P and i != (len(L) // 2):
            R.append(L[i])
    for j in range(len(L)):
        if L[j] < P:
            K.append(L[j])
    return qsort(K) + [P] + qsort(R)

def mqsort(lst, left = None, right = None):
    if lst is None or lst == [] or len(lst) == 1:
        return
    if left == None:
        left,right = 0, len(lst) - 1
    if right <= left:
        return
