# dna_features  
***********************
### 格式和运行
*******************
* 这是一个常用的DNA特征提取方法的实现，通过下面命令行的运行可以得到多个特征文件。
* 输入文件格式：标准的fasta文件格式

* 运行
```py
python feature.py -fasta fastafile
```

* 输出： 所有的特征以文件形式保存，文件名字是特征名字
* 其实，DNC就是2-mer，TNC就是3-mer。而kmer中的k我默认设置的是4，也就是4-mer。
