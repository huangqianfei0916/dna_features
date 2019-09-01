
def EIIP(fastas, **kw):

    AA = 'ACGT'

    EIIP_dict ={
        'A': 0.1260,
        'C': 0.1340,
        'G': 0.0806,
        'T': 0.1335,
        '-': 0,
        # 'A': 0.25,
        # 'C': 0.5,
        # 'G': 0.75,
        # 'T': 1.0,
        # '-': 0,
    }

    encodings = []
    header = ['#', 'label']
    for i in range(1, len(fastas[0][1]) + 1):
        header.append('F'+str(i))
    encodings.append(header)

    for i in fastas:
        name, sequence, label = i[0], i[1], i[2]
        code = [name, label]
        for aa in sequence:
            code.append(EIIP_dict.get(aa, 0))
        encodings.append(code)
    return encodings
