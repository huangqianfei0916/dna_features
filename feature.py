#!/usr/bin/env python
# _*_coding:utf-8_*_
import sys

from sklearn.preprocessing import MinMaxScaler

sys.path.extend(["../../", "../", "./"])
import sys, os
import pandas as pd
import numpy as np

from binary import binary
from DNC import DNC
from TNC import TNC
from ENAC import ENAC
from NAC import NAC
from ANF import ANF
from CKSNAP import CKSNAP
from PseEIIP import PseEIIP
from EIIP import EIIP
from RCKmer import RCKmer
from kmer import Kmer
from NCP import NCP
import argparse


def read_fasta(file):
    f = open(file)
    documents = f.readlines()
    string = ""
    flag = 0
    fea=[]
    for document in documents:
        if document.startswith(">") and flag == 0:
            flag = 1
            continue
        elif document.startswith(">") and flag == 1:
            string=string.upper()
            fea.append(string)
            string = ""
        else:
            string += document
            string = string.strip()
            string=string.replace(" ", "")

    fea.append(string)
    f.close()
    return fea


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-fasta', required=True, help="fasta file name")
    args = parser.parse_args()
    print(args)


    fasta = read_fasta(args.fasta)

    print(np.shape(fasta))

    feature_name=["binary","NCP","Kmer","DNC","TNC","ENAC","NAC","ANF","CKSNAP","PseEIIP","EIIP","RCKmer"]

    feature={"binary":"binary(fasta)","NCP":"NCP(fasta)","Kmer":"Kmer(fasta)"
        , "DNC": "DNC(fasta)","TNC":"TNC(fasta)","ENAC":"ENAC(fasta)","NAC":"NAC(fasta)",
            "ANF":"ANF(fasta)","CKSNAP":"CKSNAP(fasta)" ,"PseEIIP":"PseEIIP(fasta)",
             "EIIP":"EIIP(fasta)","RCKmer":"RCKmer(fasta)"}

    for i in feature_name:
        eval(feature[i])


if __name__ == '__main__':
    main()
