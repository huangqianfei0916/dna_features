#!/usr/bin/env python
#_*_coding:utf-8_*_

import sys, os, platform
import pandas as pd
from Prcessing.EIIP import EIIP
from Prcessing.ANF import ANF
from Prcessing.binary import binary
from Prcessing.CKSNAP import CKSNAP
from Prcessing.DNC import DNC
from Prcessing.ENAC import ENAC
from Prcessing.NAC import NAC
from Prcessing.NCP import NCP
from Prcessing.PseEIIP import PseEIIP
from Prcessing.PSTNPds import PSTNPds
from Prcessing.PSTNPss import PSTNPss
from Prcessing.TNC import TNC
from Prcessing.RCKmer import RCKmer
from Prcessing.kmer import Kmer
import re

def read_nucleotide_sequences(file):
    if os.path.exists(file) == False:
        print('Error: file %s does not exist.' % file)
        sys.exit(1)
    with open(file) as f:
        records = f.read()
    if re.search('>', records) == None:
        print('Error: the input file %s seems not in FASTA format!' % file)
        sys.exit(1)
    records = records.split('>')[1:]
    fasta_sequences = []
    for fasta in records:
        array = fasta.split('\n')
        header, sequence = array[0].split()[0], re.sub('[^ACGTU-]', '-', ''.join(array[1:]).upper())
        header_array = header.split('|')
        name = header_array[0]
        label = header_array[1] if len(header_array) >= 2 else '0'
        label_train = header_array[2] if len(header_array) >= 3 else 'training'
        sequence = re.sub('U', 'T', sequence)
        fasta_sequences.append([name, sequence, label, label_train])
    return fasta_sequences

def main():
    fasta = read_nucleotide_sequences("feature_fasta.fasta")
    a = RCKmer(fasta)

    df = pd.DataFrame(a)
    print(df)
    df.to_csv("./csv/RCKMER.csv",header=None,index=None)


if __name__ == '__main__':
    main()
