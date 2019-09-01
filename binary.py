#!/usr/bin/env python
# _*_coding:utf-8_*_

def binary(fastas, **kw):
    AA = 'ACGT'
    encodings = []
    header = ['#', 'label']
    for i in range(1, len(fastas[0][1]) * 4 + 1):
        header.append('BINARY.F' + str(i))
    encodings.append(header)

    for i in fastas:
        name, sequence, label = i[0], i[1], i[2]
        code = [name, label]
        for aa in sequence:
            if aa == '-':
                code = code + [0, 0, 0, 0]
                continue
            for aa1 in AA:
                tag = 1 if aa == aa1 else 0
                code.append(tag)
        encodings.append(code)
    return encodings
