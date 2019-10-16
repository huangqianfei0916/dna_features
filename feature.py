#!/usr/bin/env python
# _*_coding:utf-8_*_
import sys

from sklearn.preprocessing import MinMaxScaler

sys.path.extend(["../../", "../", "./"])
import sys, os
import pandas as pd
import numpy as np

from DNA_features.binary import binary
from DNA_features.DNC import DNC
from DNA_features.TNC import TNC
from DNA_features.ENAC import ENAC
from DNA_features.NAC import NAC
from DNA_features.ANF import ANF
from DNA_features.CKSNAP import CKSNAP
from DNA_features.PseEIIP import PseEIIP
from DNA_features.EIIP import EIIP
from DNA_features.RCKmer import RCKmer
from DNA_features.kmer import Kmer
from DNA_features.NCP import NCP
import argparse

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
    parser = argparse.ArgumentParser()
    parser.add_argument('-fasta', required=True, help="fasta file name")
    args = parser.parse_args()
    print(args)


    fasta = read_fasta(args.fasta)

    feature_name=["binary","NCP","Kmer","DNC","TNC","ENAC","NAC","ANF","CKSNAP","PseEIIP","EIIP","RCKmer"]

    feature={"binary":"binary(fasta)","NCP":"NCP(fasta)","Kmer":"Kmer(fasta)"
        , "DNC": "DNC(fasta)","TNC":"TNC(fasta)","ENAC":"ENAC(fasta)","NAC":"NAC(fasta)",
            "ANF":"ANF(fasta)","CKSNAP":"CKSNAP(fasta)" ,"PseEIIP":"PseEIIP(fasta)",
             "EIIP":"EIIP(fasta)","RCKmer":"RCKmer(fasta)"}

    for i in feature_name:
        eval(feature[i])


if __name__ == '__main__':
    main()
