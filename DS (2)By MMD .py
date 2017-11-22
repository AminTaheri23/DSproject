import time
import random
import matplotlib.pyplot as plt
import numpy as np


def nFacRuntimeFunc(n):  # order is n!
    for i in range(n):
        nFacRuntimeFunc(n - 1)


def bubbleSort(alist):  # oreder is n^2
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp


def moveTower(height, fromPole, toPole, withPole):  # order is 2^n
    if height >= 1:
        moveTower(height - 1, fromPole, withPole, toPole)
        moveTower(height - 1, withPole, toPole, fromPole)


def mergeSort(alist):  # Order is n*log(n)
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1


def linear_search(x, search_list):  # order is n
    iterations = 0
    idx = 0
    while idx < len(search_list):
        iterations += 1
        if x == search_list[idx]:
            return idx
        idx += 1
    return -1


def menu_selector(n):
    my_randoms = []
    linearsearch = [0 for _ in range(100)]
    bubblesort = [0 for _ in range(100)]
    hanio = [0 for _ in range(100)]
    mergesort = [0 for _ in range(100)]
    nfact = [0 for _ in range(100)]
    nfact = np.array(nfact)
    linearsearch = np.array(linearsearch)
    bubblesort = np.array(bubblesort)
    hanio = np.array(hanio)
    mergesort = np.array(mergesort)
    indx = 1
    m = 1000 * indx
    for i in range(m):
        my_randoms.append(random.randrange(1, 101, 1))
    while indx < 100:
        if n == 1 or n == 6:
            # --------------BUBBLE-------------------
            start_millis = int(round(time.time() * 1000))
            bubbleSort(my_randoms)
            end_millis = int(round(time.time() * 1000))
            bubblesort[indx] = -1 * (start_millis - end_millis)
        if n == 2 or n == 6:
            # --------------HANOI--------------------
            start_millis = int(round(time.time() * 1000))
            moveTower(int(m / 1000), "A", "B", "C")
            end_millis = int(round(time.time() * 1000))
            hanio[indx] = -1 * (start_millis - end_millis)
        if n == 3 or n == 6:
            # ---------------Merge-------------------
            start_millis = int(round(time.time() * 1000))
            mergeSort(my_randoms)
            end_millis = int(round(time.time() * 1000))
            mergesort[indx] = -1 * (start_millis - end_millis)
        if n == 4 or n == 6:
            # ---------------Linear Search--------------
            rnd_elemnt_indx = random.randrange(1, m, 1)
            # print(rnd_elemnt_indx)
            start_millis = int(round(time.time() * 1000))
            linear_search(rnd_elemnt_indx, my_randoms)
            end_millis = int(round(time.time() * 1000))
            linearsearch[indx] = -1 * (start_millis - end_millis)
        if n == 5 or n == 6:
            # --------------Nfact--------------------
            start_millis = int(round(time.time() * 1000))
            nFacRuntimeFunc(indx)
            end_millis = int(round(time.time() * 1000))
            nfact[indx] = -1 * (start_millis - end_millis)
        indx += 1
    index = [i for i in range(100)]
    index = np.array(index)
    plt.plot(index, bubblesort, label='BUBBLE', )
    plt.plot(index, hanio, label='HANOI')
    plt.plot(index, mergesort, label='Merge')
    plt.plot(index, linearsearch, label='Linear Search')
    plt.plot(index, nfact, label='Nfact')

    plt.xlabel('x = Numbers')
    plt.ylabel('y = Time(msec)')

    plt.title("DS First project Plot")

    plt.legend()

    plt.show()


alg_selector = int(input(
    "What Algorithm you wana choose ? \n1-Buuble Sort\n2-Hanoi\n3-Merge Sort\n4-Linear Search\n5-an (N!) Function\n6-All of them 2gether"))
menu_selector(alg_selector)
