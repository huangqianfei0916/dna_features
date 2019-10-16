#!/usr/bin/env python
# _*_coding:utf-8_*_

import numpy as np
from collections import Counter


def NAC(fastas, **kw):
    NA = 'ACGT'
    encodings = []


    for i in fastas:
        sequence = i.strip()
        count = Counter(sequence)
        for key in count:
            count[key] = count[key] / len(sequence)
        code = []
        for na in NA:
            code.append(count[na])
        encodings.append(code)
    return np.array(encodings)
