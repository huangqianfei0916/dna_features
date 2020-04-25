import numpy as np
import pandas as pd
def CKSNAP(fastas, gap=5, **kw):
    if gap < 0:
        print('Error: the gap should be equal or greater than zero' + '\n\n')
        return 0

    AA = 'ACGT'
    encodings = []
    aaPairs = []
    for aa1 in AA:
        for aa2 in AA:
            aaPairs.append(aa1 + aa2)

    for i in fastas:
        sequence = i.strip()
        code = []

        for g in range(gap + 1):
            myDict = {}
            for pair in aaPairs:
                myDict[pair] = 0
            # sum = 0
            sum = len(sequence) - 1 - g;
            for index1 in range(len(sequence)):
                index2 = index1 + g + 1
                if index1 < len(sequence) and index2 < len(sequence) and sequence[index1] in AA and sequence[
                    index2] in AA:
                    myDict[sequence[index1] + sequence[index2]] = myDict[sequence[index1] + sequence[index2]] + 1
                    # sum = sum + 1
            for pair in aaPairs:
                code.append(myDict[pair] / sum)
        encodings.append(code)
    # np.savetxt("cksnap", encodings)
    pd.DataFrame(encodings).to_csv("CKSNAP.csv", header=None, index=False)

    return np.array(encodings)
