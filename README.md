# VDA-RWR
This project is used for prioritizing antiviral drugs against SARS-CoV-2.

Introduction
---
The _data_ folder contain 3 files.

+ virus-drug association matrix: the associations between viruses and drugs

+ virus similarity matrix: the similarity matrix between viruses

+ drug similarity matrix: the similarity matrix between drugs

The _source_ folder contain source file.

Usage
---
The VDA-RWR is writed by Python. Therefore, please install Python and numpy pakage.  

In _VDA-RWR.py_ file:  
```fun(A, SD, SV, lam, alpha, r)``` needs 6 arguments, A denotes association matrix, Sd denotes drug similarity matrix, Sv denotes virus similarity matrix. It will return a score matrix for virus-drug associations. The other three parameters are hyperparameter.
