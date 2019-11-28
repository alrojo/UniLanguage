# What is UniLanguage?
[[PAPER](bioxiv)]&nbsp;&nbsp;&nbsp;&nbsp;[[CITATION](bioxiv)]&nbsp;&nbsp;&nbsp;&nbsp;[[CODE](github)]&nbsp;&nbsp;&nbsp;&nbsp;[[DATASET DOWNLOAD](dtu)]

UniLanguage is a dataset of proteins that has been scraped from UniProt (2019-10-01) for the purpose of **language modeling on protein sequences**.
UniLanguage is homology partitioned, split by domain, fragments, and quality (experimental vs. predicted).
We provide baselines on UniLanguage using N-gram and Recurrent Neural Network Language Models (RNN-LM).
How to download the dataset can be found near the bottom of this post.
The provided [code](github) to reproduce our results comes with automatic dataset downloading.

## What is language modelling?
Language modeling is the task of generating a probability distribution over a sequence.
Leanguage models have proven important for learning context and **has pushed state-of-the-art in natural language processing**, which is why we are now developing language modeling datasets to investigate this technology within the protein domain.

## Why proteins?
**Proteins have a high similarity to text**: discrete symbols (amino acids), dictionary of up to 25 symbols (similar to characters), average length of 335 (like a paragraph), and access to large databases of unlabelled sequences in UniProt (akin English Wikipedia).
Moreover, proteins have many supervised prediction tasks with limited data available (e.g. CullPDB).

## Protein challenges
**Priors within language cannot be assume for protein sequence**.
E.g. many proteins are more than 90% identical; ruining the i.i.d. assumption of SGD and train-/val-/test set splits, different domains of life (zebrafish vs. ebola virus) might not have much in common; corresponding to mixing chinese with english text, 99% of UniProt has not been experimentally validated, and many proteins are represented only as fragments; often noncontigous.

# Process of creating UniLanguage
We scrape all of UniProt - **250M proteins as of 2019-10-01**.
The proteins with experimental evidence (high quality, 1% of UniProt) are homology partitioned, with 20% homology, into train-, validation-, and test set with 60% train, 10% validation and 30% test for each domain on both full proteins and fragments.

Predicted proteins (low quality, 99% of UniProt) are homology compared against the validation and testset with 20% homology.
If predicted proteins do not overlap they are kept as a predicted training set, split into domains and fragments.
This removes about 50% of the predicted proteins (approx. 85 million!), which truly indicates the homogenousness in UniProt proteins.


# Dataset and results
We provide train, validation and testsets for all domains. Notice that fragments are also included for validation and testing, but we do not use them in our work.

| Link         | Partitions | Domain   | Quality | Samples | Mean Length | Fragments |
|--------------|------------|----------|---------|---------|-------------|-----------|
| [Download]() | Train      | Eukarya  | High    |         |             | No        |
| [Download]() | Train      | Eukarya  | High    |         |             | Yes       |
| [Download]() | Train      | Eukarya  | Low     |         |             | No        |
| [Download]() | Train      | Eukarya  | Low     |         |             | Yes       |
| [Download]() | Valid      | Eukarya  | High    |         |             | No        |
| [Download]() | Valid      | Eukarya  | High    |         |             | Yes       |
| [Download]() | Test       | Eukarya  | High    |         |             | No        |
| [Download]() | Test       | Eukarya  | High    |         |             | Yes       |
| [Download]() | Train      | Bacteria | High    |         |             | No        |
| [Download]() | Train      | Bacteria | High    |         |             | Yes       |
| [Download]() | Train      | Bacteria | Low     |         |             | No        |
| [Download]() | Train      | Bacteria | Low     |         |             | Yes       |
| [Download]() | Valid      | Bacteria | High    |         |             | No        |
| [Download]() | Test       | Bacteria | High    |         |             | No        |
| [Download]() | Train      | Archaea  | High    |         |             | No        |
| [Download]() | Train      | Archaea  | High    |         |             | Yes       |
| [Download]() | Train      | Archaea  | Low     |         |             | No        |
| [Download]() | Train      | Archaea  | Low     |         |             | Yes       |
| [Download]() | Valid      | Archaea  | High    |         |             | No        |
| [Download]() | Test       | Archaea  | High    |         |             | No        |
| [Download]() | Train      | Virus    | High    |         |             | No        |
| [Download]() | Train      | Virus    | High    |         |             | Yes       |
| [Download]() | Train      | Virus    | Low     |         |             | No        |
| [Download]() | Train      | Virus    | Low     |         |             | Yes       |
| [Download]() | Valid      | Virus    | High    |         |             | No        |
| [Download]() | Test       | Virus    | High    |         |             | No        |

# Our model

## Baselines
Our N-gram baseline uses add-one trick ([Jurafsky and Martin](https://web.stanford.edu/~jurafsky/slp3/)).
Our RNN-LM is implemented with the [AWD-LSTM](https://github.com/salesforce/awd-lstm-lm) architecture.
We find the optimal hyperparameters for the AWD-LSTM with bayesian hyperparameter optimization using the free academic license to [SigOpt](http://sigopt.com/).

## Results for N-Gram

## Results for Recurrent Neural Network
| Domain   | Training set          | Validation perplexity | Test perplexity |
|----------|-----------------------|-----------------------|-----------------|
| Eukarya  | Euk_exp, Euk_pred     |                       | 14.28           |
| Bacteria | Bact_exp, Bact_pred   |                       | 9.93            |
| Archaea  | Arch_exp, Arch_pred   |                       | 15.92           |
| Virus    | Virus_exp, Virus_pred |                       | 17.17           |
| Mean     |                       |                       | 14.32           |

# Citation
[[PAPER](bioxiv)]&nbsp;&nbsp;&nbsp;&nbsp;[[CITATION](bioxiv)]&nbsp;&nbsp;&nbsp;&nbsp;[[CODE](github)]&nbsp;&nbsp;&nbsp;&nbsp;[[DATASET DOWNLOAD](dtu)]

PUT IN CITATION
