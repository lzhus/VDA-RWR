# VDA-RWR
This project is used for prioritizing anti-viral drugs against SARS-CoV-2.

Introduction
---
The _data_ folder contain 3 files.

+ virus-drug assciation matrix: the association between viruses and drugs

+ virus similarity matrix: the similarity matrix between viruses

+ drug similarity matrix: the similarity matrix between drugs

The _source_ folder contain source file.

Usage
---
The VDA-RWR is writed by python. Therefore, please install Python and numpy pakage.  

In _VDA-RWR.py_ file:  
```fun(A, Sd, Sv)``` need three arguments, A presedents assciation matrix, Sd presedents drug similarity matrix, Sv presedents virus similarity matrix. It will return a matrix with score of each virus-drug interaction.
