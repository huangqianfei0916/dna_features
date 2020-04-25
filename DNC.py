import re
import numpy as np
import pandas as pd
from kmer import Kmer
def DNC(fastas, **kw):
    base = 'ACGT'

    encodings = []

    AADict = {}
    for i in range(len(base)):
        AADict[base[i]] = i

    for i in fastas:
        sequence= i.strip()
        code = []
        tmpCode = [0] * 16
        for j in range(len(sequence) - 2 + 1):
            tmpCode[AADict[sequence[j]] * 4 + AADict[sequence[j+1]]] = tmpCode[AADict[sequence[j]] * 4 + AADict[sequence[j+1]]] +1
        if sum(tmpCode) != 0:
            tmpCode = [i/sum(tmpCode) for i in tmpCode]
        code = code + tmpCode
        encodings.append(code)
    # np.savetxt("dnc", encodings)
    pd.DataFrame(encodings).to_csv("DNC.csv", header=None, index=False)
    return np.array(encodings)

# def DNC(fastas, **kw):
#     Kmer(fastas,k=2)
