# FailureAndGeneralizationDataset

This repository contans dataset for the paper, [The Fine Line between Linguistic Generalization and Failure in Seq2Seq-Attention Models] (https://arxiv.org/pdf/1805.01445.pdf), accepted for GenDeep conference at NAACL'18. 

## Data Files

The grammar is created so that each input symbol has some associated id value (i.e the input symbol 'C' has an id 3), and each input symbol maps to three output symbols (the symbols A{id}\_{1 or 2}, B{id}\_{1 or 2}, C{id}\_{1 or 2}, in any order), you can tell if the output is correct by making sure the length of the output is 3\*length of the input, the ith group of three in the output has the same id as the ith input, and the ith group of three in the output contains at least one A, B, and C. 

## Accuracy Measurement

The accuracy measure is a zero-one loss measure (either right or wrong, no partial credit). The start of sequence and end of sequence tokens are not counted when calculated accuracy. 


## Bibtex

@article{DBLP:journals/corr/abs-1805-01445,
  author    = {Noah Weber and
               Leena Shekhar and
               Niranjan Balasubramanian},
  title     = {The Fine Line between Linguistic Generalization and Failure in Seq2Seq-Attention
               Models},
  journal   = {CoRR},
  volume    = {abs/1805.01445},
  year      = {2018},
  url       = {http://arxiv.org/abs/1805.01445},
  archivePrefix = {arXiv},
  eprint    = {1805.01445},
  timestamp = {Mon, 13 Aug 2018 16:46:03 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1805-01445},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
