from collections import Counter

import numpy as np
def ENAC(fastas, window=5, **kw):
    if window < 1:
        print('Error: the sliding window should be greater than zero' + '\n\n')
        return 0

    AA = 'ACGT'
    encodings = []


    for i in fastas:
        sequence = i.strip()
        code = []
        for j in range(len(sequence)):
            if j < len(sequence) and j + window <= len(sequence):
                count = Counter(sequence[j:j + window])
                for key in count:
                    count[key] = count[key] / len(sequence[j:j + window])
                for aa in AA:
                    code.append(count[aa])
        encodings.append(code)
    return np.array(encodings)
