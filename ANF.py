import numpy as np
def ANF(fastas, **kw):

    AA = 'ACGT'
    encodings = []

    for i in fastas:
        sequence = i.strip()
        code = []
        for j in range(len(sequence)):
            code.append(sequence[0: j + 1].count(sequence[j]) / (j + 1))
        encodings.append(code)
    return np.array(encodings)