from itertools import chain, combinations
import numpy as np
import math

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

class matroid:
    # defines the matroid
    # id - identification of the matroid (int)
    # size - size of the matroid (int)
    # rank - rank of the  matroid (int)
    # bases - list of bases (array of strings)
    def __init__(self, id, size, rank, bases):
        self.id = int(id)
        self.size = int(size)
        self.rank = int(rank)
        self.bases = bases
    # returns true if simple; otherwise, return false
    def simple(self):
        def check_i(i): # checks if i is in at least one base
            for base in self.bases:
                if str(i) in base:
                    return True
            return False
        def check_pair(i, j): # checks if i, j are both in at least one base together
            for base in self.bases:
                if str(i) in base and str(j) in base:
                    return True
            return False
        # check for loops
        for i in range(self.size):
            if not check_i(i):
                return False
        # checks for parallel elements
        for i in range(self.size):
            for j in range(i):
                if not check_pair(i, j):
                    return False
        return True
    
    def intersection(self, A, base):
        num = 0
        for a in A:
            if str(a) in base:
                num += 1
        return num
    
    def coloop(self, e):
        for base in self.bases:
            if str(e) not in base:
                return False
        return True
    def show_yourself(self, A, point):
        return "ID : " + str(self.id) + " ... SIZE :" + str(self.size) + " ... BASE : ... " + str(self.bases) + " ... at " + str(point) + " and partition " + str(A)

    def check_conjecture_specific(self, A):
        sequence = [0 for i in range(self.rank+1)]
        for base in self.bases:
            sequence[self.intersection(A, base)] += 1
        for k in range(1, self.rank):
            if sequence[k-1] != 0 and sequence[k] != 0 and sequence[k+1] != 0:
                if sequence[k]**2 * math.comb(self.rank, k+1) * math.comb(self.rank, k-1) == sequence[k-1] * sequence[k+1] * math.comb(self.rank, k)**2:
                    self.show_yourself(A, k)
                    return True # this indicates that there is a counterexample

    def check_conjecture(self):
        if self.id % 10 == 0:
            print("checking " + str(self.id))
        # only print "checking" if the id is multiple of 10
        if self.simple():
            for A in powerset(range(self.size)):
                for k in range(self.rank):
                    self.check_conjecture_specific(A)
        return False

    def check_HRR_conjecture(self):
        if self.simple():
            for i in range(self.size):
                if self.HRR(i):
                    print(str(self.id) + " and at e = " + str(i))
                    return True
        return False
    
    def HRR(self, m):
        n = self.size
        if not self.coloop(m):
            hessian = np.zeros((n, n))
            for i in range(n):
                for j in range(i):
                    if i == m or j == m:
                        for base in self.bases:
                            if str(i) in base and str(j) in base:
                                hessian[i][j] += 1
                                hessian[j][i] += 1
                    else:
                        for base in self.bases:
                            if str(i) in base and str(j) in base and str(m) not in base:
                                hessian[i][j] += 1
                                hessian[j][i] += 1
            if np.linalg.det(hessian) == 0:
                return True # this indicates that there is a counterexample
        return False


def convert_to_matroid(line):
    data = line.split()
    x = matroid(data[0], data[1], data[2], data[4:len(data)])
    # first data point - id number
    # second - size of the matroid
    # third - rank
    # fourth - number of bases
    return x

file = open("C:/senior-thesis-data/matroids09_bases",  'r')
lines = file.readlines()
for l in lines:
    mat = convert_to_matroid(l)
    print(mat.id)
    if mat.check_HRR_conjecture():
        break


# The result of the program: none of the matroids in the list break the conjecture!