#!/usr/bin/env python
# _*_coding:utf-8_*_
import sys

from sklearn.preprocessing import MinMaxScaler

sys.path.extend(["../../", "../", "./"])
import sys, os
import pandas as pd
import numpy as np

from DNA.binary import binary
from DNA.DNC import DNC
from DNA.TNC import TNC
from DNA.ENAC import ENAC
from DNA.NAC import NAC
from DNA.ANF import ANF
from DNA.CKSNAP import CKSNAP
from DNA.PseEIIP import PseEIIP
from DNA.EIIP import EIIP
from DNA.RCKmer import RCKmer
from DNA.kmer import Kmer
from DNA.NCP import NCP


def read_fasta(file):
    f = open(file)
    docs = f.readlines()
    fasta = []
    for seq in docs:
        if seq.startswith(">"):
            continue
        else:
            fasta.append(seq)

    return np.array(fasta)


def main():
    fasta = read_fasta("feature_fasta.fasta")

    # 164d
    t10 = binary(fasta)
    np.savetxt("binary", t10)

    # 123d
    t11 = NCP(fasta)
    np.savetxt("ncp", t11)

    # 64
    t12 = Kmer(fasta)
    np.savetxt("kmer", t12)

    t1 = DNC(fasta)
    np.savetxt("dnc", t1)

    t2 = TNC(fasta)
    np.savetxt("tnc", t2)

    t3 = ENAC(fasta)
    np.savetxt("enac", t3)

    t4 = NAC(fasta)
    np.savetxt("nac", t4)

    t5 = ANF(fasta)
    np.savetxt("anf", t5)

    t6 = CKSNAP(fasta)
    np.savetxt("cksnap", t6)

    t7 = PseEIIP(fasta)
    np.savetxt("pseeiip", t7)

    t8 = EIIP(fasta)
    np.savetxt("eiip", t8)

    t9 = RCKmer(fasta)
    np.savetxt("rckmer", t9)


if __name__ == '__main__':
    main()
