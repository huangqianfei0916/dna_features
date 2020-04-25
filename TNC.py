#!/usr/bin/env python
#_*_coding:utf-8_*_

import re
import sys, os
import numpy as np
import pandas as pd
import itertools
from collections import Counter
import numpy as np
from kmer import Kmer
def TNC(fastas, **kw):
    AA = 'ACGT'
    encodings = []

    AADict = {}
    for i in range(len(AA)):
        AADict[AA[i]] = i


    for i in fastas:
        sequence = i.strip()
        code = []
        tmpCode = [0] * 64
        for j in range(len(sequence) - 3 + 1):
            tmpCode[AADict[sequence[j]] * 16 + AADict[sequence[j+1]]*4 + AADict[sequence[j+2]]] = \
                tmpCode[AADict[sequence[j]] * 16 + AADict[sequence[j+1]]*4 + AADict[sequence[j+2]]] +1

        if sum(tmpCode) != 0:
            tmpCode = [i/sum(tmpCode) for i in tmpCode]
        code = code + tmpCode
        encodings.append(code)
    # np.savetxt("tnc", encodings)
    pd.DataFrame(encodings).to_csv("TNC.csv", header=None, index=False)
    return np.array(encodings)


# def TNC(fastas, **kw):
#     Kmer(fastas,k=3)