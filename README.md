# DNA_features  
***********************
### 格式和运行
*******************
* 文件格式：标准的fasta文件格式

* 运行
```py
python feature.py -fasta fastafile
```

* 输出： 所有的特征以文件形式保存，文件名字是特征名字
* 其实，DNC就是2-mer，TNC就是3-mer。而kmer中的k我默认设置的是4，也就是4-mer。
