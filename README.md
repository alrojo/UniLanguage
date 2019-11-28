# What is UniLanguage?
[PAPER](bioxiv)&nbsp;&nbsp;&nbsp;&nbsp;[CITATION](bioxiv)&nbsp;&nbsp;&nbsp;&nbsp;[[CODE](github)]&nbsp;&nbsp;&nbsp;&nbsp;[[DATASET DOWNLOAD](dtu)]

UniLanguage is a dataset of proteins that has been scraped from UniProt (2019-10-01) for the purpose of **language modeling on protein sequences**.
UniLanguage is homology partitioned, split by domain, fragments, and quality (experimental vs. predicted).
We provide baselines on UniLanguage using N-gram and Recurrent Neural Network Language Models (RNN-LM).
How to download the dataset can be found near the bottom of this post.
The provided [code] to reproduce our results comes with automatic dataset downloading.

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

## Baseline
Our N-gram baseline uses add-one trick ([Jurafsky and Martin](https://web.stanford.edu/~jurafsky/slp3/)).
Our RNN-LM is implemented with the [AWD-LSTM](https://github.com/salesforce/awd-lstm-lm) architecture.
We find the optimal hyperparameters for the AWD-LSTM with bayesian hyperparameter optimization using the free academic license to [SigOpt](http://sigopt.com/).

# The challenge
Build a language model that can predict the next amino acid in a protein sequence.
Resources on building a language model: [Karpathy blogpost](http://karpathy.github.io/2015/05/21/rnn-effectiveness/), [Jurafsky & Martin](https://web.stanford.edu/~jurafsky/slp3/), [AWD-LSTM](https://github.com/salesforce/awd-lstm-lm), [fairseq](https://github.com/pytorch/fairseq/tree/master/examples/language_model)
Train it on a training set, e.g. high quality eukarya, and test it on the testset.
See **if you can beat our performance**.
If you can, please submit a technical report, e.g. to arxiv, and **[send it to us](mailto:jjalma@dtu.dk)**.
This way we can keep track of current state-of-the-art on this language modeling dataset.


# Overview of datasets and results
Our task contains multiple datasets for training and testing. We provide the simple version (only Eukarya) and the full version (all datasets, including fragments).
Notice that the full dataset also contains fragments for validation and testing. This is a result of our homology partitioning, we provide them, but do not use them in our own results.

## Simple (ML reseachers)
For simplicity we of having one validation and testset, we provide links here to the Eukarya validation, test, high quality train, and low quality train.

| Link         | Partitions | Domain   | Quality | Samples | Mean Length | Fragments |
|--------------|------------|----------|---------|---------|-------------|-----------|
| [Download]() | Train      | Eukarya  | High    |         |             | No        |
| [Download]() | Train      | Eukarya  | Low     |         |             | No        |
| [Download]() | Valid      | Eukarya  | High    |         |             | No        |
| [Download]() | Test       | Eukarya  | High    |         |             | No        |

## Simple results
| Training set | Validation perplexity | Test perplexity |
|--------------|-----------------------|-----------------|
| High quality |                       | 14.04           |
| Low quality  |                       | 14.67           |
| Combined     |                       | 14.28           |

## All datasets
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

## Results all data
| Domain   | Training set          | Validation perplexity | Test perplexity |
|----------|-----------------------|-----------------------|-----------------|
| Eukarya  | Euk_exp, Euk_pred     |                       | 14.28           |
| Bacteria | Bact_exp, Bact_pred   |                       | 9.93            |
| Archaea  | Arch_exp, Arch_pred   |                       | 15.92           |
| Virus    | Virus_exp, Virus_pred |                       | 17.17           |
| Mean     |                       |                       | 14.32           |

Please see the result section of our [paper]() for extended results, such as using all domains together, only using predicted, or only using experimental.

# Citation
[PAPER](bioxiv)
PUT IN CITATION
