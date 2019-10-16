#!/usr/bin/env python
# _*_coding:utf-8_*_
import numpy as np
def binary(fastas, **kw):
    AA = 'ACGT'
    encodings = []


    for i in fastas:
        sequence = i.strip()
        code = []
        for aa in sequence:
            if aa == '-':
                code = code + [0, 0, 0, 0]
                continue
            for aa1 in AA:
                tag = 1 if aa == aa1 else 0
                code.append(tag)
        encodings.append(code)
    return np.array(encodings)

